tp_height = 14
class Topmenu:

    def __init__(self, current_radio):
        self.current_radio = current_radio

    def render(self, draw):
        # TODO: 128 to dynamic value - device.width
        radio = "R" if self.current_radio != "stop" else ""
        draw.text((120, 1), radio, fill="white")
        draw.line((0, tp_height, 128, tp_height), fill="white")
        
