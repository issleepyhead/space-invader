from world.Entity import Entity
from random import randint
from pygame import (KEYDOWN, K_s, K_w, K_d, K_a, K_SPACE)
from pygame.key import get_pressed
from pygame.sprite import spritecollide

class PlayerEntity(Entity):

    _image_path = "assets/spaceship.png" # default image for the player
    _lives = 3                           # we will only have 3 lives for each players
    _player_id = None                    # unique identifier for the player
    _world = None

    def __init__(self, world):
        super(world, self._image_path)
        self._world = world
        self._player_id = str(randint(1000, 9999))

        # make it appear at the center
        self.x = self._world.WINDOW_WIDTH / 2 - (self.entity_width // 2)
        self.y = self._world.WINDOW_HEIGHT - (self.entity_height + 50)

    def move(self):
        # TODO change this implementation
        keys = get_pressed()
        if keys[K_w]:
            self.y -= 300 * self._world.delta
        if keys[K_s]:
            self.y += 300 * self._world.delta
        if keys[K_a]:
            self.x -= 300 * self._world.delta
        if keys[K_d]:
            self.x += 300 * self._world.delta
        if keys[K_SPACE]:
            self.fire()

    def dispose(self):
        pass

    def update(self):
        pass



