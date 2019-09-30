# -*- coding: utf-8 -*-

import wda
import random
from time import sleep

class Point:
    x = 0
    y = 0
    def __init__(self,x,y):
        self.x = x
        self.y = y

c = wda.Client()
s = c.session()

def getS():
    fs = [Point(x=470,y=920), Point(x=565,y=900),Point(x=640,y=850)]
    ts = [Point(x=400,y=600), Point(x=400,y=470),Point(x=250,y=700),Point(x=380,y=300)]

    for f in fs:
        for t in ts:
            i = 2
            while (i > 0):
                i = i - 1
                s.swipe(x1=f.x,x2=t.x,y1=f.y,y2=t.y,duration=0.5)




def item(x):
    y1 = random.uniform(0,300)
    y2 = random.uniform(s.window_size().height - 500, s.window_size().height)
    duration = random.uniform(0.3,1)
    s.swipe(x1=int(x),y1=int(y1),x2=int(x),y2=int(y2),duration=duration)
    sleep(random.uniform(0.3,2))

if __name__ == '__main__':
    while(True):
        try:
            item(random.uniform(230,330))
            item(random.uniform(380,470))
            item(random.uniform(530,610))
            getS()
        except:
            sleep(0.5)
            continue
