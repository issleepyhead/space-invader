from enum import Enum
from pygame.image import load

class Direction(Enum):
    UP = 1
    DOWN = 2

class Bullet(object):
    """bullets that will be drawn in the screen"""

    __ewith   = 64
    __eheight = 55

    def __init__(self, screen, x, y, direction:Direction):
        self.__img = "assets/bullet.png"
        self.__entity = load(self.__img)
        self.screen = screen
        self.DIRECTION = direction
        self.y = y 
        self.__x = x + self.__ewith / 2

    def draw(self):
        if self.DIRECTION.UP:
            self.y -= 200 * self.screen.delta
        else:
            self.y += 200 * self.screen.delta
        self.screen.SCREEN.blit(self.__entity, (self.__x, self.y))


