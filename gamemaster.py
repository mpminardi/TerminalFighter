import random

import pygame

from basic_grunt import BasicGrunt
from maincharacter import MainCharacter
from not_so_basic_grunt import NotSoBasicGrunt


class GameMaster():

    def __init__(self, universe, DRAWING_SCALE):
        self.universe_ = universe
        self.DRAWING_SCALE_ = DRAWING_SCALE

        self.spawn_delay_ = 200
        self.spawn_timer_ = 199
        self.enemy_x_spawn_locations = [x/100 for x in range(10, 90)] 
        self.main_character_spawn_height_ = self.universe_.height_*0.9
        self.spawn_main_character()

        self.spawn_difficulty_ = 0.1
        self.minimum_spawn_delay_ = 19 

    def draw(self, screen):
        self.universe_.main_character_.draw_view(screen)
        self.universe_.main_character_.draw_ui(screen)

    def spawn_main_character(self):
        starting_position = [
            self.universe_.width_/2, self.main_character_spawn_height_]
        the_main_character = MainCharacter(
            starting_position, self.universe_, self.DRAWING_SCALE_)
        self.universe_.create_main_character(the_main_character)

    def spawn_basic_grunt(self):
        starting_position = [self.universe_.width_*random.choice(self.enemy_x_spawn_locations), 0]
        the_basic_grunt = BasicGrunt(starting_position, self.universe_)
        self.universe_.create_enemy(the_basic_grunt)

    def spawn_not_so_basic_grunt(self):
        starting_position = [self.universe_.width_*random.choice(self.enemy_x_spawn_locations), 0]
        not_so_basic_grunt = NotSoBasicGrunt(starting_position, self.universe_)
        self.universe_.create_enemy(not_so_basic_grunt)

    def update(self, events):
        self.spawn_timer_ += 1
        
        if self.spawn_delay_ > self.minimum_spawn_delay_: 
            self.spawn_delay_ -= self.spawn_difficulty_ 
            if self.spawn_delay_ < self.minimum_spawn_delay_:
                self.spawn_delay_ = self.minimum_spawn_delay_
        
        if self.spawn_timer_ > self.spawn_delay_:
            self.spawn_not_so_basic_grunt()
            self.spawn_basic_grunt()
            self.spawn_timer_ = 0
             
        self.universe_.update(events)
