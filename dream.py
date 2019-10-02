# -*- coding: utf-8 -*-

import wda
import random

class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y


# 编辑按钮位置
def editPoint(section: wda.Session):
    if (section.window_size() == (414, 736)):
        return Point(x=360, y=430)
    else:
        return Point(x=770, y=650)


# 升级按钮位置
def updatePoint(section: wda.Session):
    if (section.window_size() == (414, 736)):
        return Point(x=330, y=660)
    else:
        return Point(x=660, y=1010)


# 划线x坐标
def lineX(section: wda.Session):
    if (section.window_size() == (414, 736)):
        return [random.uniform(100, 120), random.uniform(190, 210), random.uniform(290, 310)]
    else:
        return [random.uniform(230, 330), random.uniform(380, 470), random.uniform(530, 610)]


# 建筑物坐标
def buildsPoint(section: wda.Session):
    if (section.window_size() == (414, 736)):
        return [Point(x=110, y=270), Point(x=200, y=230), Point(x=300, y=170),
                Point(x=110, y=350), Point(x=200, y=310), Point(x=300, y=260),
                Point(x=110, y=470), Point(x=200, y=400), Point(x=300, y=360)]
    else:
        return [Point(x=270, y=390), Point(x=400, y=330), Point(x=540, y=250),
                Point(x=270, y=540), Point(x=400, y=480), Point(x=540, y=390),
                Point(x=270, y=690), Point(x=400, y=620), Point(x=540, y=550)]


# 货物坐标
def goodsPoints(section: wda.Session):
    if (section.window_size() == (414, 736)):
        return [Point(x=250, y=620), Point(x=310, y=600), Point(x=370, y=560)]
    else:
        return [Point(x=470, y=920), Point(x=565, y=900), Point(x=640, y=850)]


# 自动升级建筑
def autoUpdateBuilds(section: wda.Session, indexs: [int]):
    builds = map(lambda index: buildsPoint(section=section)[index], indexs)
    edit = editPoint(section=section)
    update = updatePoint(section=section)
    section.tap(edit.x, edit.y)

    for build in builds:
        section.tap(build.x, build.y)
        i = 10
        while (i > 0):
            i = i - 1
            section.tap(update.x, update.y)
    section.tap(edit.x, edit.y)


# 自动刷新货物
def autoGetGoods(section: wda.Session, indexs: [int]):
    builds = map(lambda index: buildsPoint(section=section)[index], indexs)
    goodss = goodsPoints(section=section)
    for goods in goodss:
        for build in builds:
            i = 2
            while (i > 0):
                i = i - 1
                section.swipe(x1=goods.x, x2=build.x, y1=goods.y, y2=build.y, duration=0.1)


# 自动刷新金币
def autoMoney(section: wda.Session, indexs: [int]):
    xs = map(lambda index: lineX(section=section)[index], indexs)
    y1 = random.uniform(100, 200)
    y2 = random.uniform(section.window_size().height - 100, section.window_size().height)
    duration = random.uniform(0.1, 0.5)
    for x in xs:
        section.swipe(x1=int(x), y1=int(y1), x2=int(x), y2=int(y2), duration=duration)
