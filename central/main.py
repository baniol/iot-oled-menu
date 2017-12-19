#!/usr/bin/env python

from subprocess import Popen
import paho.mqtt.client as mqtt

mPID = 0

stations = {
    'RMF Classic': 'http://31.192.216.5:8000/rmf_classic',
    'Trojka': 'http://stream3.polskieradio.pl:8904',
    'RMF': 'http://195.150.20.7:8000/rmf_fm'
}

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe("radio")

def playStation(name):
        stopRadio()
	print('Playing ', stations[name])
        global mPID
        mPID = Popen(["mplayer", stations[name]]).pid
        print(mPID)

def stopRadio():
    global mPID
    if mPID != 0:
        print("killing ", mPID)
        Popen(["kill", str(mPID)])
        mPID = 0

def on_message(client, userdata, msg):
    	#print(msg.topic+" "+str(msg.payload))
        if msg.payload == 'stop':
            stopRadio()
        else:
	    playStation(msg.payload)

client= mqtt.Client("rpi_b_central")
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("baniol", password="szapo321")
client.connect("localhost")
client.loop_forever()

