#!/usr/bin/env python

from  menu import Menu
from menu_definitions import MenuDefinitions
from opts import get_device
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # TODO: check qos
    client.subscribe("radio", 2)
    client.subscribe("esp8266/4", 2)

# TODO: to config
client = mqtt.Client("rpi_zero_1", clean_session=False)
client.on_connect = on_connect
client.username_pw_set("baniol", password="szapo321")

if __name__ == "__main__":
    try:
        device = get_device()
        md = MenuDefinitions(client)
        m = Menu(device, md.define_menu(), client)
        client.connect("192.168.1.45")
        client.loop_start()
        m.main_loop()
    except KeyboardInterrupt:
        pass
