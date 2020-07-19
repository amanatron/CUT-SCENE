import pygame 
from pygame import *

screen_length = 800
screen_height = 600

window = pygame.display.set_mode((screen_length,screen_height)) 
objects_on_window = []

class OBJECT:
    def __init__(self,name,sprite_directory):
        self.name = name
        self.sprite_directory = sprite_directory
        self.sprite = pygame.image.load(self.sprite_directory)
        self.x = "NONE"
        self.y = "NONE"
        self.initialise = False #boolean value to see if the object is already on screen or has just been added
        
    def display_sprite(self):
        window.blit(self.sprite,(self.x,self.y))
        pygame.display.flip()
               
aman = OBJECT("aman","Graphics/Icons/godot.png") #create an object

object_inserted = aman
object_selected = "NONE"

def add_to_window(object_inserted):
    if object_inserted not in objects_on_window:
        objects_on_window.append(object_inserted) 
        object_inserted.initialise = True 
    else:
        objects_on_window
        object_inserted.initialise = False
    
 
    
           
               
gameOn = True

while gameOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False        
        window.fill((255,255,255))
        
    add_to_window(object_inserted)
        
        
    for i in objects_on_window: #if object is inserted for the first time, it's initial position will be 200x200
        if i.initialise == True:
            i.x = 200
            i.y = 200
            
        i.display_sprite()
        
        
        
        
        
        
        
    
                                
    pygame.display.update()
    

pygame.quit()
quit()
        
        
        

        
        
        
        
        