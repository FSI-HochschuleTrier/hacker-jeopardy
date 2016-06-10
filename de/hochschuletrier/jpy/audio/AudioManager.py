from mplayer import Player, CmdPrefix

class AudioManager:
	def __init__(self, root):
		self.root = root
		# Set default prefix for all Player instances
		Player.cmd_prefix = CmdPrefix.PAUSING_KEEP
		self.backgroundsong = 'resources/Jeopardy.ogg'
		self.player = {}
		self.player[self.backgroundsong] = Player()

	def playFile(self, url):
		self.player[url] = Player(url)

	def playBackgroundSong(self):
		self.playFile(self.backgroundsong)

	def resumeBackgroundSong(self):
		self.pause(self.backgroundsong)

	def pause(self, url):
		self.player[url].pause()

	def stop(self, url):
		self.player[url] = Player()

	def playingBackground(self):
		return (not self.player[self.backgroundsong].paused) and self.player[self.backgroundsong].filename == 'Jeopardy.ogg'
