### ros2_chatgpt

```shell
mkdir -p /yourwork_ws/src
cd yourwork_ws/src
git clone git@github.com:JXSIRGITHUB/ros2_chatgpt.git
cd ..
colcon build --packages-select ros2_chatgpt
```

#### how to work:

add openai key in /config/chatgpt_params.yaml

```sh
cd /yourwork_ws
source devel/setup.bash
ros2 launch ros2_chatgpt chatgpt_launch.py
```

open new termial

```shell
ros2 topic pub /chatgpt_question std_msgs/msg/String "data: 'your question'" -1
```

