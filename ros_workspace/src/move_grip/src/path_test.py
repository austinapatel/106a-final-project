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

#Define global variables
object_robot_angle = None
wall_object_angle = None

planner = PathPlanner("right_arm")
command = outputMsg.RobotiqVacuumGrippers_robot_output()
pub = rospy.Publisher('RobotiqVacuumGrippersRobotOutput', outputMsg.RobotiqVacuumGrippers_robot_output)

orientation_original = [-180, 0, -180] #[0.0, 1.0, 0.0, 0.0] # Robot Gripper


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
def go_to_pose(position, euler_angles, grip):
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

        raw_input("Press <Enter> to move the arm to goal pose " + "\n\tAngle between object-robot: " + str(object_robot_angle) + "\n\tAngle between wall-object: " + str(wall_object_angle))
        if not planner.execute_plan(plan):
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
    while y_angle < 180:
        print(y_angle)
        go_to_pose([0.840, 0.094, 0.3], [-180, y_angle, -180] , None)
        time.sleep(3)

        wall_object_measurements[y_angle] = wall_object_angle
        object_robot_measurements[y_angle] = object_robot_angle
        print('Took measurement for %s!' % y_angle)
        y_angle = y_angle + increment

    print('Here are the measurements:')
    print(wall_object_measurements)
    print(object_robot_angle)

    drop_object()


def pickup_object():
    go_to_pose([0.840, 0.094, 0.2], orientation_original, None) # slightly above object
    go_to_pose([0.840, 0.094, 0.10], orientation_original, 'g') # grab object

def drop_object():
    # go_to_pose([0.840, 0.094, 0.2], orientation_original, None) # slightly above object
    go_to_pose([0.840, 0.094, 0.10], orientation_original, 'c') # grab object


def goto_initial_pos():
    """
    Go to initial arm location
    """
    go_to_pose([0.864, 0.108, 0.311], orientation_original, None)


def feedback_control_level_out(tolerance=10):
    """
    Closed loop feedback controller to level out the object held by the gripper
    """
    # go_to_pose([0.707, 0.158, 0.456], [-180, 90, -180], None) # Gripper parallel to groun
    rospy.sleep(3) # wait for object to stabilize

    # closed loop control to get to desired position
    while wall_object_angle > tolerance:
        print('Wall object angle is %s which is above tolerance of %s. Fixing...' % (wall_object_angle, tolerance))
        go_to_pose([0.707, 0.158, 0.456], [-180, 90 + 90 - wall_object_angle, -180], None) # Flat position
        rospy.sleep(3)

    print('Wall object angle converged to %s' % wall_object_angle)

def feedback_control_demo():
    goto_initial_pos()
    pickup_object()
    goto_initial_pos()
    feedback_control_level_out()

def main():
    """
    Main Script
    """
    init_ar_tag_listener()
    gripper_startup()
    # find_k_increments(15)
    feedback_control_demo()

# Move to utils later
def calc_k(mass, theta):
    G = 9.81
    d = 0.025 # 2.5 cm (length of small vacuum gripper)

    spring_constant_k = (mass*G*d)/theta

    return spring_constant_k

# Step 1: Find angle
# Step 2: Use angle to find k
# Step 3: Calculate angle of new object with mass and k (known)
# Step 4: Calculate the pose of the end effector to make angle of object relative to base frame 0. (straighten object)
    # Step 4a: Add tag to base of robot
    # Step 4b: Track angle between object and base ar_tags
    # Step 4c: Control the angle needed between the vacuum gripper and object that makes the angle between the object and base frame equal to 0

def calc_angle(mass, k):
    """ Figures out new angle for object given k and the object's mass """
    G = 9.81
    d = 0.025 

    return (mass*G*d)/k 

if __name__ == '__main__':
    rospy.init_node('moveit_node')
    main()
