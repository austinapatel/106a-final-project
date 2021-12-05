#!/usr/bin/env python
# The line above tells Linux that this file is a Python script, and that the OS
# should use the Python interpreter in /usr/bin/env to run it. Don't forget to
# use "chmod +x [filename]" to make this script executable.

# Import the rospy package. For an import to work, it must be specified
# in both the package manifest AND the Python file in which it is used.
import rospy
import tf2_ros
import scipy
from scipy.spatial.transform import Rotation as R

# Import the String message type from the /msg directory of the std_msgs package.
from move_grip.msg import MoveGripARMessage
from geometry_msgs.msg import TransformStamped

# Define the method which contains the node's main functionality
def init_publisher():

    # Create an instance of the rospy.Publisher object which we can  use to
    # publish messages to a topic. This publisher publishes messages of type
    # std_msgs/String to the topic /chatter_talk
    pub = rospy.Publisher('move_grip_ar_tag', MoveGripARMessage, queue_size=10)
    
    # Create a timer object that will sleep long enough to result in a 10Hz
    # publishing rate
    rate = rospy.Rate(10) # 10hz

    tfBuffer = tf2_ros.Buffer()
    tfListener = tf2_ros.TransformListener(tfBuffer)

    # Loop until the node is killed with Ctrl-C
    while not rospy.is_shutdown():
        # Construct a string that we want to publish (in Python, the "%"
        # operator functions similarly to sprintf in C or MATLAB)
        pub_time = rospy.get_time()
        # pub_input = raw_input("Please enter a line of text and press <Enter>: ")
        
        object_robot_angle=-1
        wall_object_angle=-1

        # Get the transform between the AR Tags
        rotation_quaternion = None
        try:
            target_frame = "ar_marker_0" # On the object
            source_frame = "ar_marker_1" # On the robot
            trans = tfBuffer.lookup_transform(target_frame, source_frame, rospy.Time())
            rotation_quaternion = trans.transform.rotation
             # Use the transform to compute the angle between the the object and the end effector
            r = R.from_quat([rotation_quaternion.x, rotation_quaternion.y, rotation_quaternion.z, rotation_quaternion.w])
            z, y, x = r.as_euler('zyx', degrees=True)
            object_robot_angle = z

            base_frame = "ar_marker_2" # On the wall
            trans2 = tfBuffer.lookup_transform(base_frame, source_frame, rospy.Time())
            rotation_quaternion2 = trans2.transform.rotation
            r2 = R.from_quat([rotation_quaternion2.x, rotation_quaternion2.y, rotation_quaternion2.z, rotation_quaternion2.w])
            z2, y2, x2 = r2.as_euler('zyx', degrees=True)
            wall_object_angle = z2


            timestamp_msg = MoveGripARMessage(object_robot_angle, wall_object_angle, pub_time)
            pub.publish(timestamp_msg)
            print(rospy.get_name() + ": I sent \"%s\"" % timestamp_msg)

        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            print("Bad Transform")
        
        # Use our rate object to sleep until it is time to publish again
        rate.sleep()
            
# This is Python's syntax for a main() method, which is run by default when
# exectued in the shell
if __name__ == '__main__':

    # Run this program as a new node in the ROS computation graph called /talker.
    rospy.init_node('move_grip_ar_tag_node', anonymous=True)

    # Check if the node has received a signal to shut down. If not, run the
    # talker method.
    try:
        init_publisher()
    except rospy.ROSInterruptException: pass

