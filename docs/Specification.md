# 遠隔操作デモ仕様

ここでは，以下の図に乗っ取ってデータの仕様について記載していきます．

![ユニットとロボットとサーバの接続](https://user-images.githubusercontent.com/46204057/102591811-f8f89b80-4155-11eb-8ef8-16e89d93c01c.png)

## 1. 送信データ仕様
### 1.1 ロボットからユニット
ロボット側はユニットへ以下のデータを送信します．
※今回はデータの送信は任意になります．  

```text
{"data_type":"データの型", "data":"データ内容"}
```

データの種類とデータ内容は以下になります．  
| データの型 | 説明 | データ例 |
|:-:|:-:| :-|
| odometry | 移動ロボットの場合、オドメトリ情報 | x:10,y:10,heading:15 |
| count | 特定のモーション(あいさつなど)のカウント(数字のみ) | 3 |
| other | 上記以外 | 任意の文字列 |

※オドメトリ情報の場合，サンプルプログラム([RTM RTC](https://github.com/IMS-Lab8073/RSNPUnitRemoteControl/tree/main/RSNPUnitConnector_RTCsample/RSNPUnitConnector)/[ROS Node](https://github.com/IMS-Lab8073/RSNPUnitRemoteControl/tree/main/RSNPUnitConnector_ROSNodesample/remote_control_rsnpunit))にある通り，RTMでは[TimedPose2D](https://openrtm.org/doc/idl/1.1/idlreference_ja/structRTC_1_1TimedPose2D.html#a5daf2ba8f444487228f826c280521950)の，`position.x`,`position.y`,`heading`を，ROSでは[nav_msgs/Odomtry.msg](http://docs.ros.org/en/noetic/api/nav_msgs/html/msg/Odometry.html)の，`pose.pose.position.x`,`pose.pose.position.y`，`tf`を用いたロボットの向きを使用します．

### 1.2 ユニットからサーバ(RSNP)
RSNPユニット(またはユニット内部のソフトウェア)は，サーバに以下のデータを送信します．  
※今回は，既に実装済みのため起動さえすれば以下のデータが送信されます．  

```text
{"robotID":"ロボットID", "state":"状態", "data":"ロボットのデータ", sendTime:"送信時間"}
```


## 2. 受信データ仕様
### 2.1 ユニットからロボット
ロボット側はユニットから以下のデータを受信します．  

```text
{"robotID":"controller", "vx":"", "va":"", "option":"", timestamp:"送信時間"}
```

### 2.2 サーバからユニット(RSNP)
RSNPユニット(またはユニット内部のソフトウェア)は，サーバから以下のデータを受信します．  

```text
{"robotID":"controller", "vx":"", "va":"", "option":"", timestamp:"送信時間"}
```
