# UR_Gripper_Joystick_Control

This package will allow you to control an UR3 Robot with a Gripper using a joystick. 

Code will be divided in two parts : 

- A ROS subcriber node named ur_gripper_joystick_control.py which subscribes to the /joy topic to collect information when joystick's buttons are pressed or axes' buttons are moved. The program will use the Modbus communication protocol to communicate with the robot software.

- A program on Polyscore named Gripper_UR_Control.urp, the robot operating system, where we read Modbus variables to decide what kind of action / movement will be realised.

How does it work ? 

First of all, you need to clone the ROS Driver package for UR robot and launch the bring-up of your robot and run the node, install the joy package to use a joystick and run the joy_node node. 

Then, you can import the urp file and run it and run at the same time the subscriber node and you can control the robot. 
