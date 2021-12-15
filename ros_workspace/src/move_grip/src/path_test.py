#!/usr/bin/env python
import sys
from intera_interface import Limb

import rospy
import numpy as np
import traceback
import time

from moveit_msgs.msg import OrientationConstraint
from geometry_msgs.msg import PoseStamped

from path_planner import PathPlanner
try:
    from controller import Controller
except ImportError:
    pass
import gripper_controller as gc
from robotiq_vacuum_grippers_control.msg import _RobotiqVacuumGrippers_robot_output  as outputMsg
from move_grip.msg import MoveGripARMessage
from scipy.spatial.transform import Rotation as R

import matplotlib.pyplot as plt

#Define global variables
object_robot_angle = None
wall_object_angle = None

planner = PathPlanner("right_arm")
command = outputMsg.RobotiqVacuumGrippers_robot_output()
pub = rospy.Publisher('RobotiqVacuumGrippersRobotOutput', outputMsg.RobotiqVacuumGrippers_robot_output)

orientation_original = [-180, 0, -180] #[0.0, 1.0, 0.0, 0.0] # Robot Gripper
object_height = 0.1



def to_quat(euler):
    r = R.from_euler('xyz', euler, degrees=True)
    return r.as_quat()

# Gripping Startup Code -- run before moving to pose
def gripper_startup():
    global command
    command = gc.genCommand('a', command)     #activate 
    pub.publish(command)
    time.sleep(1)
    command = gc.genCommand('c', command)   #release
    pub.publish(command)

#Function for moving to a specified location
def go_to_pose(position, euler_angles, grip, enter=True):
    global command
    goal = PoseStamped()

    # Construct Goals from Positions and Orientations
    goal.header.frame_id = "base"
    # convert euler to quat
    orientation = to_quat(euler_angles)

    #x, y, and z position
    goal.pose.position.x = position[0]
    goal.pose.position.y = position[1]
    goal.pose.position.z = position[2]

    goal.pose.orientation.x = orientation[0]
    goal.pose.orientation.y = orientation[1]
    goal.pose.orientation.z = orientation[2]
    goal.pose.orientation.w = orientation[3]

    #move
    try:
        # Might have to edit this . . . 
        plan = planner.plan_to_pose(goal, [])

        if (enter):
            raw_input("Press <Enter> to move the arm to goal pose " + "\n\tAngle between object-robot: " + str(object_robot_angle) + "\n\tAngle between wall-object: " + str(wall_object_angle))
        else:
            time.sleep(1)
        if not planner.execute_plan(plan):
            if grip:
                command = gc.genCommand(grip, command)   # do something, this is a hack
                pub.publish(command)

            raise Exception("Execution failed")

        if grip:
            command = gc.genCommand(grip, command)   # do something
            pub.publish(command)

    except Exception as e:
        print e 
        traceback.print_exc()

def callback(message):
    global object_robot_angle
    global wall_object_angle
    object_robot_angle = message.object_robot_angle if not np.isclose(message.object_robot_angle, -1) else object_robot_angle  
    wall_object_angle = message.wall_object_angle if not np.isclose(message.wall_object_angle, -1) else object_robot_angle 

# Define the method which contains the node's main functionality
def init_ar_tag_listener():
    rospy.Subscriber("move_grip_ar_tag",MoveGripARMessage, callback)

def find_k_increments(increment):
    # default_pos = [0.864, 0.108, 0.311]
    # go_to_pose(default_pos, orientation_original, None)
    #
    # go_to_pose([0.840, 0.094, 0.15], orientation_original, None) #slightly above to align object with gripper
    # go_to_pose([0.840, 0.094, 0.10], orientation_original, 'g')


    # go_to_pose([0.840, 0.094, 0.3], orientation_original, None) #move up
    goto_initial_pos()
    pickup_object()
    goto_initial_pos()

    wall_object_measurements = {}
    object_robot_measurements = {}

    y_angle = 0
    while y_angle < 140:
        print("about to do " + str(y_angle))
        go_to_pose([0.840, 0.094, 0.3], [-180, y_angle, -180] , None)
        time.sleep(3)

        wall_object_measurements[y_angle] = wall_object_angle
        object_robot_measurements[y_angle] = object_robot_angle
        print('Took measurement for %s!' % y_angle)
        print("For angle %s, we have wall object angle %s and object robot angle %s" % (y_angle, wall_object_angle, object_robot_angle))
        y_angle = y_angle + increment

    print('Here are the measurements:')
    print(wall_object_measurements)
    print(object_robot_measurements)

    drop_object()


