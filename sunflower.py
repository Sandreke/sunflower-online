from turtle import *
from math import *

speed(0)
bgcolor("black")
goto(0,-40)

for i in range(16):
    for j in range(18):
        color('#FFA216'), rt(90)
        circle(150-j*6,90), lt(90)
        circle(150-j*6,90), rt(180)
    circle(40,24)

done()