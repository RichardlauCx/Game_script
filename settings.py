class Settings():  # 存储外星人入侵项目所有设置的类
    def __init__(self):  # 初始化游戏的设置
        self.screen_width = 1200  # d对屏幕的设置
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5

        self.bullet_speed_factor = 6
        self.bullet_width = 6
        self.bullet_height = 15
        self.bullet_color = 99, 99, 99
        self.bullets_allowed = 60

        self.thano_speed_factor = 1  # 泰坦飞船设置
        self.fleet_drop_speed = 6
        self.fleet_direction = 1  # 为1时表示向右移动，为-1时表示向左移动
        # available_space_x = first_settings.screen_width - (2 * thanos_width)
        # number_thanos_x = available_space_x / (2 * thanos_width)
