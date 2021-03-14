import sys
from GameSprite import *

SCREEN_SIZE = pygame.Rect(0, 0, 480, 700)
TIME_TICK = 60


class PlaneGame:

    def __init__(self):

        pygame.init()
        # 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_SIZE.size)
        pygame.display.set_caption("飞机大战")
        # 创建时钟
        self.clock = pygame.time.Clock()
        # 创建敌机
        self.__create_sprite()

        # 创建敌机定时器
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_over()
            if event.type == CREATE_ENEMY_EVENT:
                self.enemy_group.add(Enemy())
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.plane.fire()

        self.plane.keys = pygame.key.get_pressed()

    def __update_sprite(self):
        self.background.draw(self.screen)
        self.background.update()

        self.enemy_group.draw(self.screen)
        self.enemy_group.update()

        self.plane_group.draw(self.screen)
        self.plane_group.update()

        self.plane.bullet_group.draw(self.screen)
        self.plane.bullet_group.update()

        self.boom_group.draw(self.screen)
        self.boom_group.update()

    def __create_sprite(self):
        bg1 = Background()

        bg2 = Background(is_alt=True)
        bg2.rect.y = -bg2.rect.height

        self.plane = Plane()

        self.background = pygame.sprite.Group(bg1, bg2)
        self.enemy_group = pygame.sprite.Group()
        self.plane_group = pygame.sprite.Group(self.plane)

        self.boom_group = pygame.sprite.Group()

    def __check_collide(self):
        enemy_list = pygame.sprite.groupcollide(self.enemy_group, self.plane.bullet_group, True, True)
        if enemy_list:
            for enemy in enemy_list:
                self.boom_group.add(EnemyBoom(enemy.rect, 1))

        result = pygame.sprite.spritecollide(self.plane, self.enemy_group, True)
        if len(result) > 0:
            PlaneGame.__game_over()

    def start_game(self):
        while True:
            # 设置刷新帧率
            self.clock.tick(TIME_TICK)
            # 设置时间监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新/绘制敌机
            self.__update_sprite()
            # 更新显示
            pygame.display.update()

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        sys.exit(0)


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
