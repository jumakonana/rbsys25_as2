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
        self.minute = 0
        self.second = 0 

    def cb(self):   

        self.get_logger().info(f"{self.minute} {self.second}")
               
        msg = Count()
        msg.minute = self.minute
        msg.second = self.second

       
        self.second += 1
        
        if self.second == 60:
            self.minute += 1
            self.second = 0


        self.pub.publish(msg)

def main():
    node = Pub_Etimer()
    rclpy.spin(node)
