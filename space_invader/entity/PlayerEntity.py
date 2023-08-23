from pygame.image import load
from pygame import (KEYDOWN, K_s, K_w, K_d, K_a, K_SPACE)
from pygame.key import get_pressed
from pygame.draw import rect
from pygame import Rect
from entity.Entity import Entity
from entity.Bullet import Bullet
from entity.Entity import Entities
from entity.Entity import Direction

class PlayerEntity(Entity):
    """A PlayerEntity class for every player in the game"""

    __player_img = "assets/spaceship.png"
    __explosion_img = "assets/explosion.png"
    __lives   = 3
    __explosion_w = __explosion_h = 256

    def __init__(self, screen):
        self.screen = screen
        self.__entity = load(self.__player_img)
        self.__explosion = load(self.__explosion_img)
        self.__eheight = self.__entity.get_rect().height
        self.__ewidth = self.__entity.get_rect().width
        self.rect = self.__entity.get_rect()

        # make it appear in center
        self.__pos_x = self.screen.WINDOW_WIDTH / 2 - (self.__ewidth // 2)
        self.__pos_y = self.screen.WINDOW_HEIGHT - (self.__eheight + 50)

    def draw(self):
        # TO-DO check if there's a collisions.
        self.rect = self.__entity.get_rect(x=self.__pos_x, y=self.__pos_y)
        

        if self.__lives == 0:
            self.screen.start_game()
        
        bullets_rect = [bullet.rect for bullet in self.screen.enemy_bullets]
        if self.rect.collidelistall(bullets_rect):
            self.screen.SCREEN.blit(self.__explosion, (self.__pos_x - self.__explosion_w // 3, self.__pos_y - self.__explosion_h // 3))
            self.__lives -= 1
            return

        self.screen.SCREEN.blit(self.__entity, (self.__pos_x, self.__pos_y))

    def fire(self):
        # we can only fire 20 bullets, if the bullet is off the edge we remove it
        if len(self.screen.bullets) < 20:
            bullet = Bullet(self.screen, self, Direction.UP, Entities.HERO)
            self.screen.bullets.append(bullet)

    def move(self):
        keys = get_pressed()
        if keys[K_w]:
            self.__pos_y -= 100 * self.screen.delta
        if keys[K_s]:
            self.__pos_y += 100 * self.screen.delta
        if keys[K_a]:
            self.__pos_x -= 100 * self.screen.delta
        if keys[K_d]:
            self.__pos_x += 100 * self.screen.delta
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

    @property
    def y(self):
        return self.__pos_y

    @property
    def x(self):
        return self.__pos_x

    @property
    def height(self):
        return self.__eheight

    @property
    def width(self):
        return self.__ewidth
