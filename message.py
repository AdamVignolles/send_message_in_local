import paho.mqtt.client as mqtt #import the client1
import time
############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
broker_address="192.168.1.91"
#broker_address="iot.eclipse.org"
print("creating new instance")
client = mqtt.Client("P1") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address, 5050) #connect to broker
client.loop_start() #start the loop
while True:
    print("Subscribing to topic","message")
    client.subscribe("message")
    print("Publishing message to topic","message")
    entre = input()
    client.publish("message",entre)
    time.sleep(4) # wait