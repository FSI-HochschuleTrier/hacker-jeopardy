hacker-jeopardy
===============
![](/resources/opener.png)

a jeopardy software written in python, designed for the RaspberryPI

### Questions
questionsets take place in the `questionas` folder, for image/sound-sources and the questions theirselves
in a json-file.

### Development
start with the `debug` parameter.

### Dependencies
* python2
* python-tk
* python-imaging
* RPIO
* mplayer.py

### Remote PC
You have to open two shells to the pi:

```bash
ssh pi@jeopardy.local
ssh -X pi@jeopardy.local 'x2x -east -to :0'
```

one is for starting the game, the other pipes the keyboard/mouse input to the pi