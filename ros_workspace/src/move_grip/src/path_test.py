#!/usr/bin/env python
"""
Path Planning Script for Lab 7
Author: Valmik Prabhu
"""
import sys
# assert sys.argv[1] in ("sawyer", "baxter")
# ROBOT = sys.argv[1]
ROBOT = "sawyer"

if ROBOT == "baxter":
    from baxter_interface import Limb
else:
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

object_robot_angle = -1
wall_object_angle = -1


# Define the callback method which is called whenever this node receives a 
# message on its subscribed topic. The received message is passed as the first
# argument to callback().
def callback(message):
    global object_robot_angle
    global wall_object_angle
    # Print the contents of the message to the console
    # print("Message: %s, Sent at: %f, Received at: %f" % (message.message, message.timestamp, rospy.get_time()))
    # rospy.loginfo(message)
    object_robot_angle = message.object_robot_angle
    wall_object_angle = message.wall_object_angle

# Define the method which contains the node's main functionality
def listener():

    # Create a new instance of the rospy.Subscriber object which we can use to
    # receive messages of type std_msgs/String from the topic /chatter_talk.
    # Whenever a new message is received, the method callback() will be called
    # with the received message as its first argument.
    rospy.Subscriber("move_grip_ar_tag",MoveGripARMessage, callback)

    # Wait for messages to arrive on the subscribed topics, and exit the node
    # when it is killed with Ctrl+C
    # rospy.spin()


def main():
    """
    Main Script
    """

    listener()

    # Make sure that you've looked at and understand path_planner.py before starting

    planner = PathPlanner("right_arm")
    

    if ROBOT == "sawyer":
        Kp = 0.2 * np.array([0.4, 2, 1.7, 1.5, 2, 2, 3])
        Kd = 0.01 * np.array([2, 1, 2, 0.5, 0.8, 0.8, 0.8])
        Ki = 0.01 * np.array([1.4, 1.4, 1.4, 1, 0.6, 0.6, 0.6])
        Kw = np.array([0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9])
    else:
        Kp = 0.45 * np.array([0.8, 2.5, 1.7, 2.2, 2.4, 3, 4])
        Kd = 0.015 * np.array([2, 1, 2, 0.5, 0.8, 0.8, 0.8])
        Ki = 0.01 * np.array([1.4, 1.4, 1.4, 1, 0.6, 0.6, 0.6])
        Kw = np.array([0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9])


    controller = Controller(Kp, Ki, Kd, Kw, Limb("right"))
    ##
    ## Add the obstacle to the planning scene here
    ##

    # #Create a path constraint for the arm
    # #UNCOMMENT FOR THE ORIENTATION CONSTRAINTS PART
    orientation = [0.0, 1.0, 0.0, 0.0] # Robot Gripper 
    orien_const = OrientationConstraint()
    orien_const.link_name = "right_gripper"
    orien_const.header.frame_id = "base"
    orien_const.orientation.x = orientation[0]
    orien_const.orientation.y = orientation[1]
    orien_const.orientation.z = orientation[2]
    orien_const.orientation.w = orientation[3]
    orien_const.absolute_x_axis_tolerance = 0.1 # default 0.1
    orien_const.absolute_y_axis_tolerance = 0.1
    orien_const.absolute_z_axis_tolerance = 0.1
    orien_const.weight = 1.0
    
    # planner.add_box_obstacle(size=np.array([0.40, 1.20, 0.10]), name="Table", pose=p)
    # planner.add_box_obstacle(size=np.array([0.40, 1.20, 0.10]), name="Wall", pose=p2)
    # planner.remove_obstacle("box")

    # Gripping Startup Code
    command = outputMsg.RobotiqVacuumGrippers_robot_output();
    pub = rospy.Publisher('RobotiqVacuumGrippersRobotOutput', outputMsg.RobotiqVacuumGrippers_robot_output)
    command = gc.genCommand('a', command)     #activate 
    pub.publish(command)
    time.sleep(1)
    command = gc.genCommand('c', command)   #release
    pub.publish(command)


    positions = [
                    [0.840, 0.094, 0.125],  # original
                    # [0.840, 0.094, 0.2],  # Move up along z axis
                    [0.841, -0.160, 0.265], # Move to custom position
                    [0.727, -0.420, 0.125], # Move to drop off location
                    [0.841, -0.160, 0.265], # Move back to custom
                    [0.727, -0.420, 0.125], # Move to drop off location
                    [0.841, -0.160, 0.265], # Move back to custom
                    [0.840, 0.094, 0.125],  # Move to original
                 ] #.155

    orientations = [orientation for _ in positions]

    goals = [PoseStamped() for _ in positions]
    
    # Construct Goals from Positions and Orientations
    for goal, position, orientation in zip(goals, positions, orientations):
        # print(goal)
        print(position)
        print(orientation)
        print("\n")
        goal = PoseStamped()
        goal.header.frame_id = "base"

        #x, y, and z position
        goal.pose.position.x = position[0]
        goal.pose.position.y = position[1]
        goal.pose.position.z = position[2]

        goal.pose.orientation.x = orientation[0]
        goal.pose.orientation.y = orientation[1]
        goal.pose.orientation.z = orientation[2]
        goal.pose.orientation.w = orientation[3]

    grips = ['g', None, 'c', None, 'g', None,'c']
    
    while not rospy.is_shutdown():
        for i, (goal, grip) in enumerate(zip(goals, grips)):
            try:
                # Might have to edit this . . . 
                plan = planner.plan_to_pose(goal, [orien_const])

                raw_input("Press <Enter> to move the arm to goal pose " + str(i) + "\n\tAngle between object-robot: " + str(object_robot_angle) + "\n\tAngle between wall-object: " + str(wall_object_angle))
                if not planner.execute_plan(plan):
                    raise Exception("Execution failed")

                if grip:
                    command = gc.genCommand(grip, command)   # do someting
                    pub.publish(command)

            except Exception as e:
                print e 
                traceback.print_exc()
            # else:
            #     break

# Move to utils later
def calc_k(mass, theta):
    G = 9.81
    d = 0.025 # 2.5 cm (length of small vacuum gripper)


    return (mass*G*d)/theta

# Step 1: Find angle
# Step 2: Use angle to find k
# Step 3: Calculate angle of new object with mass and k (known)
# Step 4: Calculate the pose of the end effector to make angle of object relative to base frame 0. (straighten object)
    # Step 4a: Add tag to base of robot
    # Step 4b: Track angle between object and base ar_tags
    # Step 4c: Figure out the angle needed between the vacuum gripper and object that makes the angle between the object and base frame equal to 0

def calc_angle(mass, k):
    """ Figures out new angle for object given k and the object's mass """
    G = 9.81
    d = 0.025 

    return (mass*G*d)/k 

if __name__ == '__main__':
    rospy.init_node('moveit_node')
    main()
