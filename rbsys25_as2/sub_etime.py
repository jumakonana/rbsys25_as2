import rclpy
from rclpy.node import Node
from count_msgs.msg import Count


rclpy.init()


class Sub_Etimer(Node):
    def __init__(self):
        super().__init__('sub_etimer')
        self.sub = self.create_subscription(Count, 'count', self.cb, 10)

    def cb(self, msg):
        self.get_logger().info("Listen: %s" % msg)


def main():
    node = Sub_Etimer()
    rclpy.spin(node)
