from pygame.locals import *

def colli_test(rect1,Lrect): #Fonction pour tester la collision entre deux rectangulaire, retourne True si les deux se touche
    for rect2 in Lrect:
        if rect1.colliderect(rect2.rect):
            return True
    return False

def backgroundstar_create():
    pass