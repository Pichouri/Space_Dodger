from re import A
import pygame, random, math
from pygame.locals import *
pygame.init()

lifetime = 5000 # Durée de vie des projectiles spéciaux

def distance(x1,x2,y1,y2): # fonction qui retourne la distance entre deux points x et y 2D
    return int(math.sqrt((x2-x1)**2+(y2-y1)**2))

def distance_x(x1,x2): # fonction qui retourne la distance entre deux points x 1D
    return int(math.sqrt((x2-x1)**2))

def distance_y(y1,y2): # fonction qui retourne la distance entre deux points y 1D
    return int(math.sqrt((y2-y1)**2))

def wheretogo(x1,x2,y1,y2): # fonction qui retourne la meilleure trajectoire afin de rejoindre les coordonnée x2,y2 , retourne des variables de déplacement x ou y
    if distance_x(x1,x2) > distance_y(y1,y2): 
        if x1-x2 > 0:
            return [-1,0]
        else:
            return [1,0]
    else:
        if y1-y2 > 0:
            return [0,-1]
        else:
            return [0,1]

def blackholesuck(x1,x2,y1,y2,attra): # fonction qui imite l'effet d'aspiration du trou noir à partir de la coordonnée du trou noir et de la force d'attraction, retourne des variables de déplacements
    x2+=25
    y2+=25
    if distance_x(x1,x2) < attra/2 and distance_y(y1,y2) < attra/2:
        tempBHM = wheretogoboth(x1,x2,y1,y2)
        tempBHM[0]*=1.5
        tempBHM[1]*=1.5
        return tempBHM
    elif distance_x(x1,x2) < attra and distance_y(y1,y2) < attra:
        return wheretogoboth(x1,x2,y1,y2)
    else:
        return [0,0]




def wheretogoboth(x1,x2,y1,y2): # fonction qui retourne la meilleure trajectoire afin de rejoindre les coordonnée x2,y2 , retourne des variables de déplacement x et y
    tempvit = [0,0]
    if x1-x2 > 0:
        tempvit[0]=-1
    else:
        tempvit[0]=1
    if y1-y2 > 0:
        tempvit[1]=-1
    else:
        tempvit[1]=1
    return tempvit
    

class adv_proj_1: # Mouvement suivi non standard pour troubler le joueur
    def __init__(self,width):
        self.img = pygame.image.load("images/projectiles/Rock.png").convert_alpha()
        self.rect = self.img.get_rect()
        self.rect.x = random.randint(5,width-5)
        self.rect.y = -80
        self.sx = 0
        self.sy = 0
        self.time = lifetime
    
    def traj(self): #fonction qui retourne les deux coordonnées x et y pour la trajectoire de notre projectile
        return wheretogo(self.rect.x,self.sx,self.rect.y,self.sy)

class adv_proj_2: # Mouvement suivi non standard pour troubler le joueur
    def __init__(self,width):
        self.img = pygame.image.load("images/projectiles/Rock.png").convert_alpha()
        self.rect = self.img.get_rect()
        self.rect.x = random.randint(5,width-5)
        self.rect.y = -80
        self.sx = 0
        self.sy = 0
        self.time = lifetime
    
    def traj(self): #fonction qui retourne les deux coordonnées x et y pour la trajectoire de notre projectile
        move_2d = wheretogoboth(self.rect.x,self.sx,self.rect.y,self.sy)
        return move_2d

class adv_proj_3: 
    def __init__(self,width):
        self.img = pygame.image.load("images/projectiles/Rock.png").convert_alpha()
        self.rect = self.img.get_rect()
        self.rect.x = -80
        self.rect.y = random.randint(0,400)
        self.sx = 0
        self.sy = 0
        self.time = lifetime
    
    def traj(self): #fonction la coordonnées x pour notre projectile
        move_2d = wheretogoboth(self.rect.x,self.sx,self.rect.y,self.sy)
        move_2d[1]=0
        return move_2d

class adv_proj_4: 
    def __init__(self,width):
        self.img = pygame.image.load("images/projectiles/Rock.png").convert_alpha()
        self.rect = self.img.get_rect()
        self.rect.x = random.randint(0,width)
        self.rect.y = -80
        self.sx = 0
        self.sy = 0
        self.time = lifetime
    
    def traj(self): #fonction la coordonnées y pour notre projectile
        move_2d = wheretogoboth(self.rect.x,self.sx,self.rect.y,self.sy)
        move_2d[0]=0
        return move_2d


class black_hole: # Aspire légèrement le vaisseau
    def __init__(self,width):
        self.img = pygame.image.load("images/projectiles/black_hole.png").convert_alpha()
        self.rect = self.img.get_rect()
        self.rect.x = random.randint(5,width-5)
        self.rect.y = 400
    
    def traj(self): #fonction qui retourne la coordonnée y = 0.01 pour faire lentement quitter l'écran au trou noir
        return [0,0.1]
        






