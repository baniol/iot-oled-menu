import time
import os
import datetime
from luma.core.render import canvas
from PIL import ImageFont
from topmenu import Topmenu, tp_height

# TODO: to helpers file
def make_font(name, size):
    font_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), 'fonts', name))
    return ImageFont.truetype(font_path, size)

class Clock:

    def __init__(self, device):
        self.device = device
        self.today_last_time = "Unknown"
    
    def render(self):
        now = datetime.datetime.now()
        today_date = now.strftime("%d %b %y")
        today_time = now.strftime("%H:%M:%S")
    	top_menu = Topmenu(self.current_radio, self.fan)
        if today_time != self.today_last_time:
            self.today_last_time = today_time
            with canvas(self.device) as draw:
	        if tp_height > 0:
	    	    top_menu.render(draw)	
                now = datetime.datetime.now()
                today_date = now.strftime("%d %b %y")

                font = make_font("code2000.ttf", 30)
                draw.text((5, 5 + tp_height), today_date, fill="yellow")
                draw.text((5, 15 + tp_height), today_time, font=font, fill="yellow")

    # TODO: current_radio from module, not as param
    def run(self, current_radio, fan):
        self.current_radio = current_radio
        self.fan = fan
        self.render()
        time.sleep(0.01)

