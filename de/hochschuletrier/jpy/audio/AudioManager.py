from mplayer import Player, CmdPrefix

class AudioManager:
    def __init__(self, root):
        self.root = root
        # Set default prefix for all Player instances
        Player.cmd_prefix = CmdPrefix.PAUSING_KEEP
        self.player = Player()


    def playFile(self, url):
        self.player.loadfile(url)
        #self.player.pause()

    def playBackgroundSong(self):
        self.playFile('resources/Jeopardy.ogg')

    def resumeBackgroundSong(self):
        if self.player.filename != 'Jeopardy.ogg':
            self.playFile('resources/Jeopardy.ogg')
        else:
            self.player.pause()

    def pause(self):
        self.player.pause()

    def stop(self):
        self.player = Player()

    def playingBackground(self):
        return (not self.player.paused) and self.player.filename == 'Jeopardy.ogg'
