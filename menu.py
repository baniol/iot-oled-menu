import RPi.GPIO as GPIO
import clock
import time
from opts import get_device
from luma.core.render import canvas
from PIL import ImageFont
from topmenu import Topmenu

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down = GPIO.PUD_UP)

item_height = 13
top_menu_height = 0

class Menu():

    def __init__(self, dev, menu):
        self.device = dev
        self.menu = menu
        self.current_item = 0
        self.current_view = 'clock'
        self.clock = clock.Clock(self.device)
        GPIO.add_event_detect( 20, GPIO.FALLING, callback=self.menu_item_down, bouncetime=300)
        GPIO.add_event_detect( 23, GPIO.FALLING, callback=self.menu_item_up, bouncetime=300)
        GPIO.add_event_detect( 26, GPIO.FALLING, callback=self.execute, bouncetime=300)
        GPIO.add_event_detect( 21, GPIO.FALLING, callback=self.go_home, bouncetime=300)
        GPIO.add_event_detect( 22, GPIO.FALLING, callback=self.go_home, bouncetime=300)

    def menu_item_down(self, pin):
        if self.current_item < len(self.menu) - 1:
            self.current_item += 1

    def menu_item_up(self, pin):
        if self.current_item > 0:
            self.current_item -= 1

    def main_loop(self):
        while True:
            if self.current_view == 'clock':
                self.clock.run()
            else:
                self.draw_menu()

    def go_home(self, pin):
        if hasattr(self, 'parent_menu'):
            self.menu = self.parent_menu
            del self.parent_menu
        else:
            self.current_view = 'clock'

    def draw_menu(self):
    	top_menu = Topmenu()
        with canvas(self.device) as draw:
	    if top_menu_height > 0:
	    	top_menu.render(draw)	
            for idx, item in enumerate(self.menu):
                name = item if isinstance(item, str) else item['name']
                inv = True if idx == self.current_item else False
                self.menu_item(draw, name, idx, inv)

    def menu_item(self, draw, message, idx, inv=False):
        left = 2
        right = self.device.width - 2
        top = (2 + idx * item_height) + top_menu_height
        bottom = top + item_height + 2 + top_menu_height

        if inv:
            color = "black"
            bg = "white"
        else:
            color = "white"
            bg = "black"

        draw.rectangle((left, top, right, bottom), fill=bg)
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
