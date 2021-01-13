import paho.mqtt.publish as publish
import json
import time
import sys

while True:
    send_data = {"robotID":"controller","vx":"0","va":"0","option":"","timestamp":"2021/01/07 12:00:00.000"}
    send_data_zero = json.dumps(send_data)
    print("Please input number")
    print("1 : Forward")
    print("2 : Go Back")
    print("3 : Right Turn")
    print("4 : Left Turn")
    print("5 : Option A")
    print("6 : Option B")
    print("7 : Option C")
    print("8 : Option D")
    print("q : Exit")

    input_data = input(">")

    if input_data=="1":
        send_data["vx"] = "500"
    elif input_data=="2":
        send_data["vx"] = "-500"
    elif input_data=="3":
        send_data["va"] = "500"
    elif input_data=="4":
        send_data["va"] = "-500"
    elif input_data=="5":
        send_data["option"] = "A"
    elif input_data=="6":
        send_data["option"] = "B"
    elif input_data=="7":
        send_data["option"] = "C"
    elif input_data=="8":
        send_data["option"] = "D"
    elif input_data=="q":
        sys.exit()

    send_data_json = json.dumps(send_data)
    
    for _ in range(5):
        print("Publish data : " + str(send_data_json))
        publish.single("fromServer/Velocity", send_data_json, hostname="localhost")
        time.sleep(0.5)

    publish.single("fromServer/Velocity", send_data_zero, hostname="localhost")
    
    print("publish done")
    print()