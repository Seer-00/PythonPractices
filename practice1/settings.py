import sys
import os


class Settings:
    """ 存储所有设置的类 """

    def __init__(self):
        """ 初始化游戏的设置 """
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # 1 表示向右移，-1 表示向左移
        # 记分
        self.alien_points = 50

        # 子弹设置
        # self.normal_bullet_width = 3
        # self.normal_bullet_height = 15
        self.normal_bullet_speed_factor = 1
        # self.faster_bullet_speed_factor = 20
        # self.huger_bullet_width = 0.75 * self.screen_width
        # self.huger_bullet_height = 0.1 * self.screen_height

        # self.bullet_speed_factor = self.normal_bullet_speed_factor
        # self.bullet_width = self.normal_bullet_width
        # self.bullet_height = self.normal_bullet_height
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # 加快游戏节奏的速度
        self.speedup_scale = 1.1
        # 外星人点数的提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

        # 增强
        self.once_only_bullet = True  # 一次性子弹
        self.limited_bullet = True  # 同屏有限子弹
        self.huger_bullet = False  # 大型子弹
        self.faster_bullet = False  # 快速子弹

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.normal_bullet_speed_factor = 1
        self.alien_speed_factor = 1

        # fleet_direction为1表示向右；为-1表示向左
        self.fleet_direction = 1

    def increase_speed(self):
        """ 提高速度设置和外星人点数 """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

    def set_bullet_speed_factor(self, value):
        self.normal_bullet_speed_factor *= value

    def get_bullet_speed_factor(self):
        # 最大速度，过快会无反应
        if 5 * self.normal_bullet_speed_factor > 10:
            return 10
        if self.faster_bullet:
            return 5 * self.normal_bullet_speed_factor
        else:
            return 1 * self.normal_bullet_speed_factor

    def get_bullet_width(self):
        if self.huger_bullet:
            return 0.8 * self.screen_width
        else:
            return 3

    def get_bullet_height(self):
        if self.huger_bullet:
            return 0.1 * self.screen_height
        else:
            return 15

    # 子弹设置
    bullet_speed_factor = property(get_bullet_speed_factor, set_bullet_speed_factor)
    bullet_width = property(get_bullet_width)
    bullet_height = property(get_bullet_height)


def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        absolute_path = os.path.join(sys._MEIPASS, relative)
    else:
        absolute_path = os.path.join(relative)
    return absolute_path


ship_path = resource_path('images\\ship.bmp')
alien_path = resource_path('images\\alien.bmp')
