#!/usr/bin/env python

import menu
from opts import get_device

def test(val):
    print("executing ", val)

wentylator = {
    'name': 'wentylator',
    'items': [
        {
            'name': 'on',
            'action': lambda: test('on')
        },
        {
            'name': 'off',
            'action': lambda: test('off')
        }
    ]
}
radio = {
    'name': 'radio',
    'items': [
        {
            'name': 'RFM',
            'action': lambda: test('RMF')
        },
        {
            'name': 'Melo',
            'action': lambda: test('Melo')
        }
    ]
}

menu_def = [radio, wentylator]

if __name__ == "__main__":
    try:
        #global device
        device = get_device()
        m = menu.Menu(device, menu_def)
        m.loop()
    except KeyboardInterrupt:
        pass
