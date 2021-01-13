import MQTTClient
import time
import json

mqttc = MQTTClient.MyMQTTClass()
# start subscribe
rc = mqttc.run("localhost","fromServer/Velocity")

i=0
while True:
    # send data format (dictionary)
    i+=1
    send_data = {"data_type":"count", "data":i}
    send_data_json = json.dumps(send_data)
    print("publish data : " + str(send_data_json))
    
    # publish data
    mqttc.publish_message("localhost", "toUnit/Robotdata", send_data_json)
    
    # subscribe data (if isNew() is True)
    # data format : {"robotID":"", "vx":"", "va":"", "option":"", "timestamp":""}
    if mqttc.isNew(): 
        print(mqttc.recieve_data)
        recieve_data      = mqttc.recieve_data
        recieve_data_dict = json.loads(recieve_data)
        
        vx = recieve_data_dict["vx"]
        va = recieve_data_dict["va"]
        option = recieve_data_dict["option"]

        print("recieve data : ")
        print("vx : "+str(vx)+", va : "+str(va)+", option : "+option)
    time.sleep(0.5)