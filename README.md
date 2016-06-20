hacker-jeopardy
===============
![](/resources/opener.png)

a jeopardy software written in python, designed for the RaspberryPI

### Questions
questionsets take place in the `questions` folder, for image/sound-sources and the questions theirselves
in a json-file.

### Development
start with the `debug` parameter.

### Dependencies
* python2
* python-tk
* python-imaging
* RPIO
* mplayer.py

### Controls
#### Keyboard
|Key                         |Action                                        |
|:---------------------------|----------------------------------------------|
|<kbd>9</kbd>                |Start Game                                    |
|<kbd>1</kbd> (Num)          |Show Start Screen                             |
|<kbd>0</kbd> (Num)          |Show Play Screen                              |
|<kbd>5</kbd> (Num)          |Start/Stop Intro Music (on Start Screen only) |
|<kbd>1</kbd> - <kbd>6</kbd> |Buzzer Player 1 - 6                           |
|<kbd>+</kbd> (Num)          |Question correct/Play Audio again             |
|<kbd>-</kbd> (Num)          |Question incorrect/No Answer                  |
|<kbd>Enter</kbd>            |Confirm Input                                 |

#### Mouse
The mouse is used for selecting the category and for OK clicking.

#### Board
The red button equals the question-incorrect button, the green button the question-correct button.
*(not implemented yet)*

### Remote PC
You have to open two shells to the pi:

```bash
ssh pi@jeopardy.local
ssh -X pi@jeopardy.local 'x2x -east -to :0'
```

one is for starting the game, the other pipes the keyboard/mouse input to the pi