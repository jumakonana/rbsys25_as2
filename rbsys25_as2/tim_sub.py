import rclpy
from rclpy.node import Node
from count_msgs.msg import Count


rclpy.init()


class Tim_Sub(Node):
    def __init__(self):
        super().__init__('tim_sub')
        self.sub = self.create_subscription(Count, 'count', self.cb, 10)

    def cb(self, msg):
        self.get_logger().info("Listen: %s" % msg)


def main():
    node = Tim_Sub()
    rclpy.spin(node)
