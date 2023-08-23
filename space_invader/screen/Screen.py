from pygame.display import set_mode
from pygame.image import load
from pygame.event import get
from pygame import QUIT
from pygame import quit
from pygame.display import update
from pygame import init
from pygame.display import set_icon
from pygame.display import set_caption
from pygame.sprite import Sprite
from pygame.surface import Surface
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
    __HOSTING = False
    __CLIENTS = 0

    # declared them private because I don't want to re-assign them somewhere
    __enemies = []
    __players = []
    __bullets = []
    __enemy_bullets = []

    delta = 0
    mil = 0


    def __init__(self, width=1000, height=800):
        self.WINDOW_WIDTH = width
        self.WINDOW_HEIGHT = height
        self.__background = load(self.__bg_img)
        self.__icon = load(self.__ic)
        self.SCREEN = set_mode((width, height))
        self.CLOCK = Clock()
        set_caption("Space Invader")
        set_icon(self.__icon)
        self.start_game()

    def start_game(self):
        self.__enemies.clear()
        self.__bullets.clear()
        self.__enemy_bullets.clear()

        self.player = PlayerEntity(self)
        self.__enemies.append(EnemyEntity(self))
        self.__enemies.append(EnemyEntity(self))
        self.__enemies.append(EnemyEntity(self))
        self.__enemies.append(EnemyEntity(self))

    # when a player joins the game
    def join_game(self):
        pass

    def refesh_rate(self):
        update()
        self.delta = self.CLOCK.tick(60) / 500

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

        # draw every player(s) in the screen
        # for player in self.__players:
        #    player.draw()
        #    player.move()
        self.player.draw()
        self.player.move()

        # draw every bullets in the screen
        for bullet in self.__bullets:
            bullet.draw()

        # draw every enemy in the screen
        for enemy in self.__enemies:
            enemy.draw()

        # draw every enemy bullets in the screen
        for bullet in self.__enemy_bullets:
            bullet.draw()

    @property
    def bullets(self):
        return self.__bullets

    @property
    def enemy_bullets(self):
        return self.__enemy_bullets

    @property
    def enemies(self):
        return self.__enemies

        
