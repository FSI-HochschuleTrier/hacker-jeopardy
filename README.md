hacker-jeopardy
===============
![](/resources/opener.gif)

a jeopardy software written in python, designed for the RaspberryPI

### Development
start with the `debug` parameter.

### Remote PC
You have to open two shells to the pi:

```bash
ssh pi@jeopardy.local
ssh -X pi@jeopardy.local 'x2x -east -to :0'
```