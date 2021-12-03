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

angle = -1


# Define the callback method which is called whenever this node receives a 
# message on its subscribed topic. The received message is passed as the first
# argument to callback().
def callback(message):
    global angle
    # Print the contents of the message to the console
    # print("Message: %s, Sent at: %f, Received at: %f" % (message.message, message.timestamp, rospy.get_time()))
    # rospy.loginfo(message)
    angle = message.angle

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
    orientation = [0.0, 0.7, 0.7, 0.0]
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
    
    # p = PoseStamped()
    # p.header.frame_id = "base"
    # #x, y, and z position
    # p.pose.position.x = 0.5
    # p.pose.position.y = 0.0
    # p.pose.position.z = 0.0

    # #Orientation as a quaternion
    # p.pose.orientation.x = 0.0
    # p.pose.orientation.y = 0.0
    # p.pose.orientation.z = 0.0
    # p.pose.orientation.w = 1.0

    # planner.add_box_obstacle(size=np.array([0.40, 1.20, 0.10]), name="Table", pose=p)

    # p2 = PoseStamped()
    # p2.header.frame_id = "base"
    # #x, y, and z position
    # p2.pose.position.x = 0.5
    # p2.pose.position.y = 0.0
    # p2.pose.position.z = -0.5

    # #Orientation as a quaternion
    # p2.pose.orientation.x = 0.707
    # p2.pose.orientation.y = 0.0
    # p2.pose.orientation.z = 0.0
    # p2.pose.orientation.w = 0.707

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

    # positions = [[0.850, -0.177, 0.045],
    #              [0.953, -0.313, 0.493],
    #              [0.686, -0.499, -0.001]]
    
    # orientations = [[0.0, -1.0, 0.0, 0.0],
    #                 [0.0, -1.0, 0.0, 0.0],
    #                 [0.0, -1.0, 0.0, 0.0]]
    #                 # [0.582, -0.493, 0.574, -0.295],
    #                 # [0.522, -0.507, 0.576, -0.373]]

    positions = [[0.840, 0.094, 0.125],
                [0.840, 0.094, 0.2],
                [0.840, 0.094, 0.125]] #.155

    orientations = [orientation, orientation, orientation]
    # [[1, 0, 0, 0],
    #                 [1, 0, 0, 0],
    #                 [1, 0, 0, 0]]

    grips = ['g', None, 'c']
    
    while not rospy.is_shutdown():
        for i, (position, orientation, grip) in enumerate(zip(positions, orientations, grips)):
            try:
                # if ROBOT == "baxter":
                #     x, y, z = 0.47, -0.85, 0.07
                # else:
                x, y, z = 0.850, -0.177, 0.045
                #original file coors
                # x, y, z = 0.8, 0.05, 0.07
                goal_1 = PoseStamped()
                goal_1.header.frame_id = "base"

                #x, y, and z position
                goal_1.pose.position.x = position[0]
                goal_1.pose.position.y = position[1]
                goal_1.pose.position.z = position[2]

                #Orientation as a quaternion

                #from tf echo
                
                goal_1.pose.orientation.x = orientation[0]
                goal_1.pose.orientation.y = orientation[1]
                goal_1.pose.orientation.z = orientation[2]
                goal_1.pose.orientation.w = orientation[3]

                #original
                # goal_1.pose.orientation.x = 0.0
                # goal_1.pose.orientation.y = -1.0
                # goal_1.pose.orientation.z = 0.0
                # goal_1.pose.orientation.w = 0.0


                # Might have to edit this . . . 
                plan = planner.plan_to_pose(goal_1, [orien_const])

                raw_input("Press <Enter> to move the right arm to goal pose " + str(i) + " angle: " + str(angle) + ": ")
                if not planner.execute_plan(plan):
                    raise Exception("Execution failed")

                # # Gripping Code
                # command = outputMsg.RobotiqVacuumGrippers_robot_output();
                # pub = rospy.Publisher('RobotiqVacuumGrippersRobotOutput', outputMsg.RobotiqVacuumGrippers_robot_output)

                #command = gc.genCommand(gc.askForCommand(command), command)
                if grip:
                    command = gc.genCommand(grip, command)   #do someting
                    pub.publish(command)


            except Exception as e:
                print e 
                traceback.print_exc()
            # else:
            #     break


if __name__ == '__main__':
    rospy.init_node('moveit_node')
    main()
