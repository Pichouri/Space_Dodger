import pygame, random, math
from pygame.locals import *
pygame.init()

mul_score = 0

class Projectile_Template:
    def __init__(self,score,width):
        #Modifiable:
        self.img = pygame.image.load("images/projectiles/Rock5.png").convert_alpha()

        # Initialisation
        mul_score = score/100  
        self.img.set_colorkey((255,255,255))
        self.speed = [0,1+mul_score]
        self.rect = self.img.get_rect()
        self.rect.x = random.randint(5,width-5)
        self.rect.y = -20
        self.xsave = self.rect.x
    
    def traj(temp): 
         # fonction qui reçoit la coordonnée y pour y retourner la coordonnée x
        y = temp.rect.y
        return int(math.cos(y/20)*(50+mul_score))

#Celui la m'énerve, je n'arrive pas à lui donner la trajectoire que je veut
class Projectile_1: 
    def __init__(self,score,width):
        #Modifiable:
        self.img = pygame.image.load("images/projectiles/Rock2.png").convert_alpha()

        # Initialisation
        mul_score = score/100  
        self.img.set_colorkey((255,255,255))
        self.speed = [0,2+mul_score]
        self.rect = self.img.get_rect()
        self.rect.x = random.randint(0,width)
        self.rect.y = -40
        self.xsave = self.rect.x
        if random.randint(0, 1) == 1:
            self.ipos = 1
        else:
            self.ipos = -1
    
    def traj(temp): 
         # fonction qui reçoit la coordonnée y pour y retourner la coordonnée x
        y = temp.rect.y
        return y/2*temp.ipos


class Projectile_2:

    def __init__(self,score,width):
        #Modifiable:
        self.img = pygame.image.load("images/projectiles/Rock3.png").convert_alpha()

        # Initialisation
        mul_score = score/100  
        self.img.set_colorkey((255,255,255))
        self.speed = [0,2+mul_score]
        self.rect = self.img.get_rect()
        self.rect.x = random.randint(5,width-5)
        self.rect.y = -150
        self.xsave = self.rect.x
    
    def traj(temp): 
         # fonction qui reçoit la coordonnée y pour y retourner la coordonnée x
        return 0

class Projectile_3: 
    def __init__(self,score,width):
        #Modifiable:
        self.img = pygame.image.load("images/projectiles/Rock4.png").convert_alpha()

        # Initialisation
        mul_score = score/100  
        self.img.set_colorkey((255,255,255))
        self.speed = [0,2+mul_score]
        self.rect = self.img.get_rect()
        self.rect.x = random.randint(0,width)
        self.rect.y = -40
        self.xsave = self.rect.x
        if random.randint(0, 1) == 1:
            self.ipos = 1
        else:
            self.ipos = -1
    
    def traj(temp): 
         # fonction qui reçoit la coordonnée y pour y retourner la coordonnée x
        y = temp.rect.y
        return 200*math.exp(-((y-400)**2)/(2*200**2))*temp.ipos