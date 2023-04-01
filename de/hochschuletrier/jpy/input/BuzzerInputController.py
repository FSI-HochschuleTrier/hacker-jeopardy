__author__ = 'miko'

from de.hochschuletrier.jpy.console.JPYLogger import JPYLogger
from de.hochschuletrier.jpy.input.InputController import InputController
from de.hochschuletrier.jpy.input.Buzzer import Buzzers

class BuzzerInputController(InputController):
	def __init__(self, root):
		super().__init__(root)
		if not (root.debug):
			import RPi.GPIO as GPIO

		self.root = root
		self.logger = JPYLogger(self)
		self.logger.log("BuzzerInputController initialisiert")
		self.blockBuzzer = False

		if (root.debug):
			return
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)

		for buzzer in Buzzers:
			GPIO.setup(buzzer.buzzerPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
			GPIO.setup(buzzer.ledPin, GPIO.OUT)

			GPIO.add_event_detect(buzzer.buzzerPin, GPIO.RISING)
			GPIO.output(buzzer.ledPin, GPIO.LOW)
			buzzer.addCallback(self.pressedBuzzer, GPIO)

	def pressedBuzzer(self, trigger, GPIO):
		shouldProceed = super().pressedBuzzer(trigger.player - 1)
		if not shouldProceed:
			return
		GPIO.output(trigger.ledPin, GPIO.HIGH)	
