import threading

import cv2
import numpy as np
import pynput.keyboard as keyboard
from pynput import mouse

from Screen import shotCut,shotCutTest,adaptive_binarization
from equipment import c_equipment
from mouse import *
from contants import  c_contants

#1，2选择武器
#num_lock开启关闭
#f12测试
#

def initWepone(x, y, w, h):
    weponeBmps = ["./resource/guns/akm.bmp", './resource/guns/m416.bmp']
    weponeNames = ["akm", "m416"]
    im = shotCut(x, y, w, h)
    index = 0
    for item in weponeBmps:
        curWepone = cv2.imread(item, 0)
        temp = adaptive_binarization(curWepone)
        res = cv2.matchTemplate(im, temp, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res > 0.9)
        print(loc)
        if len(loc[0]) > 0:
            return weponeNames[index]
        index = index + 1
    return 'none'

def isArm(x, y, w, h):
    screen = shotCut(x, y, w, h)
    curWepone = cv2.imread("./resource/bag.bmp", 0)
    temp = adaptive_binarization(curWepone)
    res = cv2.matchTemplate(screen, temp, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res > 0.8)
    if len(loc[0]) > 0:
        return True
    return False


def check():
    c_equipment.checkFlag = True
    time.sleep(0.3)
    test = isArm(485, 75, 100, 50)
    print("test res:" + str(test))
    if test:
        c_equipment.wepone1.name = initWepone(1770, 120, 650, 280)
        c_equipment.wepone2.name = initWepone(1770, 430, 650, 280)
        print("w1" + str(c_equipment.wepone1.name))
        print("w2" + str(c_equipment.wepone2.name))
    c_equipment.checkFlag = False

def asyncHandle():
    if c_equipment.checkFlag:
        return
    c_contants.pool.submit(check)

# 键盘点击事件
def onRelease(key):
    try:
        if '1' == key.char:
            c_equipment.switch = 1
        elif '2' == key.char:
            c_equipment.switch = 2
        elif '3' == key.char:#手枪
            c_equipment.switch = 3
        elif '4' == key.char:#刀具
            c_equipment.switch = 3
        elif '5' == key.char:#手雷
            c_equipment.switch = 3
        print("key char" + str(key.char))
    except AttributeError:
        if 'tab' == key.name:
            asyncHandle()
        elif 'f12' == key.name:
            testMouse()
        elif 'num_lock' == key.name:
            changeOpen()
        print("key name" + str(key.name))

# 监听键盘
def listen_keybord():
    listener = keyboard.Listener(on_release=onRelease)
    listener.start()


# 监听鼠标
def listen_mouse():
    with mouse.Listener(on_click=onClick) as listener:
        listener.join()


if __name__ == '__main__':
    listen_keybord()
    listen_mouse()
    # test = isArm(485, 75, 100, 50)
    # print(test)