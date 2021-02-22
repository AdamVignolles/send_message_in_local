import paho.mqtt.client as mqtt
import time

all_chanel = [
    'message',
    'famille'
]

def on_message(client, userdata, message):
    print("\nmessage received " ,str(message.payload.decode("utf-8")), "\n")

broker_address="192.168.1.91"

print("creating new instance")
name = input("entre votre nom : ")
client = mqtt.Client(name)

print("connecting to broker")
client.on_message=on_message

client.connect(broker_address, 5050)

client.loop_start()
run = True
while run:
    suite = input("1 pour envoier un message \n2 pour quitter \n-> ")
    if suite == '1':

        print("choissier le chanel sur lequel vous vouler discuter")
        chanel = input(f"{all_chanel[0]} \n{all_chanel[1]} \n->")
        client.subscribe(chanel)

        print("Publishing message to topic",chanel)
        entre = input("entre votre message : ")
        client.publish(chanel,entre)

        time.sleep(4)
        client.on_message=on_message
    elif suite == '2':
        client.disconnect()
        client.loop_stop()
        run = False