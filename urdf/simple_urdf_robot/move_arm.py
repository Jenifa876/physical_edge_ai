import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import math

class ArmController(Node):
    def __init__(self):
        super().__init__('arm_controller')
        self.joint1_pub = self.create_publisher(Float64, '/joint_1/command', 10)
        self.joint2_pub = self.create_publisher(Float64, '/joint_2/command', 10)
        self.timer = self.create_timer(0.1, self.move_joints)
        self.angle = 0.0

    def move_joints(self):
        msg1 = Float64()
        msg2 = Float64()
        msg1.data = math.sin(self.angle)
        msg2.data = math.cos(self.angle)
        self.joint1_pub.publish(msg1)
        self.joint2_pub.publish(msg2)
        self.angle += 0.1

def main(args=None):
    rclpy.init(args=args)
    node = ArmController()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
