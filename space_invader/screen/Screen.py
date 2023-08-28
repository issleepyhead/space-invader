from pygame.display import set_mode
from pygame.image import load
from pygame.event import get
from pygame import QUIT
from pygame import quit
from pygame.display import update
from pygame import init
from pygame.display import set_icon
from pygame.display import set_caption
from pygame.font import SysFont
from pygame.sprite import Group
from pygame.time import Clock
from entity.Entity import Direction
from entity.PlayerEntity import PlayerEntity
from entity.EnemyEntity import EnemyEntity


class Screen:
    """
    Main screen of the game
    """

    __bg_img = "assets/space_background.png"
    __ic     = "assets/icon.png"
    __CLIENTS_PLAYES = []

    # declared them private because I don't want to re-assign them somewhere
    enemies = Group()
    bullets = Group()
    enemy_bullets = Group()
    

    delta = 0

    WINDOW_WIDTH = 0
    WINDOW_HEIGHT = 0

    def __init__(self, width=1000, height=800):
        init()
        self.WINDOW_WIDTH = width
        self.WINDOW_HEIGHT = height
        self.__background = load(self.__bg_img)
        self.__icon = load(self.__ic)
        self.SCREEN = set_mode((width, height))
        self.CLOCK = Clock()
        self.font = SysFont('segoeuibold', 24)
        set_caption("Space Invader")
        set_icon(self.__icon)
        self.start_game()

    def start_game(self):

        self.player = PlayerEntity(self)
        self.enemies.add(EnemyEntity(self))
        self.enemies.add(EnemyEntity(self))
        self.enemies.add(EnemyEntity(self))
        self.enemies.add(EnemyEntity(self))

    # when a player joins the game
    def join_game(self):
        pass

    def refesh_rate(self):
        self.delta = self.CLOCK.tick(60) / 1000
        update()

    def events_listener(self):
        for event in get():
            if event.type == QUIT:
                return False
           
        return True
                
    def run(self):
        # game loop
        while self.events_listener():
            self.draw()
            self.refesh_rate()
        quit()
            

    def draw(self, color=(255, 255, 255)):

        # first draw the background before anything else
        self.SCREEN.fill(color)
        self.SCREEN.blit(self.__background, (0, 0))

        self.player.update()
        self.player.draw()

        # draw bullets in the screen
        self.bullets.update()
        self.bullets.draw(self.SCREEN)

        # draw enemy bullets in the screen
        self.enemy_bullets.update()
        self.enemy_bullets.draw(self.SCREEN)

        # draw every enemy in the screen
        self.enemies.update()
        self.enemies.draw(self.SCREEN)


        
