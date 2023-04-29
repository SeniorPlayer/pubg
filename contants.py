from concurrent.futures import ThreadPoolExecutor


class c_contants():
    # 程序退出标记
    exitFlag = False
    bagOpen = False
    hold = False
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
                "down": 0.43,
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
                "rifle_compensate": 0.84,
                # 消焰
                "rifle_flame": 0.84,
            },
            "speed": 100,
            "basic": [35, 28, 29, 28, 42, 43, 42, 43, 46, 46, 46, 47, 52, 53, 52, 53, 52, 53, 52, 53, 52, 53, 52, 53,
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
                "squat": 0.75
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
                "rifle_compensate": 0.84,
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
            "basic": [30, 23, 24, 23, 33, 34, 34, 34, 40, 40, 40, 40, 41, 41, 41, 42, 46, 46, 46, 46, 46, 46, 46, 46,
                      46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 57, 58, 57, 58]
        },
        "sks": {
            "type": "snipe",
            "model": 'single',  # 模式，自动或者单发
            "maxBullets": 20,
            # shift
            "hold": 1.35,
            # 姿势
            "posture": {
                "default": 1,
                "down": 0.44,
                "squat": 0.64
            },
            # 倍镜
            "mirror": {
                "none": 1,
                "x15": 10.3,
                "x2": 1.7,
                "x3": 2.55,
                "x4": 3.55,
                "x4_1": 3.55,
                "x6": 5.1,
                "x8": 6.8
            },
            # 枪口
            "muzzle": {
                "rifle_compensate": 0.88,
                "rifle_flame": 0.88,
                "snipe_compensate": 0.88,
                "snipe_flame": 0.88
            },
            "butt": {
                "sks": 0.84
            },
            # 握把
            "grip": {
                "half": 0.88,
                "thumb": 0.94,
                "vertical": 0.78
            },
            "speed": 125,
            "basic": [25, 25, 25, 25, 81, 81, 81, 81, 75, 75, 75, 75, 75, 75, 75, 75, 90, 90, 90, 97]
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
                "down": 0.58,
                "squat": 0.83
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
                "rifle_compensate": 0.86,
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
        }
    }

    def __init__(self):
        pass