def pickup_object():
    go_to_pose([0.840, 0.094, object_height + 0.01], orientation_original, None) # slightly above object
    go_to_pose([0.840, 0.094, object_height], orientation_original, 'g') # grab object

def drop_object():
    # go_to_pose([0.840, 0.094, 0.2], orientation_original, None) # slightly above object
    go_to_pose([0.840, 0.094, object_height], orientation_original, 'c') # grab object


def goto_initial_pos():
    """
    Go to initial arm location
    """
    go_to_pose([0.864, 0.108, 0.311], orientation_original, None)


def feedback_control_level_out(tolerance=5, goal=90, proportional_constant=0.5):
    """
    Closed loop feedback controller to level out the object held by the gripper
    """

    # go_to_pose([0.707, 0.158, 0.456], [-180, 90, -180], None) # Gripper parallel to groun
    rospy.sleep(3) # wait for object to stabilize

    # closed loop control to get to desired position
    curr = 0
    print('starting closed loop feedback control')
    while np.abs(goal - wall_object_angle) > tolerance:
        print('Wall object error is %s which is above tolerance of %s. Fixing...' % (goal - wall_object_angle, tolerance))
        curr += proportional_constant*(goal - wall_object_angle)
        print("going to move to %s" % curr)
        go_to_pose([0.707, 0.158, 0.456], [-180, curr, -180], None, False) # Flat position
        
        rospy.sleep(1)

    print('Wall object angle converged to %s' % wall_object_angle)

    return [-180, curr, -180]

def feedback_control_demo():
    goto_initial_pos()
    pickup_object()
    goto_initial_pos()
    feedback_control_level_out()

def go_to_box(orientation):
    box_height=-0.15
    time.sleep(2)
    # go_to_pose([0.362, 0.563, 0.186], orientation, None) # intermediate pos
    # time.sleep(2)

    # go in the box
    # go_to_pose([0.308, 0.616, box_height], orientation, None) #z orignally -0.013 # level with box
    # time.sleep(2)
    # go_to_pose([0.55, 0.616, box_height], orientation, 'c') #z orignally -0.013 # into box


    # go on top of the box
    go_to_pose([0.777, 0.435, 0.2], orientation, None)
    time.sleep(2)
    go_to_pose([0.930, 0.380, 0.2], orientation, 'c')


def go_into_box_demo():
    goto_initial_pos()
    pickup_object()
    goto_initial_pos()
    level_orientation = feedback_control_level_out()
    # level_orientation = [-180 ,136.83, -180]
    # go_to_box(level_orientation)
    # go_to_box(orientation_original)

def add_constraint(title, position, orientation, size):
    #Table Constraint
    p = PoseStamped()
    p.header.frame_id = "base"
    #x, y, and z position
    p.pose.position.x = position[0]
    p.pose.position.y = position[1]
    p.pose.position.z = position[2]

    #Orientation as a quaternion
    p.pose.orientation.x = orientation[0]
    p.pose.orientation.y = orientation[1]
    p.pose.orientation.z = orientation[2]
    p.pose.orientation.w = orientation[3]
    planner.add_box_obstacle(size=np.array(size), name=title, pose=p)

def remove_constraint(title):
    planner.remove_obstacle(title)

