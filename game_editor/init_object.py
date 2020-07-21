import pygame

""" 

Initialise playable object from cutscene objects and declare important variables 
pertaining to system control

"""

class PLAYABLE_OBJECT:
    def __init__(self,name,sprite_directory):
        self.name = name 
        self.sprite_directory = sprite_directory 
        self.sprite = pygame.image.load(self.sprite_directory)
        self.x = 'NONE'
        self.y = 'NONE'
        self.initialise = False 
        
    def display_sprite(self,window):
        window.fill((255,255,255))
        window.blit(self.sprite,(self.x,self.y))
        pygame.display.flip()
        
        


cutscene_objects = ["Salvador", "Putin", "Godot"] # a dummy list to act as the collection of all cutscene objects 

onscreen_objects = [] # a list of all cutscene objects added to the screen
#whenever a cutscene_object is chosen from the UI, it gets converted into a playable_object which
#then appears on the screen. 






        
        
        
    