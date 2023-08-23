from pygame.image import load
from entity.Entity import Entities
from entity.Entity import Direction

class Bullet(object):
    """bullets that will be drawn in the screen"""


    def __init__(self, screen, entity, direction, source):

        # TO-DO Move the source to the entity who sends the bullet
        self.__img = "assets/bullet.png" if source == Entities.HERO else "assets/enemy_bullet.png"
        self.__entity = load(self.__img)
        self.__eheight = self.__entity.get_rect().height
        self.__ewidth = self.__entity.get_rect().width
        self.screen = screen

        # TO-DO Move the direction to the entity who sends the bullet
        self.DIRECTION = direction
        self.y = entity.y
        self.__x = entity.x + entity.width / 2.4
        self.rect = self.__entity.get_rect(x=self.__x, y=self.y)
        

    def draw(self):

        self.rect = self.__entity.get_rect(x=self.__x, y=self.y)
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


