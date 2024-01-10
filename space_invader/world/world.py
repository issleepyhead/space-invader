from pygame.display import set_mode
from pygame.image import load
from pygame.event import get
from pygame import QUITs
from pygame import quit
from pygame.display import update
from pygame import init
from pygame.display import set_icon
from pygame.display import set_caption
from pygame.font import SysFont
from pygame.sprite import Group
from pygame.time import Clock

class World(object):
    
    _enemies = []
    _players = []
    _bullets = {
        'player_bullets' : [],
        'enemy_bullets'  : []
    }

    WINDOW_HEIGHT = 800
    WINDOW_WIDTH  = 1000
    delta         = 0

    def __init__(self):
        init()
        self.SCREEN = set_mode((width, height))
        self.CLOCK = Clock()
        self.font = SysFont('segoeuibold', 24)
        set_caption("Space Invader")




