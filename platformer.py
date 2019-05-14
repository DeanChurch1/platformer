#Platformer
#Dean

import pygame as pg
import random
from settings import *
from sprites import *

class Game:
    def __init__(self):
        pass


    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.run()


    def run(self):
        pass


    def update(self):
        pass

        

    def events(self):
        pass
        


    def draw(self):
        pass


    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass


g = Game()


