import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

rclpy.init()
node = Node("vcount")

def main():
    rclpy.spin(node)
