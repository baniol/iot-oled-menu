# IOT OLED Menu

```python main.py -i spi -d sh1106```

## Links

* https://luma-core.readthedocs.io/en/latest/api-documentation.html#module-luma.core.virtual - luma core docs

## Prerequisites

* install ntp (optional)
* configure local time `sudo dpkg-reconfigure tzdata`
* for RPI headless sound problem (no soundcard) - 
* http://blog.scphillips.com/posts/2013/01/sound-configuration-on-raspberry-pi-with-alsa/ - cli sound management

## Run as process

managing systemd
https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units

run as service
https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/

## MQTT

* http://www.steves-internet-guide.com/loop-python-mqtt-client/
* http://www.steves-internet-guide.com/mqtt-retained-messages-example/
* http://www.steves-internet-guide.com/mqtt-python-callbacks/
* http://www.steves-internet-guide.com/subscribing-topics-mqtt-client/
* https://www.hivemq.com/blog/mqtt-essentials-part-5-mqtt-topics-best-practices
* https://github.com/eclipse/paho.mqtt.python

## TBC

* https://www.raspberrypi.org/forums/viewtopic.php?f=32&t=34485 - class for menu
* https://www.youtube.com/watch?v=ak5TsUFhyf8 - similar cpp menu

## Keypad Matrix

* https://raspberrypi.stackexchange.com/questions/53665/how-to-use-a-4x4-keypad-in-python

