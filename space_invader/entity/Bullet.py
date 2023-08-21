from pygame.image import load
from entity.Entity import Entities
from entity.Entity import Direction

class Bullet(object):
    """bullets that will be drawn in the screen"""

    __ewith   = 64
    __eheight = 55

    def __init__(self, screen, x, y, direction, source):
        self.__img = "assets/bullet.png" if source == Entities.HERO else "assets/enemy_bullet.png"
        self.__entity = load(self.__img)
        self.rect = self.__entity.get_rect()
        self.screen = screen
        self.DIRECTION = direction
        self.y = y 
        self.__x = x + self.__ewith / 2

    def draw(self):
        if self.DIRECTION == Direction.UP:
            self.y -= 200 * self.screen.delta
        else:
            self.y += 50 * self.screen.delta
        self.screen.SCREEN.blit(self.__entity, (self.__x, self.y))


