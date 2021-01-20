## 必要ソフトのインストール

### GitHubからソフトをダウンロード
任意のディレクトリで，本リポジトリをダウンロードしてください．  
本マニュアルは，ホームディレクトリにダウンロードした状態で進めます．  

```shell
$ cd ~/
$ git clone https://github.com/IMS-Lab8073/RSNPUnitRemoteControl
```

### libjpeg8のインストール
カメラクライアントを立ち上げるため，以下のコマンドを実行してください．  
```shell
$ sudo apt-get install libjpeg8
```

### mosquittoのインストール
MQTTのブローカーをインストールします．  

```shell
# Mosquitto(Broker)をインストール
$ sudo apt-get install mosquitto

# Mosquittoクライアントをインストール
$ sudo apt-get install mosquitto-clients
```

### Python
ライブラリpahoのインストール

```shell
$ pip3 install paho-mqtt
```

### broker(mosquitto)の起動
ブローカーの開始と確認、停止

```shell
$ sudo systemctl start mosquitto
$ sudo systemctl status mosquitto
$ sudo systemctl stop mosquitto
```

### (任意) ホスト名の変更
**この項目は任意です．**
本リポジトリのサンプルプログラムはホスト名が`rsnpunit`である前提のものが多いです．  
ホスト名を変更するには以下の2つのファイルを編集してください．  
```shell
$ sudo nano /etc/hostname
$ sudo nano /etc/hosts
```
該当する箇所を変更してください．  
変更前(デフォルト)　　
```text
raspberrypi
```

変更後　　
```text
rsnpunit
```