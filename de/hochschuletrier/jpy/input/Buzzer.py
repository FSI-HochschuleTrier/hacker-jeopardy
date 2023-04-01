from dataclasses import dataclass

@dataclass
class Buzzer:
	player    : int
	buzzerPin : int
	ledPin    : int

	def addCallback(self, pressedBuzzer, GPIO):
		GPIO.add_event_callback(
			self.buzzerPin,
			lambda _: pressedBuzzer(trigger=self, GPIO = GPIO)
		)

Buzzers = [
	Buzzer(1, 4, 23),
	Buzzer(2, 27, 22),
	Buzzer(3, 21, 12),
	Buzzer(4, 13, 20)
]

def ResetBuzzerLEDs(GPIO):
	print("RESET")
	for buzzer in Buzzers:
		GPIO.output(buzzer.ledPin, GPIO.LOW)

