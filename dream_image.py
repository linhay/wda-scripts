import cv2
import numpy
from time import sleep


def image_resized(image: numpy.ndarray, scale: float):
    width = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)
    dim = (width, height)
    return cv2.resize(image, dim, interpolation=cv2.INTER_AREA)


def image_color_equal(image: numpy.ndarray, x: int, y: int, color: list):
    for item in (image[y][x] == color):
        if (not item):
            return False
        return True

# 是否有火车
def is_has_train():
    return not image_color_equal(image=image(), y=643, x=244, color=[90, 112, 118])


def image():
    img_path = './dream.png'
    image = cv2.imread(filename=img_path)
    return image_resized(image, 0.333)


def show():
    img_path = './dream-02.png'
    image = cv2.imread(filename=img_path)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    image = image_resized(image, 0.333)
    # winname弹出窗口的名字，mat为传入的图片对象
    cv2.imshow(winname='show the image', mat=image)
    # print(image_color_equal(image=image, y=643, x=244, color=[90, 112, 118]))
    # 窗口默认一直处于弹出窗状态
    cv2.waitKey()
    # 按任意键盘，销毁窗口
    # cv2.destroyAllWindows()


# 262,646
show()