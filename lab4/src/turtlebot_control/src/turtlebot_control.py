#!/usr/bin/env python
#The line above tells Linux that this file is a Python script,
#and that the OS should use the Python interpreter in /usr/bin/env
#to run it. Don't forget to use "chmod +x [filename]" to make
#this script executable.

#Import the rospy package. For an import to work, it must be specified
#in both the package manifest AND the Python file in which it is used.
import rospy
import tf2_ros
import sys
import numpy as np

from geometry_msgs.msg import Twist, Vector3

#Define the method which contains the main functionality of the node.
def controller(turtlebot_frame, goal_frame):
  """x: -0.428616080439
  - turtlebot_frame: the tf frame of the AR tag on your turtlebot
  - target_frame: the tf frame of the target AR tag
  """

  ################################### YOUR CODE HERE ##############

  #Create a publisher and a tf buffer, which is primed with a tf listener
  pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)
  tfBuffer = tf2_ros.Buffer()
  tfListener = tf2_ros.TransformListener(tfBuffer)
  
  # Create a timer object that will sleep long enough to result in
  # a 10Hz publishing rate
  r = rospy.Rate(10) # 10hz

  K1 = -0.3
  K2 = 1
  # Loop until the node is killed with Ctrl-C
  while not rospy.is_shutdown():
    try:
      trans = tfBuffer.lookup_transform(turtlebot_frame, goal_frame, rospy.Time())

      translation = trans.transform.translation
      rotation = trans.transform.rotation

      # Process trans to get your state error
      # Generate a control command to send to the robot

      # linear_vector = Vector3(0, 0, 0)
      # angular_vector = Vector3(0, 0, 0)

      # print('trans')
      # print(translation)
      # print('rot')
      # print(rotation)
      print(translation)

      y_err, z_err, x_err = translation.x, translation.y, translation.z
      theta_err = rotation.w

      K = np.array([[K1, 0],
                   [0,  K2]])

      vels = np.dot(K, np.array([x_err, y_err]))

      # print("Errors:")  
      # print("x: ", x_err)
      # print("y: ", y_err)
      # print("Velocity: ", vels)


      control_command = Twist(Vector3(vels[0], 0, 0), Vector3(0,0,vels[1]))# Generate this
      # control_command = Twist(Vector3(1, 0, 0), Vector3(0,0,0))
      #################################### end your code ###############

      # rospy.loginfo(control_command)
      pub.publish(control_command)
    except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
      pass
    # Use our rate object to sleep until it is time to publish again
    r.sleep()

      
# This is Python's sytax for a main() method, which is run by default
# when exectued in the shell
if __name__ == '__main__':
  # Check if the node has received a signal to shut down
  # If not, run the talker method

  #Run this program as a new node in the ROS computation graph 
  #called /turtlebot_controller.
  rospy.init_node('turtlebot_controller', anonymous=True)

  try:
    controller(sys.argv[1], sys.argv[2])
  except rospy.ROSInterruptException:
    pass