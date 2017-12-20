tp_height = 14
class Topmenu:

    def __init__(self, current_radio, fan):
        self.current_radio = current_radio
        self.fan = fan

    def render(self, draw):
        # TODO: 128 to dynamic value - device.width
        radio = "R" if self.current_radio != "stop" else ""
        fan = "W" if self.fan == "1" else ""
        draw.text((120, 1), radio, fill="white")
        draw.text((100, 1), fan, fill="white")
        draw.line((0, tp_height, 128, tp_height), fill="white")
        
