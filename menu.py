import RPi.GPIO as GPIO
import clock
import time
from opts import get_device
from luma.core.render import canvas
from luma.core.virtual import viewport
from PIL import ImageFont
from topmenu import Topmenu, tp_height

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down = GPIO.PUD_UP)

item_height = 13

# TODO: radio to a separate module

class Menu():

    def __init__(self, dev, menu, mqtt):
        self.device = dev
        self.menu = menu
        self.current_item = 0
        self.current_view = 'clock'
        self.clock = clock.Clock(self.device)
        self.current_radio = ""
        self.fan = ""
        GPIO.add_event_detect( 20, GPIO.FALLING, callback=self.menu_item_down, bouncetime=300)
        GPIO.add_event_detect( 23, GPIO.FALLING, callback=self.menu_item_up, bouncetime=300)
        GPIO.add_event_detect( 26, GPIO.FALLING, callback=self.execute, bouncetime=300)
        GPIO.add_event_detect( 21, GPIO.FALLING, callback=self.go_home, bouncetime=300)
        GPIO.add_event_detect( 22, GPIO.FALLING, callback=self.go_home, bouncetime=300)
        mqtt.on_message = self.on_mqtt_message

    def on_mqtt_message(self, client, userdate, msg):
        print("message: ", msg.topic+" : "+str(msg.payload))
        # TODO: topic names to constants
        if msg.topic == 'radio':
            self.current_radio = msg.payload
        if msg.topic == 'esp8266/4':
            self.fan = msg.payload

    def menu_item_down(self, pin):
        if self.current_item < len(self.menu) - 1:
            self.current_item += 1

    def menu_item_up(self, pin):
        if self.current_item > 0:
            self.current_item -= 1

    def main_loop(self):
        while True:
            if self.current_view == 'clock':
                # TODO current_radio from a module, not as param
                self.clock.run(self.current_radio, self.fan)
            else:
                self.draw_menu()

    def go_home(self, pin):
        if hasattr(self, 'parent_menu'):
            self.menu = self.parent_menu
            del self.parent_menu
        else:
            self.current_view = 'clock'

    def draw_menu(self):
    	top_menu = Topmenu(self.current_radio, self.fan)
        #virtual = viewport(self.device, width=self.device.width, height=160)
        #with canvas(virtual) as draw:
        with canvas(self.device) as draw:
	    if tp_height > 0:
	    	top_menu.render(draw)	

                
            for idx, item in enumerate(self.menu):
                #if self.current_item >= 3:
                    #idx = idx - 2
                name = item if isinstance(item, str) else item['name']
                inv = True if idx == self.current_item else False
                # TODO: temporary, make `marked` generic !
                marked = name == self.current_radio
                #if self.current_item >= 3:
                    #virtual.set_position((0, (self.current_item-2)*item_height))
                self.menu_item(draw, name, idx, inv, marked)

    def menu_item(self, draw, message, idx, inv=False, marked=False):
        left = 2
        right = self.device.width - 2
        top = (2 + idx * item_height) + tp_height
        bottom = top + item_height + 2 + tp_height

        if inv:
            color = "black"
            bg = "white"
        else:
            color = "white"
            bg = "black"

        draw.rectangle((left, top, right, bottom), fill=bg)
        #pre = "> " if marked else "  "
        #text = pre + message
        draw.text((left + 5, top + 1), text=message, fill=color)

    def execute(self, pin):
        if self.current_view == 'clock':
            self.current_view = 'menu'
        else:
            item = self.menu[self.current_item]
            if 'action' in item:
                item['action']()
            else:
                self.parent_menu = self.menu
                self.menu = item['items']
