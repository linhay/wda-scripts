# -*- coding: utf-8 -*-

import wda
import dream
from time import sleep


if __name__ == '__main__':

    dream.c = wda.Client()
    dream.s = dream.c.session()

    while (True):
        try:
            # dream.autoMoney(section=s, indexs=[2])
            # sleep(2)
            # dream.autoUpdateBuilds(section=s, indexs=[3,4,5])
            # sleep(2)
            dream.c.screenshot('./dream.png')
            # dream.exchange_build()
            if (dream.is_has_train()):
                print('--有火车--')
                dream.newAutoGetGoods(section=dream.s, indexs=[0, 1])
                # dream.newAutoGetGoods(section=dream.s, indexs=[0])
            else:
                print('--无火车--')
                sleep(0.5)

        except:
            continue
