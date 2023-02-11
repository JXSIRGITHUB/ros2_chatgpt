from setuptools import setup
from glob import glob
import os

package_name = 'ros2_chatgpt'

data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ]
data_files.append((os.path.join('share', package_name, 'launch'), glob('launch/*_launch.py')))
data_files.append(('share/' + package_name + '/config', [
                                                    'config/chatgpt_params.yaml',
                                                    ]))



setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='eliot',
    maintainer_email='2411032070@qq.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'chatgpt_node = ros2_chatgpt.chatgpt_node:main',
        'str_pub = ros2_chatgpt.str_pub:main',

        ],
    },
)
