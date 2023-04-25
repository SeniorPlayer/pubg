from concurrent.futures import ThreadPoolExecutor

class c_contants():
    # 程序退出标记
    exitFlag = False
    pool = ThreadPoolExecutor()
    guns = {
        "none": {
            "speed": 100,
            "basic": [35, 28, 29, 28, 42, 43, 42, 43, 46, 46, 46, 47, 52, 53, 52, 53, 52, 53, 52, 53, 52, 53, 52, 53,
                      52, 53, 52, 53, 53, 54, 54, 54, 53, 54, 54, 54, 67, 68, 67, 68]
        },
        "akm": {
            "type": "rifle",
            "model": 'auto',#模式，自动或者单发
            "maxBullets": 40,
            #shift
            "hold": 1.33,
            #姿势
            "posture": {
                "default": 1,
                "down": 0.43,
                "squat": 0.75
            },
            #倍镜
            "mirror": {
                "none": 1,
                "x2": 1.7,
                "x3": 2.6,
                "x4": 3.6,
                "x6": 5.2
            },
            #枪口
            "muzzle": {
                #补偿
                "rifle_compensate": 0.84,
                #消焰
                "rifle_flame": 0.84,
            },
            "speed": 100,
            "basic": [35, 28, 29, 28, 42, 43, 42, 43, 46, 46, 46, 47, 52, 53, 52, 53, 52, 53, 52, 53, 52, 53, 52, 53,
                      52, 53, 52, 53, 53, 54, 54, 54, 53, 54, 54, 54, 67, 68, 67, 68]
        },
        "m416": {
            "type": "rifle",
            "model": 'auto',#模式，自动或者单发
            "maxBullets": 42,
            #shift
            "hold": 1.33,
            #姿势
            "posture": {
                "default": 1,
                "down": 0.5,
                "squat": 0.75
            },
            #倍镜
            "mirror": {
                "none": 1,
                "x2": 1.7,
                "x3": 2.6,
                "x4": 3.6,
                "x6": 5.2
            },
            #枪口
            "muzzle": {
                #补偿
                "rifle_compensate": 0.84,
                #消焰
                "rifle_flame": 0.84,
            },
            "butt": {
                "m4": 0.965
            },
            #握把
            "grip": {
                "half": 0.77,
                "light": 0.77,
                "thumb": 0.92,
                "triangle": 1,
                "vertical": 0.77
            },
            "speed": 86,
            "basic": [30, 23, 24, 23, 33, 34, 34, 34, 40, 40, 40, 40, 41, 41, 41, 42, 46, 46, 46, 46, 46, 46, 46, 46,
                      46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 57, 58, 57, 58]
        }
    }

    def __init__(self):
        pass
