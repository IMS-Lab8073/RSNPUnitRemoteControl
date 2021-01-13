# 遠隔操作用RSNPユニット利用マニュアル

<h4> 芝浦工業大学 知能機械システム研究室　加藤宏一朗，松日楽　信人</h4>

本システムをご利用予定の方は，お手数ですが下記の連絡先までご連絡ください．また，改善点などのご意見がある方も，下記の連絡先までご連絡ください．**RSNP(Robot Service Network Protocol)をご利用いただくには，使用条件にご同意していただき，RSi事務局にお問い合わせしていただく必要がありますので，ご注意ください．** RSiとRSNPに関しては以下のURLでご参照ください．RSNPユニットのハードウェア，ソフトウェアの仕様に関しては，以下のURLをご参照ください．各種修正履歴に関しては以下のURLをご参照ください．  

[RSiとRSNPに関して](http://robotservices.org/)  
[RSNPユニットの仕様](https://ims-lab8073.github.io/RSNPTutorial2020/Specification.html)  

~~~text  
連絡先：  
芝浦工業大学 機械機能工学科 知能機械システム研究室  
〒135-8548 東京都江東区豊洲3-7-5  
機械工学専攻 修士1年 加藤宏一朗 Koichiro Kato
TEL:03-5859-8073
E-mail:md20024@shibaura-it.ac.jp  
~~~  

<div style="page-break-before:always"></div>

## 1. はじめに  

汎用ユニット(以下，「RSNPユニット」と記載)を，多種多様なロボットやデバイスに外付けで接続することで，取得したデータをRSNP(Robot Serivice Networking Protocol)通信でインターネット経由でサーバにアップロードして蓄積し，Webブラウザ等のGUI上で各ロボットの状態を管理，監視することができる．以下の図のようにRSNPユニットをロボットやデバイスに接続して使用することが可能である．  
![概要図](https://user-images.githubusercontent.com/46204057/104468815-3c321700-55fb-11eb-9f7b-5befc4f6a554.png)

## 2. ユニット使用方法  
### 2.1 WiFiの設定  
電源投入から接続，WiFiの設定は[こちら](https://ims-lab8073.github.io/RSNPTutorial2020/Setting)に詳細に記載があります．**2.5まで**を参照ください．  

まず，接続するルータ等のSSIDとパスワードを調べます．  
次に，`wpa_supplicant.conf`ファイルをエディタで編集します．  

```shell
~$ sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```

※ファイルを編集するためのエディタとして今回は"nano"を使用していますが，好みのものを使用してください．以下，"nano"を使用します．

次のとおりに追記してください．  

~~~text
network={
     ssid="SSIDを記述"
     psk="パスワードを記述"
}
~~~

### 2.2 コンフィグレーションの設定
デフォルトでは以下のようになっています．

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

### 2.3 カメラ用クライアントを立ち上げる

```
$ cd ~/RSNPUnitRemoteControl
```
```
$ java -jar RSNPCameraClient.jar
```


### 2.4 遠隔操作用クライアントを立ち上げる
新しいターミナルを開いてください．
```
$ cd ~/RSNPUnitRemoteControl
```
```
$ java -jar RSNPUnitRemoteControl.jar
```


### 3. ユニット通信用サンプルプログラム使用方法
ユニットとロボットとの通信方法を示します．通信方法はMQTTであり，MQTTブローカーおよびトピック名は2.2のコンフィグレーションに示す通りです．  
デフォルトは以下になります．  

| 項目 | コンフィグレーション名 | デフォルト値 | 説明 |
|:-:|:-:|:-:|:-:|
| ブローカー | broker | localhost | RSNPユニット内部のブローカーです． |
| トピック | subtopic | toUnit/Robotdata | 遠隔操作用クライアント**が**Subscribeする際に使うトピック名です | 
| トピック | pubtopic | fromServer/Velocity | 遠隔操作用クライアント**が**Publishする際に使うトピック名です |

### 3.1 ロボット制御用プログラムを立ち上げる
お使いのPCで以下のサンプルプログラムを動作させる際は，Pythonの`paho-mqtt`をインストールする必要があります．環境に合わせて以下のコマンドを実行してください．

```shell
$ pip install paho-mqtt
```
または，
```shell
$ pip3 install paho-mqtt
```

なお，ROSを使用する場合，ROSのプログラムは**Python2**ですが，デバッグ用プログラムなどは**Python3**で動作させているので注意してください．  
なお，ROSを使用する場合，ROSのプログラムは**Python2**ですが，デバッグ用プログラムなどは**Python3**で動作させているので注意してください．  

#### 3.1.1 RTMを使う場合
本リポジトリにある  
[`RSNPUnitConnector`](https://github.com/IMS-Lab8073/RSNPUnitRemoteControl/tree/main/RSNPUnitConnector_RTCsample)  
を使用することができます．

#### 3.1.2 ROSを使う場合
本リポジトリにある  
[`RSNPUnitConnector`](https://github.com/IMS-Lab8073/RSNPUnitRemoteControl/tree/main/RSNPUnitConnector_ROSsample)  
を使用することができます．  

[rsnpunitconnector.py](https://github.com/IMS-Lab8073/RSNPUnitRemoteControl/blob/main/RSNPUnitConnector_ROSNodesample/remote_control_rsnpunit/scripts/rsnpunitconnector.py)の，`self.hostname`をRSNPユニットのホスト名(デフォルトは`rsnpunit`)またはIPアドレスに変更してください．  

```python
class testNode():
    def __init__(self):
        # MQTT Client
        self.hostname = "localhost"
```

以下のコマンドで起動することができます．  
```shell
$ rosrun remote_control_rsnpunit rsnpunitconnector.py
```

#### 3.1.3 ロボットミドルウェアを使わない場合  
本リポジトリにある  
[`MQTTsample`](https://github.com/IMS-Lab8073/RSNPUnitRemoteControl/tree/main/RSNPUnitConnector_simpleMQTT)  
を使用することができます．  

ROSのサンプルと同様に，以下の`"localhost"`部分を，RSNPユニットのホスト名またはIPアドレスに変更して下さい．  

```python
mqttc = MQTTClient.MyMQTTClass()
# start subscribe
rc = mqttc.run("localhost","fromServer/Velocity")
```

以下のコマンドで実行することができます．  
```shell
$ python sampleMQTT.py
```

### 3.2 デバッグ用プログラムを使用する  
RSNPユニット内にある，[デバッグ用プログラム](https://github.com/IMS-Lab8073/RSNPUnitRemoteControl/tree/main/debug)で動作を確認することができます．  
イメージは以下になります．  

![](https://user-images.githubusercontent.com/46204057/104475528-8d91d480-5602-11eb-8272-3760c6bd45a0.png)

| Pub/Sub | ファイル名 |用途 |
|:-:|:-:|:-:|
| Pub | debug_publisher.py | サーバからくる文字列を送信(publish)します． |
| Sub | debug_subscriber.py | サーバへ送る文字列を受け取り(subscribe)，表示します．フォーマットが異なる場合，エラーとなります．  |

publisherとsubscriber，それぞれ，以下のコマンドで実行することができます．  
```shell
$ cd ~/RSNPUnitRemoteControl
```

publisher  
```shell
$ python3 debug_publisher.py  
```

subscriber 
```shell
$ python debug_subscriber.py  
```