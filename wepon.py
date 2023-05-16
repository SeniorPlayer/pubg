from contants import c_contants
class c_wepone():
    def __init__(self, name = 'none', mirror = '', muzzle = '', grip = '', butt = ''):
        '''
        :param name: 武器名称
        :param mirror: 倍镜
        :param muzzle: 枪口
        :param grip: 握把
        :param butt: 枪托
        '''
        self.name = name
        self.maxBullets = 0 #子弹最大数量
        self.model = 'auto'
        self.speed = 0  # 每发射击间隔
        self.basic = []  # 压强幅度
        self.posture_states = []
        self.parts = [mirror, muzzle, grip, butt]  # 配件列表
        self.k = 1.0  # 配件压枪系数,最后结果由各部分配件累乘得到
        self.interval = 0  # 每发射击间隔
        self.hold = 1.33
        if name != "none" and name != '':
            try:
                gun_data = c_contants.guns[name]
                self.maxBullets = gun_data['maxBullets']
                self.model = gun_data['model']
                self.speed = gun_data['speed']
                self.basic = gun_data['basic']
                self.posture_states.append(gun_data['posture']['default'])
                self.posture_states.append(gun_data['posture']['squat'])
                self.posture_states.append(gun_data['posture']['down'])
                self.hold = gun_data['hold']
                if mirror!= 'none' and mirror != '':
                    self.k *= gun_data['mirror'][mirror]
                if muzzle != 'none' and muzzle != '':
                    self.k *= gun_data['muzzle'][muzzle]
                if grip != 'none' and grip != '':
                    self.k *= gun_data['grip'][grip]
                if 'butt' in gun_data.keys() and butt in gun_data['butt'].keys() and butt != 'none' and muzzle != '':
                    self.k *= gun_data['butt'][butt]
            except Exception as e:
                print(type(e), '::', e)
        else:
            pass