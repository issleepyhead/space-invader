from pygame.image import load
from pygame.sprite import Sprite
from entity.Entity import Entities
from entity.Entity import Direction

class Bullet(Sprite):
    """bullets that will be drawn in the screen"""

    def __init__(self, screen, entity, direction):
        Sprite.__init__(self)
        self.__img = entity.bullet_img
        self.image = load(self.__img)
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        self.screen = screen

        self.DIRECTION = direction
        self.y = entity.y
        self.x = entity.x + entity.width // 2 - self.width // 2
        self.rect = self.image.get_rect(x=self.x, y=self.y)
        
    def update(self):
        if self.rect.top < 0 and self.DIRECTION == Direction.UP:
            self.kill()
        elif self.rect.bottom > self.screen.WINDOW_HEIGHT:
            self.kill()

        if self.DIRECTION == Direction.UP:
            self.rect.move_ip(0, -5)
        else:
            self.rect.move_ip(0, 2)


