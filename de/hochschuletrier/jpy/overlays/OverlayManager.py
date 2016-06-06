__author__ = 'miko'
from de.hochschuletrier.jpy.overlays.QuestionOverlay import QuestionOverlay
from de.hochschuletrier.jpy.overlays.UsernameOverlay import UsernameOverlay


class OverlayManager:
	def __init__(self, root):
		self.root = root
		self.activeOverlay = 0
		self.overlays = []

		self.generateOverlays()

	def generateOverlays(self):
		self.overlays.append(QuestionOverlay(self.root, overlayName="Frage", id=0))
		self.overlays.append(UsernameOverlay(self.root, overlayName="Username", id=1))

		for overlay in self.overlays:
			overlay.lower()

	def showOverlay(self, overlay):
		if overlay > len(self.overlays) - 1:
			return
		self.overlays[self.activeOverlay].lower()
		self.overlays[overlay].lift(aboveThis=None)
		self.overlays[overlay].isVisible = True
		self.activeOverlay = overlay
