from wepon import c_wepone

def getCurrentWepone():
    if 1 == c_equipment.switch:
        return c_equipment.wepone1
    elif 2 == c_equipment.switch:
        return c_equipment.wepone2
    else:
        return c_equipment.none


# 装备栏
class c_equipment():
    #是否打开装备栏
    checkFlag = False
    #装备1
    wepone1 = c_wepone()
    #装备2
    wepone2 = c_wepone()
    #无装备
    none = c_wepone()
    #选择几号装备
    switch = 1

    def __init__(self):
        pass