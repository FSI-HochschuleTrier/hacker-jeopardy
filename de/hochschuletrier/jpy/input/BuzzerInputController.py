__author__ = 'miko'
import sys
from de.hochschuletrier.jpy.console.JPYLogger import JPYLogger
from de.hochschuletrier.jpy.input.InputController import InputController
import RPIO
from thread import start_new_thread


class BuzzerInputController(InputController):
    def __init__(self, root):
        self.root = root
        self.logger = JPYLogger(self)
        self.logger.log("BuzzerInputController initialisiert")
        self.blockBuzzer = False
        mainWindow = root.mainWindow
        RPIO.add_interrupt_callback(18, lambda x, y: self.pressedBuzzer(trigger=0), edge='rising',
                                    pull_up_down=RPIO.PUD_UP, threaded_callback=True)
        start_new_thread(self.blocking_wait_for_interrupts, (self,))

    def blocking_wait_for_interrupts(self):
        while (True):
            print 'waiting for interrupts'
            RPIO.wait_for_interrupts(threaded=False)
