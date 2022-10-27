import pygame, random
from pygame.locals import *
pygame.init()

class backstar_1(): # Génération d'étoile à mouvement chaotique unidirectionnel
    def __init__(self,width) -> None:
        self.img = pygame.image.load("images/deco/star"+str(random.randint(1,4))+".png").convert_alpha()
        self.rect = self.img.get_rect()
        self.rect.x = random.randint(5,width-5)
        self.rect.y = -5
        self.speed = [0,random.randint(1,3)]

class planet(): # Génération de planète à mouvement chaotique unidirectionnel
    def __init__(self,width) -> None:
        self.img = pygame.image.load("images/deco/planet"+str(random.randint(1,7))+".png").convert_alpha()
        self.rect = self.img.get_rect()
        self.rect.x = random.randint(5,width-5)
        self.rect.y = -80
        self.speed = [0,random.randint(1,2)]
