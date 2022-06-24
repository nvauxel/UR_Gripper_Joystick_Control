# UR_Gripper_Joystick_Control

This package will allow you to control an UR3 Robot with a Gripper using a joystick. 

How it is built ?  

- A ROS subcriber node named ur_gripper_joystick_control.py which subscribes to the /joy topic to collect information when joystick's buttons are pressed or axes' buttons are moved. The program will use the Modbus communication protocol to communicate with the robot software.

- A program named Gripper_UR_Control.urp where we read Modbus variables to decide what kind of action / movement will be realised.

What are prerequisites ? 

- You need a Universal Robot with Polyscope installed (robot operating system)  
- You need to install ModbusClient to use Modbus communication if you do not have it (Use sudo pip3 install yModbusTCP.client). 
- You need a joystick. For exemple, Logitech Gamepad F710 Controller or Xbox 360 Controller. 
- You need ROS 1 Melodic or Noetic on your computer and Universal Robot ROS Driver (clone this git https://github.com/UniversalRobots/Universal_Robots_ROS_Driver)
 
How to assure communication between robot / computer ?

First, you need to configure connection between robot and computer. So, connect your computer to the robot with an RJ45 cable.
Now on Polyscope, go to Settings > System > Network. Choose an valid IP adress like 192.168.xx.xx and set the subnet mask to 255.255.255.0 .
On your computer, make sure that your network configuration is set to manual and choose an other ipadress but the same subnet mask (example : 192.168.56.42 on my robot and 192.168.56.1 on my computer).
Once you see "Network is connected" on Polyscore, it's done !

Then, you need to configure Modbus server to permit sending of information from the computer to the robot. 
Go to Installation > Fieldbus > MODBUS and make sur that your interface corresponds to the image named Modbus_Configuration.jpg

How can I control robots ? 

First of all, you need to clone the ROS Driver package for UR robot and launch the bring-up of your robot and run the node, install the joy package (clone that git https://github.com/ros-drivers/joystick_drivers) to use a joystick and run the joy_node node. 

Then, you can import the urp file and run it and run at the same time the subscriber node and you can control the robot. 

To use the Gripper, use X button to open it and B button to close it. 

To move the UR3 robot, you can do translations following x, y and z axis :

Right joystick high : translation following +y
Right joystick low : translation following -y
Right joystick left : translation following -x
Right joystick right : translation following +x

Use A button to do translations following -z and Y button to do translations following +z. 

To stop a translation, press back button. 
