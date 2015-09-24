import pygame

from gameobject import GameObject


class BasicGrunt(GameObject):

    def __init__(self, starting_position, universe):
        self.position_ = starting_position
        self.ID_ = self.create_ID()
        self.size_ = 15
        self.speed_ = 0.3
        self.universe_ = universe   

    def update(self, events):
        # Calculates shit
        main_character_position = self.universe_.main_character().position_
        x_distance = main_character_position[0] - self.position_[0]
        y_distance = main_character_position[1] - self.position_[1]
        distance = (x_distance**2 + y_distance**2)**(1/2)
        
 
        # Outside range
        if distance > 400:
            self.position_ = (self.position_[0], self.position_[1]+self.speed_)
        #if distance <= 400:
            #self.position_ = (self.position_[0]+self.speed_, self.position_[1]+self.speed_) funny
        
        elif distance >= 100:
            x_velocity = (x_distance * self.speed_) / distance
            y_velocity = (y_distance * self.speed_) / distance
            self.position_ = (self.position_[0]+x_velocity, self.position_[1]+y_velocity) 
        else:
            self.position_ = (self.position_[0], self.position_[1])
        


        
    def collision_box(self):
    	return pygame.Rect(self.position_[0]-self.size_/2,
        			       self.position_[1]-self.size_/2,
        			       self.size_, self.size_)
