import rclpy
from rclpy.node import Node
from count_msgs.msg import Count


rclpy.init()


class Sub_Etime(Node):
    def __init__(self):
        super().__init__('sub_etime')
        self.sub = self.create_subscription(Count, 'count', self.cb, 10)

    def cb(self, msg):
        self.get_logger().info(f" {msg.minute} : {msg.second}")


def main():
    node = Sub_Etime()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()
