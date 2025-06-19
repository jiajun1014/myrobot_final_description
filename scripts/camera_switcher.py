#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
import time

# 初始設定
current_camera = "front"
last_state = "front"
last_switch_time = time.time()
switch_delay = 0.3  # 秒

# Publisher
pub = None

def cmd_vel_callback(msg):
    global current_camera, last_state, last_switch_time

    now = time.time()
    # 判斷是否是後退（含斜後）
    if msg.linear.x < -0.01:
        desired_camera = "rear"
    else:
        desired_camera = "front"

    # 切換條件：狀態不同 & 時間間隔足夠
    if desired_camera != last_state and (now - last_switch_time) > switch_delay:
        current_camera = desired_camera
        last_state = desired_camera
        last_switch_time = now
        rospy.loginfo(f"Switched to {current_camera} camera")

def front_callback(msg):
    if current_camera == "front":
        pub.publish(msg)

def rear_callback(msg):
    if current_camera == "rear":
        pub.publish(msg)

def main():
    global pub
    rospy.init_node('camera_selector')
    pub = rospy.Publisher('/camera_active/image_raw', Image, queue_size=1)

    rospy.Subscriber('/cmd_vel', Twist, cmd_vel_callback)
    rospy.Subscriber('camera1/front_image_raw', Image, front_callback)
    rospy.Subscriber('camera1/rear_image_raw', Image, rear_callback)

    rospy.spin()

if __name__ == '__main__':
    main()
