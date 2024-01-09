from pygame import (KEYDOWN, K_s, K_w, K_d, K_a, K_SPACE)
from pygame.image import load
from pygame.key import get_pressed
from pygame.draw import rect
from pygame.sprite import spritecollide
from pygame.sprite import Sprite
from entity.Bullet import Bullet
from entity.Entity import Entities
from entity.Entity import Direction

class PlayerEntity(Sprite):
    """A PlayerEntity class for every player in the game"""


    def __init__(self, screen):
        self.screen = screen
        self.image_path = "assets/spaceship.png"
        self.explosion_img = "assets/explosion.png"
        self.bullet_img = "assets/bullet.png"
        self.lives   = 3
        self.explosion_w = self.explosion_h = 256
        self.image = load(self.image_path)
        self.explosion = load(self.explosion_img)

        self.height = self.image.get_rect().height
        self.width = self.image.get_rect().width
        self.rect = self.image.get_rect()
        

        # make it appear at the center
        self.x = self.screen.WINDOW_WIDTH / 2 - (self.width // 2)
        self.y = self.screen.WINDOW_HEIGHT - (self.height + 50)

    def update(self):
        self.rect = self.image.get_rect(x=self.x, y=self.y) 

        if self.lives == 0:
            self.screen.start_game()
            return
        
        self.move()

        # player bounds
        if self.rect.top < 0:
            self.y = 0
        if self.rect.top > self.screen.WINDOW_HEIGHT - self.height:
            self.y = self.screen.WINDOW_HEIGHT - self.height
        if self.rect.left < 0:
            self.x = 0
        if self.rect.left > self.screen.WINDOW_WIDTH - self.width:
            self.x = self.screen.WINDOW_WIDTH - self.width


        if spritecollide(self, self.screen.enemy_bullets, True):
            self.rect = self.image.get_rect(x=self.rect.x - self.explosion_w // 2 + self.width // 2, y=self.rect.y - self.explosion_h // 2 + self.height // 2)
            self.lives -= 1

        self.player_name()
        
    def draw(self):
        self.screen.SCREEN.blit(self.image, (self.x, self.y))

    def fire(self):
        # we can only fire 20 bullets, and if the bullet is off the edge we remove it
        if len(self.screen.bullets) < 20:
            bullet = Bullet(self.screen, self, Direction.UP)
            self.screen.bullets.add(bullet)

    def move(self):
        keys = get_pressed()
        if keys[K_w]:
            self.y -= 300 * self.screen.delta
        if keys[K_s]:
            self.y += 300 * self.screen.delta
        if keys[K_a]:
            self.x -= 300 * self.screen.delta
        if keys[K_d]:
            self.x += 300 * self.screen.delta
        if keys[K_SPACE]:
            self.fire()

        

    def player_name(self):
        text = self.screen.font.render('Clancy', True, (0, 255, 0))
        width = text.get_rect().width
        self.screen.SCREEN.blit(text, (self.x - width // 2 + self.width // 2, self.y + self.height))

