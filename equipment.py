import cv2
import numpy
from wepon import c_wepone
from Screen import shotCut
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
        res = calculate_ssim(numpy.asarray(screenImg), numpy.asarray(curWepone))
        if res > 0.8:
            return str(fileName)[:-4]
    return name

#识别装备
def recognizeEquiment():
    #武器位置
    screenWepon1 = shotCut(1825, 125, 80, 40)
    #武器名字  1825, 125, 80, 40
    w1Name = compareAndGetName(screenWepon1, "./resource/guns/")
    #1825,431,80,40
    screenWepon2 = shotCut(1825,431,80,40)
    w2Name = compareAndGetName(screenWepon2, "./resource/guns/")
    #倍镜 2136, 160, 62, 30
    screenMirror1 = shotCut(2136, 160, 62, 30)
    m1Name = compareAndGetName(screenMirror1, "./resource/mirrors/")
    #2136, 466, 62, 30
    screenMirror2 = shotCut(2136, 466, 62, 30)
    m2Name = compareAndGetName(screenMirror2, "./resource/mirrors/")
    #握把 1915,336,50,52
    screenGrip1 = shotCut(1915,336,50,52)
    g1Name = compareAndGetName(screenGrip1, "resource/grip/")
    #1915, 642, 50, 52
    screenGrip2 = shotCut(1915, 642, 50, 52)
    g2Name = compareAndGetName(screenGrip2, "resource/grip/")
    #枪托 2344,340,50,48
    screenButt1 = shotCut(2344,340,50,48)
    butt1Name = compareAndGetName(screenButt1, "./resource/butt/")
    #2344, 646, 50, 48
    screenButt2 = shotCut(2344, 646, 50, 48)
    butt2Name = compareAndGetName(screenButt2, "./resource/butt/")
    #枪口 1780,336,50,52
    muzzleName1 = 'none'
    #1780, 642, 50, 52
    muzzleName2 = 'none'
    if w1Name != 'none':
        try:
            wepon1 = c_contants.guns[w1Name]
            gunType = wepon1['type']
            muzzle_path = "./resource/muzzle/" + gunType + "/"
            screenMuzzle1 = shotCut(1780,336,50,52)
            muzzleName1 = compareAndGetName(screenMuzzle1, muzzle_path)
        except Exception as e:
            print("装备栏1未识别")
    if w1Name != 'none':
        try:
            wepon1 = c_contants.guns[w1Name]
            gunType = wepon1['type']
            muzzle_path = "./resource/muzzle/" + gunType + "/"
            screenMuzzle2= shotCut(1780, 642, 50, 52)
            muzzleName2 = compareAndGetName(screenMuzzle2, muzzle_path)
        except Exception as e:
            print("装备栏2未识别")
    gun1 = c_wepone(w1Name, m1Name, muzzleName1, g1Name, butt1Name)
    gun2 = c_wepone(w2Name, m2Name, muzzleName2, g2Name, butt2Name)
    print(w1Name, m1Name, muzzleName1, g1Name, butt1Name)
    print(w2Name, m2Name, muzzleName2, g2Name, butt2Name)
    c_equipment.wepone1 = gun1
    c_equipment.wepone2 = gun2


def isBagOpen():
    #背包截图 501,78,72,38
    screen = shotCut(501,78,72,38)
    bag = cv2.imread("./bag.bmp", 0)
    res = calculate_ssim(numpy.asarray(screen), numpy.asarray(bag))
    if res > 0.8:
        return True
    return False

def posture():
    #姿势946, 1320, 42, 46
    screen = shotCut(946, 1320, 42, 46)

def check():
    c_equipment.checkFlag = True
    time.sleep(0.3)
    bagOpen = isBagOpen()
    c_contants.bagOpen = bagOpen
    print("test res:" + str(bagOpen))
    if bagOpen:
        recognizeEquiment()
    c_equipment.checkFlag = False

def ssim(img1, img2):
    C1 = (0.01 * 255) ** 2
    C2 = (0.03 * 255) ** 2
    img1 = img1.astype(numpy.float64)
    img2 = img2.astype(numpy.float64)
    kernel = cv2.getGaussianKernel(11, 1.5)
    window = numpy.outer(kernel, kernel.transpose())
    mu1 = cv2.filter2D(img1, -1, window)[5:-5, 5:-5]  # valid
    mu2 = cv2.filter2D(img2, -1, window)[5:-5, 5:-5]
    mu1_sq = mu1 ** 2
    mu2_sq = mu2 ** 2
    mu1_mu2 = mu1 * mu2
    sigma1_sq = cv2.filter2D(img1 ** 2, -1, window)[5:-5, 5:-5] - mu1_sq
    sigma2_sq = cv2.filter2D(img2 ** 2, -1, window)[5:-5, 5:-5] - mu2_sq
    sigma12 = cv2.filter2D(img1 * img2, -1, window)[5:-5, 5:-5] - mu1_mu2
    ssim_map = ((2 * mu1_mu2 + C1) * (2 * sigma12 + C2)) / ((mu1_sq + mu2_sq + C1) * (sigma1_sq + sigma2_sq + C2))
    return ssim_map.mean()


def calculate_ssim(img1, img2):
    if not img1.shape == img2.shape:
        raise ValueError('Input images must have the same dimensions.')
    if img1.ndim == 2:
        return ssim(img1, img2)
    elif img1.ndim == 3:
        if img1.shape[2] == 3:
            ssims = []
            for i in range(3):
                ssims.append(ssim(img1, img2))
            return numpy.array(ssims).mean()
        elif img1.shape[2] == 1:
            return ssim(numpy.squeeze(img1), numpy.squeeze(img2))
    else:
        raise ValueError('Wrong input image dimensions.')

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