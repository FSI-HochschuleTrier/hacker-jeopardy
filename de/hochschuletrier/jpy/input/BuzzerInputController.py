__author__ = 'miko'
import sys
from de.hochschuletrier.jpy.console.JPYLogger import JPYLogger
from de.hochschuletrier.jpy.input.InputController import InputController
import RPIO


class BuzzerInputController(InputController):
    def __init__(self, root):
        self.root = root
        self.logger = JPYLogger(self)
        self.logger.log("BuzzerInputController initialisiert")
        self.blockBuzzer = False
        mainWindow = root.mainWindow

        RPIO.add_interrupt_callback(18, self.pressedBuzzer(event=None, trigger=0), edge='rising',
                                    pull_up_down=RPIO.PUD_UP)
        RPIO.wait_for_interrupts(threaded=True)