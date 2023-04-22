import time

import pydirectinput

from contants import c_contants

pydirectinput.PAUSE = 0


def changeOpen():
    c_mouse.openFlag = not c_mouse.openFlag


def moveMouse():
    gun = c_contants.guns_3[c_mouse.repairName]
    basic = gun['basic']
    speed = gun['speed']
    print("curent" + str(basic))
    for i in range(14):
        if not c_mouse.leftPressed:
            break
        for j in range(speed):
            if not c_mouse.leftPressed:
                break
            pydirectinput.move(xOffset=0, yOffset=int(round(basic[i]*0.65, 0)), relative=True)
            time.sleep(0.03)

def handlePressed():
    if not c_mouse.leftPressed or not c_mouse.openFlag:
        return
    c_contants.pool.submit(moveMouse)


# 鼠标点击事件
def onClick(x, y, button, pressed):
    print(button.name)
    if 'left' == button.name:
        c_mouse.leftPressed = pressed
        handlePressed()
    return not c_contants.exitFlag


class c_mouse():
    leftPressed = False
    openFlag = False
    repairName = 'none'
    def __init__(self):
        pass
