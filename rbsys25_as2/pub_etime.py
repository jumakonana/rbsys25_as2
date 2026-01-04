import rclpy
from rclpy.node import Node
from count_msgs.msg import Count

rclpy.init()

class Pub_Etimer(Node):
    def __init__(self):
        super().__init__('pub_etimer')         

        self.pub = self.create_publisher(Count, "count", 10)
        self.create_timer(1, self.cb)
        self.n = 0
        self.period = 4
        self.deadline = 10

    def cb(self):   

        self.get_logger().info(f"{self.n}")
        self.n += 1
               
        msg = Count()
        msg.minute = self.period
        msg.second = self.deadline

        self.pub.publish(msg)

def main():
    node = Pub_Etimer()
    rclpy.spin(node)
