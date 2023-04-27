import time

import pydirectinput

from contants import c_contants
from equipment import getCurrentWepone
pydirectinput.PAUSE = 0


def changeOpen():
    c_mouse.openFlag = not c_mouse.openFlag

def moveMouse():
    curWepone = getCurrentWepone()
    if(curWepone.name == 'none'):
        return
    basic = curWepone.basic
    speed = curWepone.speed
    startTime = round(time.perf_counter(), 3) * 1000
    if curWepone.model == 'auto':
        for i in range(curWepone.maxBullets):
            if not canFire():
                break
            holdK = 1
            if c_contants.hold:
                holdK = curWepone.hold
            moveSum = int(round(basic[i] * curWepone.k * holdK, 2))
            while True:
                if(moveSum > 10):
                    pydirectinput.move(xOffset=0, yOffset=10, relative=True)
                    moveSum -= 10
                elif(moveSum > 0):
                    pydirectinput.move(xOffset=0, yOffset=moveSum, relative=True)
                    moveSum = 0
                elapsed = (round(time.perf_counter(), 3) * 1000 - startTime)
                if not canFire() or elapsed > (i+1)*speed + 10:
                    break
                time.sleep(0.01)
    else:
        print()


def handlePressed():
    if not canFire():
        return
    c_contants.pool.submit(moveMouse)


# 鼠标点击事件
def onClick(x, y, button, pressed):
    if 'left' == button.name:
        c_mouse.leftPressed = pressed
        handlePressed()
    return not c_contants.exitFlag

#按下f1测试程序生效
def testMouse():
    if c_mouse.openFlag:
        for i in range(10):
            pydirectinput.moveRel(xOffset=0, yOffset=10)
            time.sleep(0.1)

# 是否可以开火
def canFire():
    return c_mouse.leftPressed and c_mouse.openFlag and not c_contants.exitFlag and not c_contants.bagOpen

class c_mouse():
    leftPressed = False
    openFlag = False
    def __init__(self):
        pass
