import pyglet

class AudioManager:
	def __init__(self, root):
		self.root   = root
		self.songs  = {
			"question"   : None,
			"background" : pyglet.media.load("resources/Jeopardy.ogg")
		}
		self.player     = pyglet.media.Player()
		self.background = pyglet.media.Player()
		self.buzzer     = pyglet.media.load("resources/buzzer.ogg", streaming=False)

		self.background.queue(self.songs["background"])

	def playFile(self, url):
		if not url in self.songs:
			self.songs[url] = pyglet.media.load(url)
		self.player.queue(self.songs[url])
		if self.player.playing:
			self.player.next_source()
		else:
			self.player.play()

	def stop(self, _):
		wasPlaying = self.player.playing
		self.player.pause()
		self.player.seek(0)

		if wasPlaying:
			self.player.next_source()

	def pause(self, _):
		self.player.pause() 

	def playBuzzer(self):
		self.buzzer.play()

	def playBackgroundSong(self):
		self.background.play()

	def pauseBackgroundSong(self):
		self.background.pause();

	def stopBackgroundSong(self):
		self.background.pause()
		self.background.seek(0)

	def playQuestion(self, url):
		self.songs["question"] = pyglet.media.load(url)
		self.playFile("question")

	def stopQuestion(self):
		self.stop(None)
	

	def playingBackground(self):
		return self.player.playing and self.player.source == self.songs["background"]