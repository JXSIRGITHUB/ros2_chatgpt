#!/usr/bin/env python3
# coding=utf-8

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from urllib import response
import openai

class ChatGptNode(Node):
    def __init__(self):
        super().__init__("chatgpt_node")
        self.get_logger().info('ChatGPT: 我已经准备好了！向我提问吧 ^_^')
        self.declare_parameter('chatgpt_api_key')
        self.api_key = self.get_parameter('chatgpt_api_key').get_parameter_value().string_value

        self.create_subscription(String,'/chatgpt_question',self._question_cb,10)
        self._response_pub = self.create_publisher(String,'/chatgpt_answer',10)

    def _question_cb(self,msg):
        openai.api_key = self.api_key
        model_engine = "davinci-instruct-beta-v3"
        prompt = msg.data
        self.get_logger().info('------------')
        completion = openai.Completion.create(
            engine = model_engine,
            prompt = prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        if 'choices' in completion:
            if len(completion['choices'])>0:
                response= completion['choices'][0]['text']
                answer_msg = String()
                answer_msg.data = response
                self._response_pub.publish(answer_msg)
            else:
                response = None
        else:
                response = None
        self.get_logger().warn("answer:%s" % response)

def main(args=None):
    rclpy.init(args=args)
    chatgpt_node = ChatGptNode()
    rclpy.spin(chatgpt_node)
    chatgpt_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
