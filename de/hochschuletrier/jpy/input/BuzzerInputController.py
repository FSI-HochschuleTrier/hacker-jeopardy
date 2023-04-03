__author__ = 'miko'

from de.hochschuletrier.jpy.console.JPYLogger import JPYLogger
from de.hochschuletrier.jpy.input.InputController import InputController
from de.hochschuletrier.jpy.input.Buzzer import Buzzers
from de.hochschuletrier.jpy.input.Button import Button
from de.hochschuletrier.jpy.Util import debounce
from dataclasses import dataclass

@dataclass
class PushButton:
	pin    : int
	button : Button

	def registerCallback(self, GPIO):
		GPIO.add_event_callback(self.pin, lambda _: self.press())

	@debounce(0.3)
	def press(self):
		print("BUTTON:", self.button)

class BuzzerInputController(InputController):
	Buttons = [
		PushButton(5,  Button.BLACK),
		PushButton(24, Button.RED),
		PushButton(25, Button.GREEN)
	]

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

		for button in BuzzerInputController.Buttons:
			GPIO.setup(button.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
			GPIO.add_event_detect(button.pin, GPIO.RISING)
			button.registerCallback(GPIO)

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
