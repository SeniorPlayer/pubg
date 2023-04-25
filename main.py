import pynput.keyboard as keyboard
from pynput import mouse
from equipment import c_equipment,check
from mouse import *
from contants import  c_contants


#1，2选择武器
#num_lock开启关闭
#f12测试




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