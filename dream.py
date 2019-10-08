# -*- coding: utf-8 -*-

import wda
import random
from time import sleep
import cv2
import numpy
from wda import Session

c: wda.Client = wda.Client(url='http://192.168.0.106:8100')
s: Session = c.session()


class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y


def image():
    img_path = './dream.png'
    image = cv2.imread(filename=img_path)
    return image_resized(image, 0.333)


def image_resized(image: numpy.ndarray, scale: float):
    width = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)
    dim = (width, height)
    return cv2.resize(image, dim, interpolation=cv2.INTER_AREA)


def image_color(image: numpy.ndarray, x: int, y: int):
    return image[y][x]


def image_color_equal(image: numpy.ndarray, x: int, y: int, color: list):
    for item in (image_color(image=image, x=x, y=y) == color):
        if (not item):
            return False
        return True


def is_image_color_in(color: list, max: list, min: list):
    for i in range(len(color)):
        if ((color[i] >= min[i]) and (color[i] <= max[i])):
            return i
    return -1


# 是否有火车
def is_has_train():
    return not image_color_equal(image=image(), y=643, x=244, color=[90, 112, 118])


def goods_detail():
    goodsPoints = goodsOfBuildPoint(section=s)

    for goodsIndex in range(len(goodsOfBuildPoint(section=s))):
        goods = goodsPoints[goodsIndex]
        s.tap_hold(goods.x, goods.y, duration=1)
        c.screenshot('./dream.png')


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
                Point(x=110, y=350), Point(x=200, y=300), Point(x=300, y=260),
                Point(x=110, y=470), Point(x=200, y=400), Point(x=300, y=360)]
    else:
        return [Point(x=270, y=390), Point(x=400, y=330), Point(x=540, y=250),
                Point(x=270, y=540), Point(x=400, y=480), Point(x=540, y=390),
                Point(x=270, y=690), Point(x=400, y=620), Point(x=540, y=550)]


def goodsOfBuildPoint(section: wda.Session):
    if (section.window_size() == (414, 736)):
        return [Point(x=177, y=273),
                Point(x=140, y=408),
                Point(x=287, y=220),
                Point(x=280, y=315)]
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
    builds = list(map(lambda index: buildsPoint(section=section)[index], indexs))
    edit = editPoint(section=section)
    update = updatePoint(section=section)
    sleep(0.5)
    section.tap(edit.x, edit.y)

    for build in builds:
        section.tap(build.x, build.y)
        i = 10
        while (i > 0):
            i = i - 1
            section.tap(update.x, update.y)
    sleep(0.5)
    section.tap(edit.x, edit.y)


def newAutoGetGoods(section: wda.Session, indexs: [int]):
    builds = list(map(lambda index: goodsOfBuildPoint(section=section)[index], indexs))
    goodss = goodsPoints(section=section)
    for goods in goodss:
        for build in builds:
            i = 2
            while (i > 0):
                i = i - 1
                print(goods.x, "-", goods.y, " : ", build.x, "-", build.y)
                section.swipe(x1=goods.x, y1=goods.y, x2=build.x, y2=build.y, duration=0.1)


# 自动刷新货物
def autoGetGoods(section: wda.Session, indexs: [int]):
    builds = list(map(lambda index: buildsPoint(section=section)[index], indexs))
    goodss = goodsPoints(section=section)
    for goods in goodss:
        for build in builds:
            i = 2
            while (i > 0):
                i = i - 1
                section.swipe(x1=goods.x, y1=goods.y, x2=build.x, y2=build.y, duration=0.1)


def tap_edit_btn():
    point = editPoint(section=s)
    s.tap(point.x, point.y)
    sleep(0.3)


def exchange_build():
    tap_edit_btn()
    builds = buildsPoint(section=s)
    builds = [builds[2], builds[5], builds[7], builds[8]]
    for build in builds:
        s.tap(build.x,build.y)
        s.tap(207,666)
        sleep(0.3)
        s.tap(208,311)
        sleep(0.3)
        s.tap(207,666)
        sleep(0.3)
        s.tap(build.x,build.y)
        sleep(0.3)
        s.tap(207,666)
        sleep(0.3)
        s.tap(208,311)
        sleep(0.3)
        s.tap(207,666)
        sleep(0.3)
    tap_edit_btn


# 自动刷新金币
def autoMoney(section: wda.Session, indexs: [int]):
    xs = list(map(lambda index: lineX(section=section)[index], indexs))
    y1 = random.uniform(100, 200)
    y2 = random.uniform(section.window_size().height - 100, section.window_size().height)
    duration = random.uniform(0.1, 0.5)
    for x in xs:
        section.swipe(x1=int(x), y1=int(y1), x2=int(x), y2=int(y2), duration=duration)
