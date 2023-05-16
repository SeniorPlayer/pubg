from concurrent.futures import ThreadPoolExecutor


class c_contants():
    # 程序退出标记
    exitFlag = False
    #背包打开标记
    bagOpen = False
    #屏息标记
    hold = False
    #姿势 0默认 1下蹲 2趴下
    posture = 0
    pool = ThreadPoolExecutor(max_workers=10)
    guns = {
        "none": {
            "speed": 100,
            "basic": [35, 28, 29, 28, 42, 43, 42, 43, 46, 46, 46, 47, 52, 53, 52, 53, 52, 53, 52, 53, 52, 53, 52, 53,
                      52, 53, 52, 53, 53, 54, 54, 54, 53, 54, 54, 54, 67, 68, 67, 68]
        },
        "akm": {
            "type": "rifle",
            "model": 'auto',  # 模式，自动或者单发
            "maxBullets": 40,
            # shift
            "hold": 1.33,
            # 姿势
            "posture": {
                "default": 1,
                "down": 0.45,
                "squat": 0.75
            },
            # 倍镜
            "mirror": {
                "none": 1,
                "x2": 1.7,
                "x3": 2.6,
                "x4": 3.6,
                "x4_1": 3.6,
                "x6": 5.2
            },
            # 枪口
            "muzzle": {
                # 补偿
                "rifle_compensate": 0.80,
                # 消焰
                "rifle_flame": 0.84,
            },
            "speed": 100,
            "basic": [40, 28, 29, 28, 42, 43, 42, 43, 48, 48, 46, 47, 52, 53, 52, 53, 52, 53, 52, 53, 52, 53, 52, 53,
                      52, 53, 52, 53, 53, 54, 54, 54, 53, 54, 54, 54, 67, 68, 67, 68]
        },
        "m416": {
            "type": "rifle",
            "model": 'auto',  # 模式，自动或者单发
            "maxBullets": 42,
            # shift
            "hold": 1.33,
            # 姿势
            "posture": {
                "default": 1,
                "down": 0.5,
                "squat": 0.80
            },
            # 倍镜
            "mirror": {
                "none": 1,
                "x2": 1.7,
                "x3": 3.2,
                "x4": 3.6,
                "x4_1": 3.6,
                "x6": 5.2
            },
            # 枪口
            "muzzle": {
                # 补偿
                "rifle_compensate": 0.80,
                # 消焰
                "rifle_flame": 0.84,
            },
            "butt": {
                "none": 1,
                "m4": 0.965,
                "m41": 0.965
            },
            # 握把
            "grip": {
                "half": 0.77,
                "thumb": 0.92,
                "vertical": 0.77
            },
            "speed": 86,
            "basic": [37, 16, 24, 23, 33, 34, 34, 34, 40, 40, 40, 40, 41, 41, 41, 42, 46, 46, 46, 46, 46, 46, 46, 46,
                      46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 57, 58, 57, 58]
        },
        "ace32": {
            "type": "rifle",
            "model": 'auto',  # 模式，自动或者单发
            "maxBullets": 40,
            # shift
            "hold": 1.33,
            # 姿势
            "posture": {
                "default": 1,
                "down": 0.45,
                "squat": 0.75
            },
            # 倍镜
            "mirror": {
                "none": 1.06,
                "x2": 1.7,
                "x3": 2.6,
                "x4": 3.6,
                "x4_1": 3.6,
                "x6": 5.1
            },
            # 枪口
            "muzzle": {
                "rifle_compensate": 0.80,
                "rifle_flame": 0.84
            },
            "butt": {
                "m4": 0.97
            },
            # 握把
            "grip": {
                "half": 0.77,
                "thumb": 0.92,
                "vertical": 0.77
            },
            "speed": 88,
            #                                                             15
            "basic": [39, 30, 27, 37, 36, 43, 44, 45, 42, 45, 45, 47, 45, 45, 46, 46, 52, 49, 49, 49, 52, 52, 52, 52,
                      52, 52, 52, 52, 52, 52, 52, 52, 53, 53, 53, 53, 63, 63, 63, 63]
        },
        "m762": {
            "type": "rifle",
            "model": 'auto',  # 模式，自动或者单发
            "maxBullets": 40,
            # shift
            "hold": 1.33,
            # 姿势
            "posture": {
                "default": 1,
                "down": 0.55,
                "squat": 0.80
            },
            # 倍镜
            "mirror": {
                "none": 1,
                "x2": 1.72,
                "x3": 2.62,
                "x4": 3.62,
                "x4_1": 3.62,
                "x6": 5.2
            },
            # 枪口
            "muzzle": {
                "rifle_compensate": 0.80,
                "rifle_flame": 0.86,
            },
            # 握把
            "grip": {
                "half": 0.8,
                "thumb": 0.93,
                "vertical": 0.78
            },
            "speed": 86,
            "basic": [42, 36, 36, 36, 42, 43, 42, 43, 54, 55, 54, 55, 54, 55, 54, 55, 62, 62, 62, 62, 62, 62, 62, 62,
                      62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 77, 78, 77, 78]
        },
        "aug": {
            "type": "rifle",
            "model": 'auto',  # 模式，自动或者单发
            "maxBullets": 40,
            # shift
            "hold": 1.33,
            # 姿势
            "posture": {
                "default": 1,
                "down": 0.55,
                "squat": 0.8
            },
            # 倍镜
            "mirror": {
                "none": 1,
                "x2": 1.7,
                "x3": 2.6,
                "x4": 3.6,
                "x4_1": 3.6,
                "x6": 5.1
            },
            # 枪口
            "muzzle": {
                "rifle_compensate": 0.80,
                "rifle_flame": 0.86,
            },
            # 握把
            "grip": {
                "half": 0.82,
                "thumb": 0.92,
                "vertical": 0.8
            },
            "speed": 80,#                                                 15
            "basic": [39, 15, 19, 18, 32, 28, 27, 35, 37, 33, 39, 38, 43, 43, 43, 43, 47, 47, 47, 47, 47, 48, 48, 48,
                      #               30                                      40
                      48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 55, 55, 55, 55]
        },
        "g36c": {
            "type": "rifle",
            "model": 'auto',  # 模式，自动或者单发
            "maxBullets": 40,
            # shift
            "hold": 1.33,
            # 姿势
            "posture": {
                "default": 1,
                "down": 0.50,
                "squat": 0.75
            },
            # 倍镜
            "mirror": {
                "none": 1,
                "x2": 1.72,
                "x3": 2.6,
                "x4": 3.6,
                "x4_1": 3.6,
                "x6": 5.1
            },
            # 枪口
            "muzzle": {
                "rifle_compensate": 0.84,
                "rifle_flame": 0.84,
            },
            # 握把
            "grip": {
                "half": 0.75,
                "thumb": 0.92,
                "vertical": 0.77
            },
            "speed": 86,
            "basic": [37, 10, 20, 20, 31, 31, 31, 32, 37, 35, 37, 38, 42, 43, 42, 43, 44, 46, 46, 47, 46, 46, 46, 47,
                      46, 46, 46, 47, 46, 46, 46, 47, 46, 46, 46, 47, 57, 58, 58, 58]
        },
        "groza": {
            "type": "rifle",
            "model": 'auto',  # 模式，自动或者单发
            "maxBullets": 40,
            # shift
            "hold": 1.33,
            # 姿势
            "posture": {
                "default": 1,
                "down": 0.45,
                "squat": 0.67
            },
            # 倍镜
            "mirror": {
                "none": 1,
                "x2": 1.75,
                "x3": 2.6,
                "x4": 3.6,
                "x4_1": 3.6,
                "x6": 5.2
            },
            # 枪口
            "muzzle": {
                "rifle_compensate": 1,
                "rifle_flame": 1,
            },
            "speed": 80,
            "basic": [30, 21, 21, 21, 30, 30, 30, 30, 30, 30, 30, 30, 37, 38, 37, 38, 37, 38, 37, 38, 40, 40, 40, 40,
                      40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 50, 50, 50, 50]
        },
        "k2": {
            "type": "rifle",
            "model": 'auto',  # 模式，自动或者单发
            "maxBullets": 44,
            # shift
            "hold": 1.33,
            # 姿势
            "posture": {
                "default": 1,
                "down": 0.5,
                "squat": 0.75
            },
            # 倍镜
            "mirror": {
                "none": 1,
                "x2": 1.75,
                "x3": 2.6,
                "x4": 3.6,
                "x4_1": 3.6,
                "x6": 5.2
            },
            # 枪口
            "muzzle": {
                "rifle_compensate": 0.80,
                "rifle_flame": 0.84,
            },
            "speed": 43,
            "basic": [15, 8, 9, 8, 9, 9, 9, 9, 35, 35, 35, 35, 35, 35, 35, 35, 42, 43, 42, 43, 44, 44, 44, 44, 44,
                      44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 55, 55, 55, 55]
        },
        "mp5": {
            "type": "sub",
            "model": 'auto',  # 模式，自动或者单发
            "maxBullets": 32,
            # shift
            "hold": 1.28,
            # 姿势
            "posture": {
                "default": 1,
                "down": 0.5,
                "squat": 0.65
            },
            # 倍镜
            "mirror": {
                "none": 1,
                "x2": 1.9,
                "x3": 2.9,
                "x4": 4,
                "x4_1": 4,
                "x6": 5.8
            },
            # 枪口
            "muzzle": {
                "rifle_compensate": 1,
                "rifle_flame": 1,
            },
            "grip": {
                "half": 0.89,
                "thumb": 0.91,
                "vertical": 0.74
            },
            "speed": 83.75,
            "basic": [21, 21, 21, 22, 41, 41, 41, 42, 36, 36, 36, 37, 36, 36, 36, 37, 36, 36, 36, 37, 36, 36, 36, 37,
                      36, 36, 36, 37, 43, 44, 43, 44]
        },
        "p90": {
            "type": "sub",
            "model": 'auto',  # 模式，自动或者单发
            "maxBullets": 28,
            # shift
            "hold": 1.15,
            # 姿势
            "posture": {
                "default": 1,
                "down": 0.65,
                "squat": 0.75
            },
            # 倍镜
            "mirror": {
                "none": 1,
                "x2": 1.8
            },
            "speed": 105,
            "basic": [23, 23, 23, 23, 32, 33, 32, 33, 26, 26, 26, 27, 19, 20, 19, 20, 24, 25, 24, 25, 21, 21, 21, 22,
                      21, 21, 21, 22]
        },
        "pp19": {
            "type": "sub",
            "model": 'auto',  # 模式，自动或者单发
            "maxBullets": 44,
            # shift
            "hold": 1.28,
            # 姿势
            "posture": {
                "default": 1,
                "down": 0.68,
                "squat": 0.78
            },
            # 倍镜
            "mirror": {
                "none": 1,
                "x2": 1.9,
                "x3": 2.9,
                "x4": 4,
                "x4_1": 4,
                "x6": 5.7
            },
            # 枪口
            "muzzle": {
                "rifle_compensate": 1,
                "rifle_flame": 1,
            },
            "speed": 107.5,
            "basic": [20, 20, 20, 20, 31, 32, 31, 32, 28, 29, 29, 29, 26, 26, 26, 27, 26, 26, 26, 27, 26, 26, 26, 27,
                      26, 26, 26, 27, 26, 26, 26, 27, 26, 26, 26, 27, 26, 26, 26, 27, 10, 11, 10, 11]
        },
        "qbz": {
            "type": "rifle",
            "model": 'auto',  # 模式，自动或者单发
            "maxBullets": 40,
            # shift
            "hold": 1.33,
            # 姿势
            "posture": {
                "default": 1,
                "down": 0.5,
                "squat": 0.78
            },
            # 倍镜
            "mirror": {
                "none": 1,
                "x2": 1.72,
                "x3": 2.6,
                "x4": 3.6,
                "x4_1": 3.6,
                "x6": 5.1
            },
            # 枪口
            "muzzle": {
                "rifle_compensate": 0.75,
                "rifle_flame": 0.84,
            },
            "grip": {
                "half": 0.75,
                "thumb": 0.92,
                "vertical": 0.77
            },
            "speed": 92,
            "basic": [23, 24, 24, 24, 30, 30, 30, 30, 38, 39, 39, 39, 47, 47, 47, 48, 47, 47, 47, 48, 47, 47, 47, 48,
                      47, 47, 47, 48, 47, 47, 47, 48, 47, 47, 47, 48, 59, 59, 59, 59]
        },
        "scarl": {
            "type": "rifle",
            "model": 'auto',  # 模式，自动或者单发
            "maxBullets": 40,
            # shift
            "hold": 1.33,
            # 姿势
            "posture": {
                "default": 1,
                "down": 0.53,
                "squat": 0.75
            },
            # 倍镜
            "mirror": {
                "none": 1,
                "x2": 1.72,
                "x3": 2.6,
                "x4": 3.6,
                "x4_1": 3.6,
                "x6": 5.1
            },
            # 枪口
            "muzzle": {
                "rifle_compensate": 0.80,
                "rifle_flame": 0.84,
            },
            "grip": {
                "half": 0.77,
                "thumb": 0.92,
                "vertical": 0.77
            },
            "speed": 96,
            "basic": [37, 15, 20, 20, 30, 30, 30, 27, 38, 39, 39, 39, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43,
                      43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 53, 54, 54, 54]
        },
        "tommy": {
            "type": "sub",
            "model": 'auto',  # 模式，自动或者单发
            "maxBullets": 44,
            # shift
            "hold": 1.28,
            # 姿势
            "posture": {
                "default": 1,
                "down": 0.58,
                "squat": 0.68
            },
            # 倍镜
            "mirror": {
                "none": 1
            },
            "grip": {
                "vertical": 0.77
            },
            "speed": 90,
            "basic": [22, 23, 22, 23, 26, 26, 26, 27, 58, 59, 59, 59, 51, 51, 51, 52, 51, 51, 51, 52, 51, 51, 51, 52,
                      51, 51, 51, 52, 51, 51, 51, 52, 51, 51, 51, 52, 51, 51, 51, 52, 41, 41, 41, 42]
        },
        "ump45": {
            "type": "sub",
            "model": 'auto',  # 模式，自动或者单发
            "maxBullets": 36,
            # shift
            "hold": 1.28,
            # 姿势
            "posture": {
                "default": 1,
                "down": 0.64,
                "squat": 0.74
            },
            # 倍镜
            "mirror": {
                "none": 1,
                "x2": 1.9,
                "x3": 2.9,
                "x4": 4,
                "x4_1": 4,
                "x6": 5.7
            },
            "grip": {
                "half": 0.84,
                "thumb": 0.91,
                "vertical": 0.77
            },
            "muzzle": {
                "sub_flame": 1,
                "sub_compensate": 1
            },
            "speed": 90,
            "basic": [18, 18, 18, 19, 26, 26, 26, 27, 26, 26, 26, 27, 32, 33, 32, 33, 30, 30, 30, 31, 30, 30, 30, 31,
                      30, 30, 30, 31, 30, 30, 30, 31, 37, 38, 37, 38]
        },
        "uzi": {
            "type": "sub",
            "model": 'auto',  # 模式，自动或者单发
            "maxBullets": 28,
            # shift
            "hold": 1.28,
            # 姿势
            "posture": {
                "default": 1,
                "down": 0.6,
                "squat": 0.75
            },
            # 倍镜
            "mirror": {
                "none": 1
            },
            "muzzle": {
                "sub_flame": 0.85,
                "sub_compensate": 0.65
            },
            "speed": 60,
            "basic": [10, 11, 10, 11, 23, 24, 24, 24, 30, 30, 30, 30, 38, 39, 39, 39, 38, 39, 39, 39, 40, 40, 40, 40,
                      48, 48, 48, 48]
        },
        "vector": {
            "type": "sub",
            "model": 'auto',  # 模式，自动或者单发
            "maxBullets": 28,
            # shift
            "hold": 1.28,
            # 姿势
            "posture": {
                "default": 1,
                "down": 0.64,
                "squat": 0.74
            },
            "butt": {
                "m4": 0.97
            },
            # 倍镜
            "mirror": {
                "none": 1,
                "x2": 1.9,
                "x3": 2.9,
                "x4": 4,
                "x4_1": 4,
                "x6": 5.7
            },
            "muzzle": {
                "sub_flame": 1,
                "sub_compensate": 1
            },
            "grip": {
                "half": 0.85,
                "thumb": 0.92,
                "vertical": 0.8
            },
            "speed": 68.75,
            "basic": [16, 17, 16, 17, 30, 30, 30, 30, 31, 31, 31, 32, 46, 46, 46, 47, 41, 41, 41, 42, 41, 41, 41, 42,
                      41, 41, 41, 42]
        },
    }

    def __init__(self):
        pass
