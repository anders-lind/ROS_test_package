#!/usr/bin/env python3
from math import pi as pi
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist


def pose_callback(pose: Pose):
    cmd = Twist()
    cmd.linear.x = 4
    cmd.angular.z = 0.5
    # Left wall
    if pose.x < 1:
        # Points towards wall
        if  -pi/2.0 > pose.theta or pose.theta > pi/2.0:
            cmd.linear.x = 0
            cmd.angular.z = 4
        else:
            cmd.linear.x = 4
    # Right wall
    if 10 < pose.x:
        # Points towards wall
        if pi/2.0 > pose.theta and pose.theta > -pi/2.0:
            cmd.linear.x = 0
            cmd.angular.z = 4
        else:
            cmd.linear.x = 4
    # Lower wall
    if pose.y < 1:
        if -pi < pose.theta and pose.theta < 0:
            cmd.linear.x = 0
            cmd.angular.z = 4
        else:
            cmd.linear.x = 4
    # Top wall
    if pose.y > 10:
        if 0 < pose.theta and pose.theta < pi:
            cmd.linear.x = 0
            cmd.angular.z = 4
        else:
            cmd.linear.x = 4
    
    pub.publish(cmd)

if __name__ == "__main__":
    rospy.init_node("turtle_avoid_walls")

    sub = rospy.Subscriber("/turtle1/pose", Pose, pose_callback)
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)

    rospy.spin()