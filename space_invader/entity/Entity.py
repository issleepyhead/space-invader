from abc import ABC, abstractmethod

class Entity(ABC):
    """
    Base class for every entities in the game.
    """

    @abstractmethod
    def draw(self):
        """
        Draw the entity on the screen
        """
        pass

    @abstractmethod
    def fire(self):
        """
        Draw the bullets on the screen
        """
        pass


