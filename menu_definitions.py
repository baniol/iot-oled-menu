class MenuDefinitions:

    def __init__(self, client):
        self.client = client

    def send_message(self, topic, val):
	print("sending ", topic, val)
	# TODO: check qos
	self.client.publish(topic, payload=val, qos=2, retain=True)

    def define_menu(self):
        wentylator = {
            'name': 'wentylator',
            'items': [
                {
                    'name': 'on',
                    'action': lambda: self.send_message('fan', 1)
                },
                {
                    'name': 'off',
                    'action': lambda: self.send_message('fan', 0)
                }
            ]
        }
        radio = {
            'name': 'radio',
            'items': [
                {
                    'name': 'Stop radio',
                    'action': lambda: self.send_message('radio', 'stop')
                },
                {
                    'name': 'Chilli Zet',
                    'action': lambda: self.send_message('radio', 'Chilli Zet')
                },
                {
                    'name': 'France Inter',
                    'action': lambda: self.send_message('radio', 'France Inter')
                },
                {
                    'name': 'Trojka',
                    'action': lambda: self.send_message('radio', 'Trojka')
                },
                {
                    'name': 'RMF Classic',
                    'action': lambda: self.send_message('radio', 'RMF Classic')
                },
                {
                    'name': 'RMF',
                    'action': lambda: self.send_message('radio', 'RMF')
                }
            ]
        }
        return [radio, wentylator]

