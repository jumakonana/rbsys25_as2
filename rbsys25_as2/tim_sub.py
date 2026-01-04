import rclpy
from rclpy.node import Node
from count_msgs.msg import Count


rclpy.init()


class Tim_Sub(Node):
    def __init__(self):
        super().__init__('tim_sub')
        self.create_subscription(Count, 'count', self.cb, 10)

    def cb(msg, self):
        self.get_logger().info("Listen: {msg}")


def main():
    node = Tim_Sub()
    rclpy.spin(node)
