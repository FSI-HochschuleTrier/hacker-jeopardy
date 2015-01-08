from mplayer import Player, CmdPrefix


class AudioManager:
    def __init__(self, root):
        self.root = root
        # Set default prefix for all Player instances
        Player.cmd_prefix = CmdPrefix.PAUSING_KEEP
        self.player = Player()


    def playFile(self, url):
        self.player.loadfile(url)
        self.player.pause()

    def playBackgroundSong(self):
        self.player.loadfile('resources/Jeopardy.ogg')
        #self.player.pause()

    def resumeBackgroundSong(self):
        if self.player.filename != 'Jeopardy.ogg':
            self.player.loadfile('resources/Jeopardy.ogg')
        #self.player.pause()

    def pause(self):
        self.player.pause()

    def stop(self):
        self.player = Player()