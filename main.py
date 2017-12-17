#!/usr/bin/env python

import menu
from opts import get_device
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

client= mqtt.Client("rpi_zero_1")
client.on_connect = on_connect
client.username_pw_set("baniol", password="szapo321")
client.connect("192.168.1.45")
client.loop_start()

def test(val):
    print("executing ", val)

def sendMessage(topic, val):
	print("sending ", topic, val)
	client.publish(topic, payload=val)

wentylator = {
    'name': 'wentylator',
    'items': [
        {
            'name': 'on',
            'action': lambda: sendMessage('fan', 1)
        },
        {
            'name': 'off',
            'action': lambda: sendMessage('fan', 0)
        }
    ]
}
radio = {
    'name': 'radio',
    'items': [
        {
            'name': 'RFM',
            'action': lambda: test('RMF')
        },
        {
            'name': 'Melo',
            'action': lambda: test('Melo')
        }
    ]
}

menu_def = [radio, wentylator]

if __name__ == "__main__":
    try:
        #global device
        device = get_device()
        m = menu.Menu(device, menu_def)
        m.loop()
    except KeyboardInterrupt:
        pass