def move_object_no_cam_to_angle_demo():
    global object_height

    theta_desired = np.radians(90)

    # object masses
    object_1_mass = 0.157 # small
    object_2_mass = 0.345 # medium
    object_3_mass = 0.373 + .084 # large
    
    # object d
    object_1_d = 0.051 # small
    object_2_d = 0.102 # medium
    object_3_d = 0.122 # large

    # object height
    object_1_h = 0.05
    object_2_h = 0.1
    object_3_h = 0.11

    # set params based on which object is being used
    mass = object_1_mass
    object_d = object_1_d
    object_height = object_1_h


    # pick up object
    goto_initial_pos()
    pickup_object()
    goto_initial_pos()

    # compute gripper angle to go to
    candidate_theta_grippers = np.linspace(0,np.pi,1000)
    resulting_object_angles = [calc_object_angle(mass, get_k(gripper_theta), gripper_theta, object_d) for gripper_theta in candidate_theta_grippers]

    smallest_diff = np.inf
    smallest_diff_i = -1
    for i, object_angle in enumerate(resulting_object_angles):
        cur_diff = np.abs(object_angle - theta_desired)
        if cur_diff < smallest_diff:
            smallest_diff = cur_diff
            smallest_diff_i = i

    best_gripper_angle = candidate_theta_grippers[smallest_diff_i]
    best_resulting_object_angle = resulting_object_angles[smallest_diff_i]

    print("found that %s is the best gripper angle, which causes a %s object angle" % (np.degrees(best_gripper_angle), np.degrees(best_resulting_object_angle)))


    # Generate plot
    plt.plot(np.degrees(candidate_theta_grippers), np.degrees(resulting_object_angles), label='Predicted behavior')
    plt.xlabel('Candidate gripper theta (degrees)')
    plt.ylabel('Predicted gripper theta (degrees)')
    plt.axhline(y=np.degrees(theta_desired), color='r', label='Desired object angle', linestyle='dashed')
    plt.axvline(x=np.degrees(best_gripper_angle), color='g', label='Best gripper angle', linestyle='dashed')
    plt.title('Non rigid gripper model curve for mass=%s kg' % mass)
    plt.legend()
    plt.savefig('/home/cc/ee106a/fl21/class/ee106a-ace/Desktop/106a-final-project/figures/mass_%s.png' % mass)

    # go to desired location
    go_to_pose([0.707, 0.158, 0.456], [-180, np.degrees(best_gripper_angle), -180], None) # Flat position

    #
    # k = get_k() # .308
    # angle_rad = calc_object_angle(mass, k, theta_desired)
    # print("Calculated angle (degrees) is: " + str(np.degrees(angle_rad)))
    #
    # go_to_pose([0.707, 0.158, 0.456], [-180, np.degrees(theta_desired + angle_rad), -180], None) # Flat position
    #
    # print(wall_object_angle)

    print('waiting for object to stabilize')
    time.sleep(3)
    print('actual angle between object and robot is %s' % wall_object_angle)
    print('error from desired is %s' % (wall_object_angle - np.degrees(theta_desired)))


def modeling_determine_mass_demo():
    global object_height
    object_height = 0.085

    # 200g is actual weight


    # pick up object
    goto_initial_pos()
    pickup_object()
    goto_initial_pos()

    gripper_angle = np.radians(90) # radians

    # move gripper to 90
    go_to_pose([0.707, 0.158, 0.456], [-180, np.degrees(gripper_angle), -180], None) # Flat position

    # stabilize and measure object wall angle
    time.sleep(3)
    cur_wall_obj_angle = np.radians(wall_object_angle)
    print("Current wall obj angle is %s" % np.degrees(cur_wall_obj_angle))
    
    # compute mass
    mass_computed = compute_m(get_k(gripper_angle), 0.108, gripper_angle, cur_wall_obj_angle)
    print("Mass is computed to be %s" % mass_computed)


def get_k(gripper_angle): # gripper_angle is in radians
    k = 0.361
    return k


def main():
    """
    Main Script
    """
    init_ar_tag_listener()
    gripper_startup()
    # 
    add_constraint("Table", [1.1,.2,-.2], [0,0,0,1], [0.40, 1.20, 0.10]) #Table
    # add_constraint("Box", [1,0.6, .05 + 0.3048/2 - .2],[0,0,0,1],[0.3048, 0.3048, 0.3048]) #Box
    # remove_constraint("Box")
    # remove_constraint('Table')

    # 
    

    # find_k_increments(15)
    #feedback_control_demo()

    # feedback_control_demo()
    # go_into_box_demo()
    # move_object_no_cam_to_angle_demo()
    modeling_determine_mass_demo()
    

# Move to utils later
# def calc_k(mass, theta): #THIS IS THE WRONG FORMULA
#     G = 9.81
#     d = 0.025 # 2.5 cm (length of small vacuum gripper)
#
#
#     spring_constant_k = (mass*G*d)/theta
#     print("no bad")
#
#     return spring_constant_k

# Step 1: Find angle
# Step 2: Use angle to find k
# Step 3: Calculate angle of new object with mass and k (known)
# Step 4: Calculate the pose of the end effector to make angle of object relative to base frame 0. (straighten object)
    # Step 4a: Add tag to base of robot
    # Step 4b: Track angle between object and base ar_tags
    # Step 4c: Control the angle needed between the vacuum gripper and object that makes the angle between the object and base frame equal to 0

def calc_object_angle(mass, k, gripper_angle, object_d):
    """ Figures out new angle for object given k and the object's mass """

    G = 9.81
    d = object_d + 0.025 

    # return (mass * G * d)/k
    return gripper_angle - (mass * G * d * np.sin(gripper_angle) / k)


def compute_m(k, object_d, gripper_angle, object_angle):
    G = 9.81
    d = object_d + 0.025 

    return k*(gripper_angle - object_angle)/(G*d*np.sin(gripper_angle))

if __name__ == '__main__':
    rospy.init_node('moveit_node')
    main()
