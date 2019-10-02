# -*- coding: utf-8 -*-

import wda
import dream
from time import sleep

if __name__ == '__main__':

    c = wda.Client(url='http://172.20.10.8:8100')
    s = c.session()

    while (True):
        try:
            dream.autoMoney(section=s, indexs=[0, 1, 2])
            sleep(2)
            dream.autoUpdateBuilds(section=s, indexs=[3,4,5])
            sleep(2)
            dream.autoGetGoods(section=s, indexs=[0, 1, 2])
        except:
            continue
