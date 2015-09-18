import pygame


pygame.font.init()
UI_FONT = pygame.font.SysFont("monospace", 20)

class RifleTargetingSystem():
	def __init__(self):
		self.enemies_ = []
		self.target_tags_ = dict()

	def update(self, enemies):
		self.enemies_ = enemies

		for enemy in self.enemies_:
			if enemy.ID_ not in self.target_tags_:
					self.target_tags_[enemy.ID_] = self.new_word() 

	def draw_target_tags(self, screen):
		for enemy in self.enemies_:
			target_tag_word = self.target_tags_[enemy.ID_]
			target_tag_label = UI_FONT.render(target_tag_word, 1, enemy.colour_)
			# !!NEW!! Get target tag size and adjust coordinates of tag 	
			width = UI_FONT.size(target_tag_word)[0]
			screen.blit(target_tag_label, (enemy.position_[0] - (width/2),  
										  (enemy.position_[1] + enemy.size_/2)+10))
			
	def draw_terminal(self, screen):
		pass

	def new_word(self):
		return "TestTag"

class Rifle():
	def __init__(self):
		self.NAME_ = "Rifle"
		self.targeting_system = RifleTargetingSystem()

	def update(self, enemies):
		self.targeting_system.update(enemies)

	def draw(self, screen):
		self.targeting_system.draw_target_tags(screen)
		self.targeting_system.draw_terminal(screen)
