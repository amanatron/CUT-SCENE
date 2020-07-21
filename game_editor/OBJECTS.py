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
        self.x = 'NONE' #x coordinate of the image 
        self.y = 'NONE' #y coordinate of the image 
        self.initialise = False #boolean value to see if the object is already on screen or has just been added
        
    def display_sprite(self):
        window.fill((255,255,255))
        window.blit(self.sprite,(self.x,self.y))
        pygame.display.flip()
               
aman = OBJECT("aman","Graphics/Icons/godot.png") #create an object

object_inserted = aman #check to see which object has been inserted from the GUI list of objects
object_selected = "NONE" #check to see which object has been selected on screen 

def add_to_window(object_inserted): #function to add the selected object to the window list -- it checks whether the selected object already exists in the window list 
    if object_inserted not in objects_on_window:
        objects_on_window.append(object_inserted) 
        object_inserted.initialise = True 
    else:
        objects_on_window
        object_inserted.initialise = False
        
        
def move_four_directions(object,SPEED):
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_LEFT]:
        object.x -= SPEED
    if keys_pressed[pygame.K_RIGHT]:
        object.x += SPEED
        
    if keys_pressed[pygame.K_UP]:
        object.y -= SPEED
        
    if keys_pressed[pygame.K_DOWN]:
        object.y += SPEED
        
def bound_to_layout(object):
    
    sprite_width = object.sprite.get_width()
    sprite_height = object.sprite.get_height()

    if object.x < 0:
        object.x = 0
    elif object.x > screen_length - sprite_width:
        object.x = screen_length - sprite_width
    if object.y < 0:
        object.y = 0
    elif object.y > screen_height - sprite_height:
        object.y = screen_height - sprite_height
   
   
played = True
  
                
gameOn = True

while gameOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False        
        window.fill((255,255,255))
        
    if played == False:    
        add_to_window(object_inserted)
        
        for i in objects_on_window: #if object is inserted for the first time, it's initial position will be 200x200
            if i.initialise == True:
                i.x = 200
                i.y = 200
            
            i.display_sprite()
                
                
    if played == True: 
        add_to_window(object_inserted)
        
        for i in objects_on_window:
            if i.initialise == True: #only temporarily -- remove condition for played modes
                i.x = 200
                i.y = 200
            i.display_sprite() 
        
        
          
        bound_to_layout(aman)
        move_four_directions(aman,20)
        
        
        
        
        
        
        
    
                                
    pygame.display.update()
    

pygame.quit()
quit()
        
        
        

        
        
        
        
        