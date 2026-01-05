# SPDX-FileCopyrightText: 2026 jumakonana
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from count_msgs.msg import Count

class Pub_Etime(Node):
    def __init__(self):
        super().__init__('pub_etime')         

        self.pub = self.create_publisher(Count, "count", 10)
        self.create_timer(1, self.cb)
 
        self.minute = 0
        self.second = 0 

    def cb(self):   
        msg = Count()
        msg.minute = self.minute
        msg.second = self.second
       
        self.second += 1
        
        if self.second == 60:
            self.minute += 1
            self.second = 0

        self.pub.publish(msg)

def main():
    rclpy.init()
    node = Pub_Etime()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()
