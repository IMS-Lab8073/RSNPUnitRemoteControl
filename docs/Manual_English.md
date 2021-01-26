# RSNP Unit User Manual for Remote Control

<h4> Shibaura Institute of Technology Intellignet Mchanical Systems Lab Koichiro Kato, Nobuto Matsuhitra</h4>

If you are planning to use this system, please contact us at the following address. If you have any suggestions for improvement, please contact us at the following address. **In order to use RSNP (Robot Service Network Protocol), you need to agree to the terms of use and contact the RSi office. ** For more information about RSi and RSNP, please refer to the following URL: For the hardware and software specifications of the RSNP unit, please refer to the following URL. Please refer to the following URL for the revision history.    

[About RSi and RSNP](http://robotservices.org/)  
[Specification of RSNP Unit](https://ims-lab8073.github.io/RSNPTutorial2020/Specification.html)  

~~~text  
連絡先：  
芝浦工業大学 機械機能工学科 知能機械システム研究室  
〒135-8548 東京都江東区豊洲3-7-5  
機械工学専攻 修士1年 加藤宏一朗 Koichiro Kato
TEL:03-5859-8073
E-mail:md20024@shibaura-it.ac.jp  
~~~  

<div style="page-break-before:always"></div>

<!-- TOC -->

- [RSNP Unit User Manual for Remote Control](#rsnp-unit-user-manual-for-remote-control)
  - [1. Introduction](#1-introduction)
  - [2. How to use the unit](#2-how-to-use-the-unit)
    - [2.1 Setting of WiFi](#21-setting-of-wifi)
    - [2.2 When using RSNP connection](#22-when-using-rsnp-connection)
      - [2.2.1 Configuring the configuration](#221-configuring-the-configuration)
      - [2.2.2 Launch the client for the camera.](#222-launch-the-client-for-the-camera)
      - [2.2.3 Launch the remote control client.](#223-launch-the-remote-control-client)
    - [2.3 Check the operation without RSNP communication (using a debugging program).](#23-check-the-operation-without-rsnp-communication-using-a-debugging-program)
  - [3. How to use the sample program for unit communication](#3-how-to-use-the-sample-program-for-unit-communication)
    - [3.1 Start up the program for robot control.](#31-start-up-the-program-for-robot-control)
      - [3.1.1 When using RTM](#311-when-using-rtm)
      - [3.1.2 In case of using ROS](#312-in-case-of-using-ros)
      - [3.1.3 Without the robot middleware](#313-without-the-robot-middleware)
  - [4. Operate the robot from the operation screen](#4-operate-the-robot-from-the-operation-screen)

<!-- /TOC -->

## 1. Introduction  

We have developed a system in which a general-purpose unit (hereinafter referred to as "RSNP unit") is connected externally to a wide variety of robots and devices, and the acquired data is uploaded to a server via the Internet using RSNP (Robot Serivice Networking Protocol) communication. We have developed a system to manage and monitor the status of each robot on a GUI such as a web browser. This time, we have realized bi-directional communication, and the RSNP unit can be connected to a robot or device and remotely controlled via the Internet, as shown in the figure below.      

<img src="https://user-images.githubusercontent.com/46204057/104468815-3c321700-55fb-11eb-9f7b-5befc4f6a554.png"  width="60%">

## 2. How to use the unit  

**If you wish to use a unit other than the one distributed, go to [here](https://github.com/IMS-Lab8073/RSNPUnitRemoteControl/blob/main/docs/RaspiSetup.md) to complete the various settings.**  

### 2.1 Setting of WiFi  
Power on, connection, and WiFi settings are described in detail at [here](https://ims-lab8073.github.io/RSNPTutorial2020/Setting). Please refer to **2.1 to 2.5**.  

The host name, user name, and password for the distributed unit are as follows.  
| Intem | data |
|:-:|:-:|
| host name | rsnpunit |
| user name | pi |
| password | 8073 |

Turn on the Raspberry Pi and use the commands on the Raspberry Pi to do the following.  
First, find out the SSID and password of the router you want to connect to.  
Next, edit the `wpa_supplicant.conf` file with an editor.  

```shell
$ sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```

This time, "nano" is used as the editor for editing the files. You can use any editor you like. "nano" will be used below.  

Please add the following information.  

~~~text
network={
     ssid="SSID"
     psk="password"
}
~~~

### 2.2 When using RSNP connection
If you want to connect to RSNP, follow the instructions below, but you can also use the debug program without RSNP.   

#### 2.2.1 Configuring the configuration
This is the file that sets the configuration parameters for RSNP client execution.   
It can be edited by the following command.   

```shell
$ cd ~/RSNPUnitRemoteControl
$ sudo nano Config/Config.properties
```

The default value is as follows.    
Please change `robot_id` to the string you gave.   

```
#Configuration
broker = localhost
subtopic = toUnit/Robotdata
pubtopic = fromServer/Velocity
end_point = http://zmini.robo.meo.shibaura-it.ac.jp:8080/RemoteControlSystem/services
robot_id = Raspi1
password = null
debug = false
max_fps = 10
camera_no = 0
```

#### 2.2.2 Launch the client for the camera.

```
$ cd ~/RSNPUnitRemoteControl
```
```
$ java -jar RSNPCameraClient.jar
```


#### 2.2.3 Launch the remote control client.
Open a new terminal.  

```
$ cd ~/RSNPUnitRemoteControl
```
```
$ java -jar RSNPUnitRemoteControl.jar
```

### 2.3 Check the operation without RSNP communication (using a debugging program).   
You can check the operation by using the [debug program](https://github.com/IMS-Lab8073/RSNPUnitRemoteControl/tree/main/debug) in the RSNP unit.  
The image is shown below.  

<img src="https://user-images.githubusercontent.com/46204057/104475528-8d91d480-5602-11eb-8272-3760c6bd45a0.png" width="60%">

| Pub/Sub | File name| Purpose |
|:-:|:-:|:-:|
| Pub | debug_publisher.py | This function publishes a string from the server. |
| Sub | debug_subscriber.py | This function receives (subscribes to) and displays the string sent to the server. If the format is different, an error occurs. |

You can run the following commands for publisher and subscriber, respectively.  
```shell
$ cd ~/RSNPUnitRemoteControl/debug
```

publisher  
```shell
$ python3 debug_publisher.py  
```

subscriber 
```shell
$ python3 debug_subscriber.py  
```


## 3. How to use the sample program for unit communication  
This section shows the communication method between the unit and the robot. The communication method is MQTT, and the MQTT broker and topic name are shown in the configuration of 2.2. The communication data content is [here](https://github.com/IMS-Lab8073/RSNPUnitRemoteControl/blob/main/docs/Specification.md).  
The default is as follows.   

| Item | Configuration name | Default value | Description
|:-:|:-:|:-:|:-:|
| broker | broker | localhost | broker inside RSNP unit.
| topic | subtopic | toUnit/Robotdata | the name of the topic to be **Subscribed** by the remote control client **. 
| topic | pubtopic | fromServer/Velocity | topic name used by remote control client** to **Publish**. |

### 3.1 Start up the program for robot control.
In order to run the following sample programs on your PC, you need to install `paho-mqtt` for Python. Please execute the following commands according to your environment.

```shell
$ pip install paho-mqtt
```
Or
```shell
$ pip3 install paho-mqtt
```

Note that when using ROS, the ROS program runs in **Python2**, but the debugging program and other programs run in **Python3**.  

#### 3.1.1 When using RTM
In this repository.  
[`RSNPUnitConnector`](https://github.com/IMS-Lab8073/RSNPUnitRemoteControl/tree/main/RSNPUnitConnector_RTCsample)  
in this repository.

#### 3.1.2 In case of using ROS
You can use  
[`RSNPUnitConnector`](https://github.com/IMS-Lab8073/RSNPUnitRemoteControl/tree/main/RSNPUnitConnector_ROSsample)  
in this repository.  

In [rsnpunitconnector.py](https://github.com/IMS-Lab8073/RSNPUnitRemoteControl/blob/main/RSNPUnitConnector_ROSNodesample/remote_control_rsnpunit/scripts/rsnpunitconnector.py), change `self.hostname` to the hostname of the RSNP unit (default is `rsnpunit`) or IP address.  

```python
class testNode():
    def __init__(self):
        # MQTT Client
        self.hostname = "localhost"
````

You can start it with the following command.   

```shell
$ rosrun remote_control_rsnpunit rsnpunitconnector.py  
```

#### 3.1.3 Without the robot middleware  
In this repository  
[`MQTTsample`](https://github.com/IMS-Lab8073/RSNPUnitRemoteControl/tree/main/RSNPUnitConnector_simpleMQTT)  
available in this repository can be used.  

As with the ROS sample, change the following ``"localhost"` part to the hostname or IP address of the RSNP unit.  

```python
mqttc = MQTTClient.MyMQTTClass()
# start subscribe
MyMQTTClass() # subscribe rc = mqttc.run("localhost", "fromServer/Velocity")
````

You can run the following command.   

```shell
$ python sampleMQTT.py
```

## 4. Operate the robot from the operation screen  
The URL of the operation screen is as follows. For the details of the operation method, click [here](https://github.com/IMS-Lab8073/RSNPUnitRemoteControl/blob/main/docs/manual_operation.md)  
  
http://zmini.robo.meo.shibaura-it.ac.jp:8080/RemoteControlSystem/network  

The operation screen looks like the following
<img src="https://user-images.githubusercontent.com/46204057/105194023-84fa4a80-5b7c-11eb-9120-fb4348ad95c4.png" width="80%">

Selecting the robot's image will cause the following popup to appear.  
<img src="https://user-images.githubusercontent.com/46204057/105657459-c20d6680-5f07-11eb-82ee-322ca60cc372.png" width="80%">

After moving to the operation screen, the camera image can be viewed by turning on the camera distribution, and the robot can be moved with the arrow keys or the A~E buttons by turning on the robot operation.  
<img src="https://user-images.githubusercontent.com/46204057/105197045-91cc6d80-5b7f-11eb-8d9c-425035352798.png" width="80%">