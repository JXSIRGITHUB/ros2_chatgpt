import os
import time
from typing import DefaultDict
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    ibvs_dir = get_package_share_directory('ros2_chatgpt')
    params_file = LaunchConfiguration(
        'params_file',
        default=os.path.join(
            ibvs_dir,
            'config',
            'chatgpt_params.yaml'))    

    return LaunchDescription([

        Node(
            package='ros2_chatgpt',
            executable='chatgpt_node',
            name='chatgpt_node',
            output='screen',
            parameters=[params_file]),
    ])