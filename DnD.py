import pygame
from pygame import * 

screen_x = 600 #custom screen size 
screen_y = 600 #custom screen size 

x_coordinate = 200
y_coordinate = 200

pygame.init()
screen = pygame.display.set_mode((screen_x,screen_y))
clicked = False


class OBJECTS():
    
    def __init__(self,image_directory):
        self.x = x_coordinate
        self.y = y_coordinate
        self.image = pygame.image.load(image_directory)
        self.create_object()
        
   
    def create_object(self): #displays image of self on the screen..
        screen.fill((255,255,255))
        screen.blit(self.image,(self.x,self.y))
        pygame.display.flip()
        

        
            
            
        
        


class EVENTS():
    
    def mouse_event(self,event_type,object,action):
        object_image = object.image
        if event_type == "HOVER":
            if object_image.get_rect().collidepoint(pygame.mouse.get_pos()):
                print ("mouse is over 'newGameButton'")
                
        if event_type == "CLICK":
            pass
        
        if event_type == "DRAG":
            pass
                
 
 
 
 
class BEHAVIOURS():
    
    def move_four_directions(object,SPEED): 
        global x_coordinate
        global y_coordinate
        keys_pressed = pygame.key.get_pressed()
        
        if keys_pressed[pygame.K_LEFT]:
            x_coordinate -= SPEED
            
        if keys_pressed[pygame.K_RIGHT]:
            x_coordinate += SPEED
            
        if keys_pressed[pygame.K_UP]:
            y_coordinate -= SPEED
            
        if keys_pressed[pygame.K_DOWN]:
            y_coordinate += SPEED
            
            
        
            
                
            
        
                
            

gameOn = True 

while gameOn:
    for event in pygame.event.get():
        if event.type == QUIT:
            gameOn = False
        aman = OBJECTS("Graphics/Icons/decor_2.png")
        BEHAVIOURS.move_four_directions(aman,100)  
             
    pygame.display.update()
    
pygame.quit()
    