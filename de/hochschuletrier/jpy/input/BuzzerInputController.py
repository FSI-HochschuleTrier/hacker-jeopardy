__author__ = 'miko'

from de.hochschuletrier.jpy.console.JPYLogger import JPYLogger
from de.hochschuletrier.jpy.input.InputController import InputController

class BuzzerInputController(InputController):
	def __init__(self, root):
		if not (root.debug):
			import RPi.GPIO as GPIO

		self.root = root
		self.logger = JPYLogger(self)
		self.logger.log("BuzzerInputController initialisiert")
		self.blockBuzzer = False

		if (root.debug):
			return
		GPIO.setmode(GPIO.BOARD)

		for channel in [25, 8, 7]:
			GPIO.setup(channel, GPIO.IN, initial=GPIO.HIGH)
			GPIO.add_event_detect(channel, GPIO.RISING)

		GPIO.add_event_callback(25, lambda: self.pressedBuzzer(trigger=0))
		GPIO.add_event_callback(8, lambda: self.pressedBuzzer(trigger=1))
		GPIO.add_event_callback(7, lambda: self.pressedBuzzer(trigger=2))