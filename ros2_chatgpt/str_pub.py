#!/usr/bin/env python3
# coding=utf-8

import sys
import rclpy
import time
from rclpy.node import Node
from std_msgs.msg import String

class StrPub(Node):
    def __init__(self):
        super().__init__("string_pub_node")
        self._ask_pub = self.create_publisher(String,'/chatgpt_question',10)

    def run(self):
        if(len(sys.argv) > 1):
            question_msg = String()
            question_msg.data = sys.argv[1]
            time.sleep(0.1)
            self._ask_pub.publish(question_msg)
        else:
            self.get_logger().info('请在指令的后面加入要发送的问句')
        time.sleep(0.1)

def main(args=None):
    rclpy.init(args=args)
    str_node = StrPub()
    rclpy.spin(str_node)
    str_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
