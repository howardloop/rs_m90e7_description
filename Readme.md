# README

此package為計畫使用機器人的URDF

![image-20230420152911935](./pic/Readme/image-20230420152911935.png)



![image-20230420152831855](./pic/Readme/image-20230420152831855.png)

![image-20230517095316574](./pic/Readme/image-20230517095316574.png)

![image-20230517095701780](./pic/Readme/image-20230517095701780.png)





## 測試

Download and check out to "ros2" branch

```shell
cd ros2_ws/src
git clone https://github.com/howardloop/rs_m90e7_description.git -b ros2 
```

Build

```bash
cd ~/ros2_ws/
colcon build
# source ~/ros2_ws/install/setup.bash
```

install exec depend
```shell
rosdep install --from-paths ~/ros2_ws/src/rs_m90e7_description
```

Run
```shell
ros2 launch rs_m90e7_description display.launch
```


