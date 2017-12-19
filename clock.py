"""
An analog clockface with date & time.

Ported from:
https://gist.github.com/TheRayTracer/dd12c498e3ecb9b8b47f#file-clock-py
"""

import time
import os
import datetime
from luma.core.render import canvas
from PIL import ImageFont

def make_font(name, size):
    font_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), 'fonts', name))
    return ImageFont.truetype(font_path, size)

def posn(angle, arm_length):
    dx = int(math.cos(math.radians(angle)) * arm_length)
    dy = int(math.sin(math.radians(angle)) * arm_length)
    return (dx, dy)

class Clock:

    def __init__(self, device):
        self.device = device
        self.today_last_time = "Unknown"
    
    def render(self):
        now = datetime.datetime.now()
        today_date = now.strftime("%d %b %y")
        today_time = now.strftime("%H:%M:%S")
        if today_time != self.today_last_time:
            self.today_last_time = today_time
            with canvas(self.device) as draw:
                now = datetime.datetime.now()
                today_date = now.strftime("%d %b %y")

                font = make_font("code2000.ttf", 30)
                draw.text((5, 5), today_date, fill="yellow")
                draw.text((5, 15), today_time, font=font, fill="yellow")

    def run(self):
        #while self.running:
        self.render()
        time.sleep(0.01)

    def stop(self):
        self.running = False
        #self.device.clear()

    def is_running(self):
        return self.running


