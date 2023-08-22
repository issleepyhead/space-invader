from pygame.image import load
from entity.Entity import Entities
from entity.Entity import Direction

class Bullet(object):
    """bullets that will be drawn in the screen"""

    __ewidth   = 64
    __eheight = 55

    def __init__(self, screen, x, y, direction, source):
        self.__img = "assets/bullet.png" if source == Entities.HERO else "assets/enemy_bullet.png"
        self.__entity = load(self.__img)
        self.screen = screen
        self.DIRECTION = direction
        self.y = y 
        self.__x = x + self.__ewidth / 2
        self.rect = self.__entity.get_rect(x=self.__x, y=self.y)
        

    def draw(self):
        # TO-DO check if there's a collision
        self.rect = self.__entity.get_rect(x=self.__x - self.__ewidth // 3, y=self.y - self.__eheight // 3)

        if self.DIRECTION == Direction.UP:
            # check if we are off the edge
            if self.y < 0 and self.DIRECTION == Direction.UP:
                self.screen.bullets.remove(self)
                return
            self.y -= 200 * self.screen.delta
        else:
            # check if we are off the edge
            if self.y > self.screen.WINDOW_HEIGHT and self.DIRECTION == Direction.DOWN:
                self.screen.enemy_bullets.remove(self)
                return
            self.y += 50 * self.screen.delta
        self.screen.SCREEN.blit(self.__entity, (self.__x, self.y))


