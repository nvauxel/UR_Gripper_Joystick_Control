#!/usr/bin/env python3

from multiprocessing.connection import wait
import rospy
from sensor_msgs.msg import Joy
from pyModbusTCP.client import ModbusClient


MODBUS_SERVER_IP="192.168.56.42"
c = ModbusClient(host=MODBUS_SERVER_IP, port=502, auto_open=True)
c.host=MODBUS_SERVER_IP
c.port=502
c.open()


def callback(j):
    a=j.buttons[0]
    b=j.buttons[1]
    x=j.buttons[2]
    y=j.buttons[3]
    l3=j.buttons[9]
    r3=j.buttons[10]
    joygauchegd=j.axes[6]
    joygauchehb=j.axes[7]
    joydroitgd=j.axes[3]
    joydroithb=j.axes[4]
    rb=j.buttons[5]
    lb=j.buttons[4]
    lt=j.axes[2]
    rt=j.axes[5]
    start=j.buttons[7]
    back=j.buttons[6]

    
  
    if l3 == 1:
        c.write_single_register(132,1)
        print("Commande MODBUS d'ouverture envoyée")
        rospy.sleep(0.5)
        c.write_single_register(132,0)

    elif r3 == 1:
        c.write_single_register(133,1)
        print("Commande MODBUS de fermeture envoyée")
        rospy.sleep(0.5)
        c.write_single_register(133,0)
    
    elif joydroitgd == 1 :
        c.write_single_register(135,1)
        print("Translation suivant les x négatifs")
    if back == 1 :
        c.write_single_register(135,0)
    
    elif joydroitgd == -1 :
        c.write_single_register(134,1)
        print("Translation suivant les x positifs")
    if back == 1 :
        c.write_single_register(134,0)
    
    elif joydroithb == -1 :
        c.write_single_register(137,1)
        print("Translation suivant les y négatifs")
    if back == 1 :
        c.write_single_register(137,0)
    
    elif joydroithb == 1 :
        c.write_single_register(136,1)
        print("Translation suivant les y positifs")
    if back == 1 :
        c.write_single_register(136,0)      
    
    elif a == 1 :
        c.write_single_register(139,1)
        print("Translation suivant les z négatifs")
    if back == 1 :
        c.write_single_register(139,0)
    
    elif y == 1 :
        c.write_single_register(138,1)
        print("Translation suivant les z postifis")
    if back == 1 :    
        c.write_single_register(138,0)
     
    
      

def listener():

    rospy.init_node('modbus_subscriber', anonymous=True)

    rospy.Subscriber("/joy", Joy, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
