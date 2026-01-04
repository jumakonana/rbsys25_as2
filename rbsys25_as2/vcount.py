import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

rclpy.init()
n = 0

class Vcount(Node):
    def __init__(self):
        super().__init__('vcount')
        
        global pub

        self.declare_parameter("deadline", 10)
        

        pub = self.create_publisher(Int16, "countup", 10)
        #self.create_timer(0.5, self.cb)

    def cb(self):
        global n
        deadline = self.get_parameter("deadline").value
        deadline += 1
        self.get_logger().info(f"{deadline}")
        n = deadline
       
        self.create_timer(0.5, self.cb)
        msg = Int16()
        msg.data = n
        pub.publish(msg)

def main():
    node = Vcount()
    rclpy.spin(node)
