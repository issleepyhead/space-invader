from pygame.display import set_mode
from pygame.display import get_desktop_sizes
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
    
    _enemies = Group
    _players = Group
    _bullets = {
        'player_bullets' : Group(),
        'enemy_bullets'  : Group()
    }
    delta         = 0

    def __init__(self):
        init()
        screen_size = get_desktop_sizes()
        self.SCREEN = set_mode(screen_size[0])
        self.CLOCK = Clock()
        self.font = SysFont('segoeuibold', 24)
        set_caption("Space Invader")




