import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

rclpy.init()
n = 0

class Vcount(Node):
    def __init__(self):
        super().__init__('vcount')
        
        self.declare_parameter("deadline", 10)
        
        self.deadline = self.get_parameter("deadline").value

        self.pub = self.create_publisher(Int16, "countup", 10)
        self.create_timer(1, self.cb)
        
    def cb(self):   

        self.get_logger().info(f"{self.deadline}")
        self.deadline += 1
       
        
  
        msg = Int16()
        msg.data = self.deadline
        self.pub.publish(msg)

def main():
    node = Vcount()
    rclpy.spin(node)
