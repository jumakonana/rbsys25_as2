import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

rclpy.init()


class Vcount(Node):
    def __init__(self):
        super().__init__('vcount')
        
        self.declare_parameter("deadline", 10)
        
        self.create_timer(0.5, self.cb)

    def cb(self):
        deadline = self.get_parameter("deadline").value

def main():
    node = Vcount()
    rclpy.spin(node)
