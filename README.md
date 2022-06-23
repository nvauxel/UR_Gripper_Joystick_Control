# UR_Gripper_Joystick_Control

This package will allow you to control at the same time Husky Robot and UR3 Robot with a Gripper using a joystick. 

Code will be divided in two parts : 

- A ROS subcriber node which subscribes to the /joy topic to collect information when joystick's buttons are pressed or axes' buttons are moved. The program will use the Modbus communication protocol to communicate with the robot software.

- A program on Polyscore, the robot operating system, where we read Modbus variables to decide what kind of action / movement will be realised.


