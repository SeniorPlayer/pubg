
import cv2
import numpy
import pyautogui

def adaptive_binarization(img):
    #自适应二值化
    maxval = 255
    blockSize = 3
    C = 5
    img2 = cv2.adaptiveThreshold(img, maxval, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize, C)
    return img2

# 屏幕截图
def shotCut(x, y, w, h):
    im = pyautogui.screenshot(region=[x, y, w, h])
    screen = cv2.cvtColor(numpy.asarray(im), cv2.COLOR_BGR2GRAY)
    temp = adaptive_binarization(screen)
    return temp

def shotCutTest():
    img = cv2.imread(r'./resource/shotcut/screen.bmp', 0)
    temp = adaptive_binarization(img)
    return temp
