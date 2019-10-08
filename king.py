# -*- coding: utf-8 -*-

import wda
import random
from time import sleep

class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y


def autoMoney(session: wda.Session):
    while (True):
        session.tap(767, 587.5)
        session.tap(1000, 790)
        sleep(0.3)

if __name__ == '__main__':

    c = wda.Client(url='http://172.20.10.8:8100')
    s = c.session()
    autoMoney(session=s)