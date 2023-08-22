from entity.Entity import Entity
from entity.Entity import Entities
from entity.Entity import Direction
from entity.Bullet import Bullet
from random import randint as rand
from pygame.image import load

class EnemyEntity(Entity):
    """Enemy class for the game THE BAD GUYS THAT LOOKS PRETTY GOOD"""

    __ewidth = __eheight = 128
    __enemy_entity = [load("assets/enemy_blue.png"), load("assets/enemy_white.png")]
    __explosion_w = __explosion_h = 256
    __explosion = load("assets/explosion.png")
    is_alive = True

    def __init__(self, screen):
        self.screen = screen
        self.__entity = self.__enemy_entity[rand(0, 1)]
        
        # random position
        self.__pos_x = rand(0, self.screen.WINDOW_WIDTH - self.__ewidth)
        self.__pos_y = -128 # we don't want the entity to appear right away.
        self.fire()

    @property
    def y(self):
        return self.__pos_y

    def fire(self):
        if len(self.screen.enemy_bullets) < 100:
            bullet = Bullet(self.screen, self.__pos_x, self.__pos_y + self.__eheight, Direction.DOWN, Entities.ENEMY)
            self.screen.enemy_bullets.append(bullet)

    def draw(self):
        # check if there's a collision
        self.rect = self.__entity.get_rect(x=self.__pos_x, y=self.__pos_y)

        if not self.is_alive:
            self.screen.enemies.remove(self)
            return
        
        bullets_rect = [bullet.rect for bullet in self.screen.bullets]
        if self.rect.collidelistall(bullets_rect):
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


