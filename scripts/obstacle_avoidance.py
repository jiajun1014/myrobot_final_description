#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class ObstacleAvoider:
    def __init__(self):
        rospy.init_node('obstacle_avoider', anonymous=True)

        rospy.Subscriber('/rrbot/laser/scan', LaserScan, self.scan_callback)

        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        self.move_cmd = Twist()
        self.obstacle_distance_threshold = 3  # 公尺

        rospy.loginfo("🚗 Obstacle Avoider Node Started (Laser: /rrbot/laser/scan)")

    def scan_callback(self, scan_data):
        # 前方 ±15 度 → 720 個 samples 的中間 ±30 個樣本
        mid_index = len(scan_data.ranges) // 2
        front_range = scan_data.ranges[mid_index - 30 : mid_index + 30]

        # 排除無效值
        valid_ranges = [d for d in front_range if 0.1 < d < float('inf')]
        min_distance = min(valid_ranges) if valid_ranges else float('inf')

        if min_distance < self.obstacle_distance_threshold:
            rospy.loginfo(f"⚠️ Obstacle {min_distance:.2f}m ahead. Turning.")
            self.avoid_obstacle()
        else:
            rospy.loginfo("✅ Path clear. Moving forward.")
            self.move_forward()

    def move_forward(self):
        self.move_cmd.linear.x = 0.2
        self.move_cmd.angular.z = 0.0
        self.cmd_vel_pub.publish(self.move_cmd)

    def avoid_obstacle(self):
        self.move_cmd.linear.x = 0.0
        self.move_cmd.angular.z = 0.5  # 可以改成 -0.5 讓他往右轉
        self.cmd_vel_pub.publish(self.move_cmd)

if __name__ == '__main__':
    try:
        node = ObstacleAvoider()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
