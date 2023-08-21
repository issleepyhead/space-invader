from pygame.image import load
from pygame import (KEYDOWN, K_s, K_w, K_d, K_a, K_SPACE)
from pygame.key import get_pressed
from entity.Entity import Entity
from entity.Bullet import Bullet
from time import sleep
from entity.Bullet import Direction

class PlayerEntity(Entity):
    """A PlayerEntity class for every player in the game"""

    __ewidth  = 128
    __eheight = 128
    __lives   = 3

    def __init__(self, screen):
        self.screen = screen
        self.__img = "assets/spaceship.png"
        self.__entity = load(self.__img)

        self.__pos_x = self.screen.WINDOW_WIDTH / 2 - (self.__ewidth // 2)
        self.__pos_y = self.screen.WINDOW_HEIGHT - (self.__eheight + 50)

    def time_delta(self):
        mills = get_ticks()

    def draw(self):
        self.screen.SCREEN.blit(self.__entity, (self.__pos_x, self.__pos_y))

    def fire(self):
        if len(self.screen.bullets) < 20:
            bullet = Bullet(self.screen, self.__pos_x, self.__pos_y, Direction.UP)
            self.screen.bullets.append(bullet)


    def move(self):
        keys = get_pressed()
        if keys[K_w]:
            self.__pos_y -= 300 * self.screen.delta
        if keys[K_s]:
            self.__pos_y += 300 * self.screen.delta
        if keys[K_a]:
            self.__pos_x -= 300 * self.screen.delta
        if keys[K_d]:
            self.__pos_x += 300 * self.screen.delta
        if keys[K_SPACE]:
            self.fire()

        # player bounds
        if self.__pos_y < 0:
            self.__pos_y = 0
        if self.__pos_y > self.screen.WINDOW_HEIGHT - self.__eheight:
            self.__pos_y = self.screen.WINDOW_HEIGHT - self.__eheight
        if self.__pos_x < 0:
            self.__pos_x = 0
        if self.__pos_x > self.screen.WINDOW_WIDTH - self.__ewidth:
            self.__pos_x = self.screen.WINDOW_WIDTH - self.__ewidth
