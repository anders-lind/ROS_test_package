#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose


def pose_callback(msg_pose: Pose):
    rospy.loginfo("Pose: x=" + str(msg_pose.x) + ", y=" + str(msg_pose.y))

if __name__ == "__main__":
    rospy.init_node("turle_pose_subsriber")

    sub = rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback)
    rospy.loginfo("Subsriber has been started")

    rospy.spin()