# -*- coding: utf-8 -*-

import wda
import logging
import os
import random
from time import sleep
import time
# 日志输出
logging.basicConfig(format='[%(asctime)s][%(name)s:%(levelname)s(%(lineno)d)][%(module)s:%(funcName)s]:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S',
                    level=logging.INFO)
logging.getLogger("requests").setLevel(logging.WARNING)

# 屏幕分辨率
device_x, device_y = 1920, 1080

# 小号 60左右 da 30
FIGHT_TIME = 30

# 刷金币次数
repeat_times = 60

c = wda.Client()
s = c.session()


def item(y):
    x1 = random.uniform(0,200)
    x2 = random.uniform(s.window_size().width - 300,s.window_size().width)
    duration = random.uniform(0.3,2)
    s.swipe(x1=int(x1),y1=int(y),x2=int(x2),y2=int(y),duration=duration)

if __name__ == '__main__':
    while(True):
        try:
            item(random.uniform(710,750))
            sleep(random.uniform(0.3,1))
            item(random.uniform(650,700))
            sleep(random.uniform(0.3,1))
            item(random.uniform(600,650))
            sleep(random.uniform(0.3,1))
            item(random.uniform(550,600))
            sleep(random.uniform(0.3,1))
            item(random.uniform(500,550))
            sleep(random.uniform(0.3,1))
            item(random.uniform(450,500))
            sleep(random.uniform(0.3,1))
            item(random.uniform(400,450))
            sleep(random.uniform(0.3,1))
            item(random.uniform(350,400))
            sleep(random.uniform(0.3,1))
            item(random.uniform(300,350))
            sleep(random.uniform(0.3,1))
            item(random.uniform(250,300))
            sleep(random.uniform(0.3,1))
            item(random.uniform(200,250))
        except:
            sleep(0.5)
            continue
