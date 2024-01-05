
from entity.Entity import Entities
from entity.Entity import Direction
from entity.Bullet import Bullet
from pygame.sprite import Sprite
from pygame.sprite import spritecollide
from pygame.draw import rect
from random import randint as rand
from pygame.image import load

class EnemyEntity(Sprite):
    """Enemy class for the game THE BAD GUYS THAT LOOK PRETTY GOOD"""
    

    def __init__(self, screen):
        #self.screen = screen
        Sprite.__init__(self)
        self.screen = screen
        self.__images = [load("assets/enemy_blue.png"), load("assets/enemy_white.png")]
        self.idx = rand(0, len(self.__images)-1)

        # TODO fix the images don't randomize it.
        self.image = self.__images[self.idx]
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        
        # random position
        self.x = rand(0, self.screen.WINDOW_WIDTH - self.width)
        self.y = -(-self.height) # we don't want the entity to appear right away.
        
        
        self.__explosion = load("assets/explosion.png")
        self.__explosion_w = self.__explosion.get_rect().width
        self.__explosion_h = self.__explosion.get_rect().height

        self.counter = 0
        self.bullet_img = "assets/enemy_bullet.png"
        self.is_alive = True
        
        
        
        self.rect = self.image.get_rect(x=self.x, y=-self.y)
        self.fire()


    def fire(self):
        bullet = Bullet(self.screen, self, Direction.DOWN)
        self.screen.enemy_bullets.add(bullet)

    def update(self):
        if self.is_alive:
            self.rect.move_ip(0, 1)
            if self.rect.bottom > self.screen.WINDOW_HEIGHT:
                self.kill()
            if spritecollide(self, self.screen.bullets, True):
                self.image = self.__explosion
                self.rect = self.image.get_rect(x=self.rect.x - self.__explosion_w // 3, y=self.rect.y - self.__explosion_h // 3)
                self.is_alive = False

        # wtf is MAXCOUNT?
        MAX_COUNT = 3
        if not self.is_alive and self.counter <= MAX_COUNT:
            self.counter += 1
        
        if self.counter > MAX_COUNT:
            self.kill()