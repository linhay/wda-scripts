# -*- coding: utf-8 -*-

import wda
import random
from time import sleep


c = wda.Client()
s = c.session()


def item(x):
    y1 = random.uniform(0,300)
    y2 = random.uniform(s.window_size().height - 500, s.window_size().height)
    duration = random.uniform(0.3,2)
    s.swipe(x1=int(x),y1=int(y1),x2=int(x),y2=int(y2),duration=duration)
    sleep(random.uniform(0.3,2))

if __name__ == '__main__':
    while(True):
        try:
            item(random.uniform(230,330))
            item(random.uniform(380,470))
            item(random.uniform(530,610))
        except:
            sleep(0.5)
            continue
