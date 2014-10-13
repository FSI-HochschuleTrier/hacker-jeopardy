__author__ = 'miko'
from de.hochschuletrier.jpy.states.GameState import GameState
from de.hochschuletrier.jpy.ui.TableProcessor import TableProcessor
from de.hochschuletrier.jpy.overlays.OverlayManager import OverlayManager

class PlayGameState(GameState):
    def __init__(self, *args, **kwargs):
        GameState.__init__(self, *args, **kwargs)
        TableProcessor(self, self.root, "questions.json")
        self.overlayManager = OverlayManager(self)