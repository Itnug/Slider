# Slider
 15 squares dragged on a 4x4 board

Currently this project is only a REPL and is available on a terminal of your choice.
As 2.7 support has been discontinued, all the code has been ported to 3.8.
Backward compatibility is lost with 2.7, but all 3.x versions of python will still run.

Assuming python 3.x is available on your machine, just run `python slider.py` to get going

Instructions:
wasd (lowercase) instructions can be chained and executed per iteration
```
eg:
 7 10  4 13
 2    15 12  
14 11  6  3
 1  5  8  9

next move?a 
 7 10  4 13
 2 15    12   <- dragged 15 left
14 11  6  3
 1  5  8  9

next move?d
 7 10  4 13
 2    15 12   <- dragged 15 right
14 11  6  3
 1  5  8  9

next move?wd
 7 10  4 13
 2 11 15 12   <--11 up (1. w)
   14  6  3   <--14 right (2. d)
 1  5  8  9

next move?
```
