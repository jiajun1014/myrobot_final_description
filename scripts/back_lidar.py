#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def rear_scan_callback(msg):
    min_distance = min(msg.ranges)
    if min_distance < 0.3:
        rospy.logwarn("🚨 後方太近，停車！距離：%.2f m" % min_distance)
        stop_msg = Twist()
        stop_msg.linear.x = 0.0
        stop_msg.angular.z = 0.0
        cmd_pub.publish(stop_msg)

rospy.init_node('rear_proximity_stop')
cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rospy.Subscriber('/rear_scan', LaserScan, rear_scan_callback)
rospy.spin()
