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

<!-- TOC -->

- [遠隔操作用RSNPユニット利用マニュアル](#%E9%81%A0%E9%9A%94%E6%93%8D%E4%BD%9C%E7%94%A8rsnp%E3%83%A6%E3%83%8B%E3%83%83%E3%83%88%E5%88%A9%E7%94%A8%E3%83%9E%E3%83%8B%E3%83%A5%E3%82%A2%E3%83%AB)
    - [はじめに](#%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB)
    - [ユニット使用方法](#%E3%83%A6%E3%83%8B%E3%83%83%E3%83%88%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95)
        - [WiFiの設定](#wifi%E3%81%AE%E8%A8%AD%E5%AE%9A)
        - [RSNP接続をする場合](#rsnp%E6%8E%A5%E7%B6%9A%E3%82%92%E3%81%99%E3%82%8B%E5%A0%B4%E5%90%88)
            - [コンフィグレーションの設定](#%E3%82%B3%E3%83%B3%E3%83%95%E3%82%A3%E3%82%B0%E3%83%AC%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%81%AE%E8%A8%AD%E5%AE%9A)
            - [カメラ用クライアントを立ち上げる](#%E3%82%AB%E3%83%A1%E3%83%A9%E7%94%A8%E3%82%AF%E3%83%A9%E3%82%A4%E3%82%A2%E3%83%B3%E3%83%88%E3%82%92%E7%AB%8B%E3%81%A1%E4%B8%8A%E3%81%92%E3%82%8B)
            - [遠隔操作用クライアントを立ち上げる](#%E9%81%A0%E9%9A%94%E6%93%8D%E4%BD%9C%E7%94%A8%E3%82%AF%E3%83%A9%E3%82%A4%E3%82%A2%E3%83%B3%E3%83%88%E3%82%92%E7%AB%8B%E3%81%A1%E4%B8%8A%E3%81%92%E3%82%8B)
        - [RSNP通信を行わずに，動作を確認するデバッグ用プログラムを使用する](#rsnp%E9%80%9A%E4%BF%A1%E3%82%92%E8%A1%8C%E3%82%8F%E3%81%9A%E3%81%AB%E5%8B%95%E4%BD%9C%E3%82%92%E7%A2%BA%E8%AA%8D%E3%81%99%E3%82%8B%E3%83%87%E3%83%90%E3%83%83%E3%82%B0%E7%94%A8%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%99%E3%82%8B)
    - [ユニット通信用サンプルプログラム使用方法](#%E3%83%A6%E3%83%8B%E3%83%83%E3%83%88%E9%80%9A%E4%BF%A1%E7%94%A8%E3%82%B5%E3%83%B3%E3%83%97%E3%83%AB%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95)
        - [ロボット制御用プログラムを立ち上げる](#%E3%83%AD%E3%83%9C%E3%83%83%E3%83%88%E5%88%B6%E5%BE%A1%E7%94%A8%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0%E3%82%92%E7%AB%8B%E3%81%A1%E4%B8%8A%E3%81%92%E3%82%8B)
            - [RTMを使う場合](#rtm%E3%82%92%E4%BD%BF%E3%81%86%E5%A0%B4%E5%90%88)
            - [ROSを使う場合](#ros%E3%82%92%E4%BD%BF%E3%81%86%E5%A0%B4%E5%90%88)
            - [ロボットミドルウェアを使わない場合](#%E3%83%AD%E3%83%9C%E3%83%83%E3%83%88%E3%83%9F%E3%83%89%E3%83%AB%E3%82%A6%E3%82%A7%E3%82%A2%E3%82%92%E4%BD%BF%E3%82%8F%E3%81%AA%E3%81%84%E5%A0%B4%E5%90%88)
    - [操作画面からロボットを操作する](#%E6%93%8D%E4%BD%9C%E7%94%BB%E9%9D%A2%E3%81%8B%E3%82%89%E3%83%AD%E3%83%9C%E3%83%83%E3%83%88%E3%82%92%E6%93%8D%E4%BD%9C%E3%81%99%E3%82%8B)

<!-- /TOC -->

## 1.はじめに  

汎用ユニット(以下，「RSNPユニット」と記載)を，多種多様なロボットやデバイスに外付けで接続することで，取得したデータをRSNP(Robot Serivice Networking Protocol)通信でインターネット経由でサーバにアップロードして蓄積し，Webブラウザ等のGUI上で各ロボットの状態を管理，監視するシステムを開発してきました．今回は，双方向の通信を実現し，以下の図のようにRSNPユニットをロボットやデバイスに接続してインターネット経由で遠隔操作することができます．  

<img src="https://user-images.githubusercontent.com/46204057/104468815-3c321700-55fb-11eb-9f7b-5befc4f6a554.png"  width="60%">

## 2. ユニット使用方法  

**配布したユニット以外のユニットを使用する場合，[こちら](https://github.com/IMS-Lab8073/RSNPUnitRemoteControl/blob/main/docs/RaspiSetup.md)から各種設定を済ませてください．**  

### 2.1 WiFiの設定  
電源投入から接続，WiFiの設定は[こちら](https://ims-lab8073.github.io/RSNPTutorial2020/Setting)に詳細な記載があります．**2.1から2.5まで**を参照ください．  

配布したユニットのホスト名，ユーザ名，パスワードは以下になります．  
| 項目 | 内容 |
|:-:|:-:|
| ホスト名 | rsnpunit |
| ユーザ名 | pi |
| パスワード | 8073 |

以下，Raspberry Piの電源をいれ，Raspberry Pi上のコマンドで操作を行ってください．  
まず，接続するルータ等のSSIDとパスワードを調べます．  
次に，`wpa_supplicant.conf`ファイルをエディタで編集します．  

```shell
$ sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```

※ファイルを編集するためのエディタとして今回は"nano"を使用していますが，好みのものを使用してください．以下，"nano"を使用します．

次のとおりに追記してください．  

~~~text
network={
     ssid="SSIDを記述"
     psk="パスワードを記述"
}
~~~

### 2.2 RSNP接続をする場合
RSNP接続をする場合，以下にしたがって下さい．RSNP接続を行わず，デバッグ用プログラムで動作を確認することもできます．  

#### 2.2.1 コンフィグレーションの設定
RSNPクライアントの実行のコンフィグレーションパラメータを設定しているファイルです．  
以下のコマンドで編集することができます．  

```shell
$ cd ~/RSNPUnitRemoteControl
$ sudo nano Config/Config.properties
```

デフォルトでは以下のようになっています．  
`robot_id`をお伝えした文字列に変更してください．  
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

#### 2.2.2 カメラ用クライアントを立ち上げる

```
$ cd ~/RSNPUnitRemoteControl
```
```
$ java -jar RSNPCameraClient.jar
```


#### 2.2.3 遠隔操作用クライアントを立ち上げる
新しいターミナルを開いてください．
```
$ cd ~/RSNPUnitRemoteControl
```
```
$ java -jar RSNPUnitRemoteControl.jar
```

### 2.3 RSNP通信を行わずに，動作を確認する(デバッグ用プログラムを使用する)  
RSNPユニット内にある，[デバッグ用プログラム](https://github.com/IMS-Lab8073/RSNPUnitRemoteControl/tree/main/debug)で動作を確認することができます．  
イメージは以下になります．  

<img src="https://user-images.githubusercontent.com/46204057/104475528-8d91d480-5602-11eb-8272-3760c6bd45a0.png" width="60%">

| Pub/Sub | ファイル名 |用途 |
|:-:|:-:|:-:|
| Pub | debug_publisher.py | サーバからくる文字列を送信(publish)します． |
| Sub | debug_subscriber.py | サーバへ送る文字列を受け取り(subscribe)，表示します．フォーマットが異なる場合，エラーとなります．  |

publisherとsubscriber，それぞれ，以下のコマンドで実行することができます．  
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


## 3. ユニット通信用サンプルプログラム使用方法
ユニットとロボットとの通信方法を示します．通信方法はMQTTであり，MQTTブローカーおよびトピック名は2.2のコンフィグレーションに示す通りです．通信データ内容は[こちら](https://github.com/IMS-Lab8073/RSNPUnitRemoteControl/blob/main/docs/Specification.md)になります．  
デフォルトは以下になります．    

| 項目 | コンフィグレーション名 | デフォルト値 | 説明 |
|:-:|:-:|:-:|:-:|
| ブローカー | broker | localhost | RSNPユニット内部のブローカーです |
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

#### 3.1.1 RTMを使う場合
本リポジトリにある  
[`RSNPUnitConnector`](https://github.com/IMS-Lab8073/RSNPUnitRemoteControl/tree/main/RSNPUnitConnector_RTCsample)  
を使用することができます．

#### 3.1.2 ROSを使う場合
本リポジトリにある  
[`RSNPUnitConnector`](https://github.com/IMS-Lab8073/RSNPUnitRemoteControl/blob/main/RSNPUnitConnector_ROSNodesample)  
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

## 4. 操作画面からロボットを操作する  
操作画面のURLは以下です．操作方法の詳細については[こちら](https://github.com/IMS-Lab8073/RSNPUnitRemoteControl/blob/main/docs/manual_operation.md)  
  
http://zmini.robo.meo.shibaura-it.ac.jp:8080/RemoteControlSystem/network  

操作画面は以下のようになっていて，
<img src="https://user-images.githubusercontent.com/46204057/105194023-84fa4a80-5b7c-11eb-9120-fb4348ad95c4.png" width="80%">

ロボットの画像を選択すると以下のようにポップアップが表示されます．  
<img src="https://user-images.githubusercontent.com/46204057/105657459-c20d6680-5f07-11eb-82ee-322ca60cc372.png" width="80%">

操作画面に移動後，カメラ配信をオンにするとカメラ画像が，ロボット操作をオンにすると矢印キーまたはA~Eのボタンでの移動が可能になります．  
<img src="https://user-images.githubusercontent.com/46204057/105197045-91cc6d80-5b7f-11eb-8d9c-425035352798.png" width="80%">