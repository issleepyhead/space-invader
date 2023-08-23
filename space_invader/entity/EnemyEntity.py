from entity.Entity import Entity
from entity.Entity import Entities
from entity.Entity import Direction
from entity.Bullet import Bullet
from random import randint as rand
from pygame.image import load

class EnemyEntity(Entity):
    """Enemy class for the game THE BAD GUYS THAT LOOKS PRETTY GOOD"""

    __images = [load("assets/enemy_blue.png"), load("assets/enemy_white.png")]
    __explosion_w = __explosion_h = 256
    __explosion = load("assets/explosion.png")
    is_alive = True

    def __init__(self, screen):
        self.screen = screen
        self.idx = rand(0, len(self.__images)-1)
        self.__entity = self.__images[self.idx]
        self.__eheight = self.__entity.get_rect().height
        self.__ewidth = self.__entity.get_rect().width
        
        # random position
        self.__pos_x = rand(0, self.screen.WINDOW_WIDTH - self.__ewidth)
        self.__pos_y = -128 # we don't want the entity to appear right away.
        self.fire()

    @property
    def y(self):
        return self.__pos_y

    def fire(self):
        if len(self.screen.enemy_bullets) < 100:
            bullet = Bullet(self.screen, self, Direction.DOWN, Entities.ENEMY)
            self.screen.enemy_bullets.append(bullet)

    def draw(self):
        self.rect = self.__entity.get_rect(x=self.__pos_x, y=self.__pos_y)

        if not self.is_alive:
            self.screen.enemies.remove(self)
            return
        
        bullets_rect = [bullet.rect for bullet in self.screen.bullets]
        collision = self.rect.collidelistall(bullets_rect)
        if collision:
            for bullet in collision:
                del self.screen.bullets[bullet]
            self.screen.SCREEN.blit(self.__explosion, (self.__pos_x - self.__explosion_w // 3, self.__pos_y - self.__explosion_h // 3))
            self.is_alive = not self.is_alive
            return
            

        # check if we are off the edge
        if self.y > self.screen.WINDOW_HEIGHT:
            self.screen.enemies.remove(self)
            return

        self.__pos_y += 25 * self.screen.delta
        self.screen.SCREEN.blit(self.__entity, (self.__pos_x, self.__pos_y))

    def explode(self):
        pass

    @property
    def x(self):
        return self.__pos_x

    @property
    def y(self):
        return self.__pos_y

    @property
    def width(self):
        return self.__ewidth

    @property
    def height(self):
        return self.__eheight


