import pygame
import random
from plane_main import SCREEN_SIZE

CREATE_ENEMY_EVENT = pygame.USEREVENT
ENEMY1_DOWN_PICTURE = "./images/enemy1_down{}.png"


# 飞机精灵类
class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image, speed=1):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class Plane(GameSprite):

    def __init__(self):
        super().__init__("./images/me1.png", 0)
        self.rect.x = SCREEN_SIZE.centerx - 0.5 * self.rect.width
        self.rect.bottom = SCREEN_SIZE.height - 120
        self.bullet_group = pygame.sprite.Group()
        self.keys = None

    def update(self):
        if self.keys:
            if self.keys[pygame.K_UP]:
                print("向上飞")
                self.rect.y -= 3
                if self.rect.y <= SCREEN_SIZE.top:
                    self.rect.y = SCREEN_SIZE.top

            if self.keys[pygame.K_LEFT]:
                print("向左飞")
                self.rect.x -= 3
                if self.rect.x <= SCREEN_SIZE.left:
                    self.rect.x = SCREEN_SIZE.left

            if self.keys[pygame.K_DOWN]:
                print("向下飞")
                self.rect.y += 3
                if self.rect.bottom >= SCREEN_SIZE.bottom:
                    self.rect.y = SCREEN_SIZE.bottom - self.rect.height

            if self.keys[pygame.K_RIGHT]:
                print("向右飞")
                self.rect.x += 3
                if self.rect.right >= SCREEN_SIZE.right:
                    self.rect.right = SCREEN_SIZE.right

    def fire(self):
        print("开火")
        bullet = Bullet()
        bullet.rect.bottom = self.rect.y - 10
        bullet.rect.centerx = self.rect.centerx

        self.bullet_group.add(bullet)


class Bullet(GameSprite):

    def __init__(self):
        super().__init__("./images/bullet2.png", -2)

    def update(self):
        super().update()
        if self.rect.y <= 0:
            self.kill()

    def __del__(self):
        print("子弹销毁")


class Enemy(GameSprite):

    def __init__(self):
        super().__init__("./images/enemy1.png", random.randint(1, 2))
        self.rect.x = random.randint(0, SCREEN_SIZE.width-self.rect.width)
        self.rect.y = -self.rect.height

    def update(self):

        self.rect.y += self.speed
        if self.rect.y >= SCREEN_SIZE.height:
            self.kill()

    def __del__(self):
        print("敌机消失了")


class Background(GameSprite):

    def __init__(self, is_alt=False):
        super().__init__("./images/background.png")
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_SIZE.height:
            self.rect.y = -self.rect.y


class EnemyBoom(GameSprite):

    def __init__(self, rect, picture_index):
        super().__init__(ENEMY1_DOWN_PICTURE.format(picture_index), 0)
        self.rect = rect
        self.index = picture_index

    def update(self):
        if self.index > 4:
            self.kill()

        if self.index <= 4:
            self.image = pygame.image.load(ENEMY1_DOWN_PICTURE.format(self.index))
            self.index += 1

    def __del__(self):
        print("爆炸销毁")


class PlaneBoom(GameSprite):

    def __init__(self):
        pass