from pygame.sprite import Sprite
from abc import ABC, abstractmethod
from pygame.image import load
from pygame.sprite import Sprite


class Entity(Sprite, ABC):

    x          = 0
    y          = 0

    def __init__(self, world, image_path):
        self.world = world
        self.image = load(image_path)

        self.entity_height = self.image.get_rect().height
        self.entity_width = self.image.get_rect().width
        self.entity_rect = self.image.get_rect()

    def draw(self):
        # TODO change this implementation
        self.world.SCREEN.blit(self.image, (self.x, self.y))


    @abstractmethod
    def move(self):
        '''
        Defines how entity should move across the screen.
        '''
        pass

    @abstractmethod
    def dispose(self):
        '''
        Defines how to dispose the entity.
        '''
        pass

    @abstractmethod
    def update(self):
        '''
        Update the visual of the entity in the screen.
        '''
        pass



