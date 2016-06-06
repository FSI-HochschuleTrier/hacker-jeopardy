__author__ = 'miko'
from de.hochschuletrier.jpy.states.GameState import GameState
from de.hochschuletrier.jpy.ui.TableProcessor import TableProcessor
from de.hochschuletrier.jpy.overlays.OverlayManager import OverlayManager
from de.hochschuletrier.jpy.overlays.DoubleOverlay import DoubleOverlay


class PlayGameState(GameState):
	def __init__(self, *args, **kwargs):
		GameState.__init__(self, *args, **kwargs)
		TableProcessor(self, self.root)
		self.overlayManager = OverlayManager(self)
		self.double = DoubleOverlay(self, overlayName="Double", id=2)
		self.double.lower()
