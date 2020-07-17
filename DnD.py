import pygame
from pygame import * 

screen_x = 600 #value that can be inserted by the player upon choosing mechanic
screen_y = 600 #value that can be inserted by the player upon choosing mechanic

pygame.init()
screen = pygame.display.set_mode((screen_x,screen_y))

class OBJECTS():
    def __init__(self,name,image_directory,issolid,istemp):
        self.name = name
        self.image = pygame.image.load(image_directory)
        self.issolid = False
        self.isstemp = False
        
    def create_object(self):
        screen.blit(self.image,(0,0))
        


class EVENTS():
    
    def mouse_event(self,event_type,object,action):
        object_image = object.image
        if event_type == "HOVER":
            if object_image.get_rect().collidepoint(pygame.mouse.get_pos()):
                print ("mouse is over 'newGameButton'")
            

gameOn = True 

while gameOn:
    for event in pygame.event.get():
        if event.type == QUIT:
            gameOn = False
        aman = OBJECTS("ICON","Graphics/Icons/act.png",False,False)
        aman.create_object()
        

pygame.quit()
    