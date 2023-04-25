import cv2
import numpy
from wepon import c_wepone
from Screen import shotCut,adaptive_binarization
import os
from contants import c_contants
import time
def getCurrentWepone():
    if 1 == c_equipment.switch:
        return c_equipment.wepone1
    elif 2 == c_equipment.switch:
        return c_equipment.wepone2
    else:
        return c_equipment.none

#对比图片获取名字
def compareAndGetName(screenImg, dir):
    content = os.listdir(dir)
    name = 'none'
    for fileName in content:
        curWepone = cv2.imread(dir + fileName, 0)
        temp = adaptive_binarization(curWepone)
        res = cv2.matchTemplate(screenImg, temp, cv2.TM_CCOEFF_NORMED)
        loc = numpy.where(res > 0.9)
        if len(loc[0]) > 0:
            name = str(fileName)[:-4]
    return name

#识别装备
def recognizeEquiment():
    #武器位置
    screen = shotCut(1770, 120, 650, 590)
    #武器名字
    w1Name = compareAndGetName(screen[0:55, 50:150], "./resource/guns")
    w2Name = compareAndGetName(screen[300:355, 50:150], "./resource/guns")
    #倍镜
    m1Name = compareAndGetName(screen[30:100, 365:425], "./resource/mirrors")
    m2Name = compareAndGetName(screen[330:400, 365:425], "./resource/mirrors")
    #握把
    g1Name = compareAndGetName(screen[200:285, 135:205], "./resource/woba")
    g2Name = compareAndGetName(screen[500:585, 135:205], "./resource/woba")
    #枪托
    butt1Name = compareAndGetName(screen[200:285, 560:640], "./resource/butt")
    butt2Name = compareAndGetName(screen[500:585, 560:640], "./resource/butt")
    #枪口
    muzzleName1 = 'none'
    muzzleName2 = 'none'
    if w1Name != 'none':
        try:
            wepon1 = c_contants.guns[w1Name]
            gunType = wepon1['type']
            muzzle_path = "./resource/muzzle/" + gunType + "/"
            muzzleName1 = compareAndGetName(screen[200:285, 0:70], muzzle_path)
        except Exception as e:
            print("装备栏1未识别")
    if w1Name != 'none':
        try:
            wepon1 = c_contants.guns[w1Name]
            gunType = wepon1['type']
            muzzle_path = "./resource/muzzle/" + gunType + "/"
            muzzleName2 = compareAndGetName(screen[500:585, 0:70], muzzle_path)
        except Exception as e:
            print("装备栏2未识别")
    gun1 = c_wepone(w1Name, m1Name, muzzleName1, g1Name, butt1Name)
    gun2 = c_wepone(w2Name, m2Name, muzzleName2, g2Name, butt2Name)
    c_equipment.wepone1 = gun1
    c_equipment.wepone2 = gun2

def isBagOpen():
    screen = shotCut(485, 75, 100, 50)
    curWepone = cv2.imread("./resource/bag.bmp", 0)
    temp = adaptive_binarization(curWepone)
    res = cv2.matchTemplate(screen, temp, cv2.TM_CCOEFF_NORMED)
    loc = numpy.where(res > 0.8)
    if len(loc[0]) > 0:
        return True
    return False


def check():
    c_equipment.checkFlag = True
    time.sleep(0.3)
    bagOpen = isBagOpen()
    print("test res:" + str(bagOpen))
    if bagOpen:
        recognizeEquiment()
    c_equipment.checkFlag = False

# 装备栏
class c_equipment():
    #是否打开装备栏
    checkFlag = False
    #装备1
    wepone1 = c_wepone('none', '', '', '', '')
    #装备2
    wepone2 = c_wepone('none', '', '', '', '')
    #无装备
    none = c_wepone('none', '', '', '', '')
    #选择几号装备
    switch = 1

    def __init__(self):
        pass