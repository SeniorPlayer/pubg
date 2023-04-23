import os

import cv2
import numpy as np
import pydirectinput

from Screen import shotCut,shotCutTest
import time
import pyautogui
from contants import c_contants

wepone1 = 'none'
wepone2 = 'none'
a = []
def initWepone(x,y,w,h):
    wepones = ["./resource/akm.bmp", './resource/m416.bmp']
    weponeNames = ["akm", "m416"]
    im = shotCut(x,y,w,h)
    index = 0
    for item in wepones:
        curWepone = cv2.imread(item, 0)
        thresh,temp = cv2.threshold (curWepone, 230, 255, cv2.THRESH_BINARY)
        res = cv2.matchTemplate(im, temp, cv2.TM_CCOEFF_NORMED)
        # min_max = cv2.minMaxLoc(res)
        # match_loc = min_max[3]
        # if match_loc[0] > 0 and match_loc[1] > 0:
        #     a.append(match_loc)
        loc = np.where(res > 0.9)
        if len(loc[0]) > 0:
            return weponeNames[index]
        index = index + 1


pydirectinput.PAUSE = 0


def adaptive_binarization(img):
    #自适应二值化
    maxval = 255
    blockSize = 5
    C = 5
    img2 = cv2.adaptiveThreshold(img, maxval, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize, C)
    return img2

if __name__ == '__main__':
    # im = shotCutTest()
    # img2 = adaptive_binarization(np.array(im))
    # curWepone = cv2.imread("./resource/test.bmp", 0)
    # temp = adaptive_binarization(np.array(curWepone))
    # cv2.imshow("test", img2)
    # cv2.waitKey(0)
    # res = cv2.matchTemplate(img2, temp, cv2.TM_CCOEFF_NORMED)
    # loc = np.where(res > 0.9)
    # print(loc)
    # a = [30, 23, 24, 23, 33, 34, 34, 34, 40, 40, 40, 40, 41, 41, 41, 42, 46, 46, 46, 46, 46, 46, 46, 46,
    #      46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 57, 58, 57, 58]
    # print(len(a))
    # num = 0
    # sum = 0
    # res = []
    # for i in range(40):
    #     if num == 3:
    #         res.append(sum/10)
    #         num = 0
    #         sum = 0
    #     num += 1
    #     sum += a[i]
    # print(res)
    for filename in os.listdir("./resource/buqiang/"):
        print(filename)
        if filename == 'akm.bmp' or filename == 'm416.bmp':
            continue
        file = "./resource/buqiang/" + filename
        im = cv2.imread("./resource/buqiang/" + filename, 0)
        cv2.imwrite("./resource/aa/" + filename, im[8:42, 55:140])
        time.sleep(0.1)