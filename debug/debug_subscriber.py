import paho.mqtt.subscribe as subscribe
import json

def print_msg(client, userdata, message):
    try:
        recieve_data_dict = json.loads(message.payload)
        print(recieve_data_dict)
        print("data type : " + str(recieve_data_dict["data_type"]))
        print("data : " + str(recieve_data_dict["data"]))
        print()
    except Exception as e:
        print(e)

while True:
    subscribe.callback(print_msg, "toUnit/RobotData", hostname="localhost")