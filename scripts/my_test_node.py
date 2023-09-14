#!/usr/bin/env python3
import rospy

if __name__ == "__main__":
    rospy.init_node("test_node")

    rospy.loginfo("Test node has been started")
    rospy.logwarn("This is a test warning!")
    rospy.logerr("This is a test error!")

    # while not rospy.is_shutdown():
    #     rospy.loginfo("Hello!")
    #     rospy.sleep(0.1)

    rospy.loginfo("End of program")