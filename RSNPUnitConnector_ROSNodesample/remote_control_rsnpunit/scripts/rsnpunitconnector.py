#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from nav_msgs.msg import Odometry   
import tf
from tf.transformations import euler_from_quaternion

import MQTTClient
import time
import json

class testNode():
    def __init__(self):
        # MQTT Client
        self.hostname = "localhost"
        self.mqttc = MQTTClient.MyMQTTClass()
        self.mqttc.run(self.hostname, "fromServer/Velocity")
        
        # ROS
        # Publisher, Subscriber
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
        self.sub = rospy.Subscriber("odom", Odometry, self.roscallback)

    def roscallback(self, msg):
        # ros callback
        odom_x = msg.pose.pose.position.x
        odom_y = msg.pose.pose.position.y
        qx = msg.pose.pose.orientation.x
        qy = msg.pose.pose.orientation.y
        qz = msg.pose.pose.orientation.z
        qw = msg.pose.pose.orientation.w
        q = (qx, qy, qz, qw)
        e = euler_from_quaternion(q)
        odom_theta = e[2] 
        # rospy.loginfo("Odomery: x=%s y=%s theta=%s", odom_x, odom_y, odom_theta)
        # set odom data
        send_data = {"data_type":"odometry", "data":""}
        send_data["data"] = "x:"+str(odom_x)+",y:"+str(odom_y)+",heading"+str(odom_theta)
        send_data_json = json.dumps(send_data)
        # MQTT publish
        self.mqttc.publish_message(self.hostname, "toUnit/RobotData", send_data_json)

    def mqttcallback(self):
        # mqtt callback
        recievedata =  self.mqttc.recieve_data
        recievedata = json.loads(recievedata)
        cmd_vel = Twist()
        cmd_vel.linear.x = float(recievedata["vx"])  / 1000
        cmd_vel.angular.z = float(recievedata["va"]) / 1000
        rospy.loginfo("Velocity from RSNP: vx=%s va=%s ", cmd_vel.linear.x, cmd_vel.angular.z)
        self.Publisher(cmd_vel)

    def Publisher(self, data):
        self.pub.publish(data)

if __name__ == '__main__':
    rospy.init_node('rsnpunitconnector')

    time.sleep(0.5)
    node = testNode()

    while not rospy.is_shutdown():
        # print("run in while")
        if node.mqttc.isNew(): 
            node.mqttcallback()
        rospy.sleep(0.01)