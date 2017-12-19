#!/usr/bin/env python

from subprocess import Popen
import paho.mqtt.client as mqtt

mPID = 0

stations = {
    'RMF Classic': 'http://31.192.216.5:8000/rmf_classic',
    'Trojka': 'http://stream3.polskieradio.pl:8904',
    'Chilli Zet': 'http://chi-kat-02.cdn.eurozet.pl:8902/'
}

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe("radio")

def playStation(name):
	print('Playing ', stations[name])
        #command = "mplayer %s" (name)
        #command = "mplayer " + stations[name]
        #os.system(command)
        mPID = Popen(["mplayer", stations[name]]).pid
        print(mPID)

def stopRadio():
    Popen("kill", mPID)

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

