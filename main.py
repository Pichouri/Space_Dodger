# Importation de toutes les libs utilisés
from pygame.locals import *
import pygame as py
import Projectile as pro
import star as st
import func as fu
import random
import math
import speproj as infi

# Constante
max_y = 500
max_x = 800
vx = 0
vy = 0
fps = 288  # action par seconde
dpp = 1  # deplacement par pixel
player = "images/player.png"  # récupération du skin de base vaisseau
score = 0
projectile_list = []  # projectile existant
background_list_star = []  # fond existant
background_list_planet = []  # fond existant
proj_spe_list = []
BH_list = []
keyship = [False,False,False,False]
White = 255, 255, 255
timer = [0,0]
speedlimit = 2
speedtimer = 0

#Fichier de sauvegarde du score
with open("bank.txt","r") as f:
    if f.readline() != "":
        f.seek(0)
        MAXscore = int(f.readline())

# Initialisation de l'affichage
py.init()
screen = py.display.set_mode((max_y, max_x))
rectScreen = screen.get_rect()
py.display.set_caption("Balade Stellaire")

# Initialisation du son et musique
py.mixer.init()
music_menu = py.mixer.music.load("music/menu.ogg")
py.mixer.music.play(-1) #loop -1 pour répéter la musique à l'infini
sound_play = py.mixer.Sound("music/play.wav")
sound_play.set_volume(0.3)
sound_gameover = py.mixer.Sound("music/gameover.wav")
repeat = True

#Point de Départ
depimg = py.image.load("images/deco/startarea.png").convert_alpha()
deprect = depimg.get_rect()
deprect.x = 0
deprect.y = 400

# Initialisation de l'écriture du score
write = py.font.SysFont('didot.ttc', 24)
writing = write.render("Score: 0", True, White)

#Initialisation de la représentation graphique du vaisseau
vaisseau = py.image.load(player).convert_alpha()
hitbox = py.image.load("images/hitbox.png").convert_alpha()
screen.blit(vaisseau, ((max_y - 20) / 2, max_x - 40))  # Position initiale du vaisseau 
pos = vaisseau.get_rect()  # Avoir la hitbox
pos.midbottom = (max_y / 2, max_x - 20)
py.display.flip()

# Initialisation des différents projectiles
projectile_class = [pro.Projectile_Template,pro.Projectile_1,pro.Projectile_2,pro.Projectile_2,pro.Projectile_3]
# Initialisation des différentes étoiles/planètes
star_class = [st.backstar_1, st.planet]
# Initialisation des projectiles spéciaux
proj_spe = [infi.adv_proj_1,infi.adv_proj_2,infi.adv_proj_3,infi.adv_proj_4]

#Condition pour jouer
continuer = False

# Initialisation de menu
img_fond = "images/menu/menu_fond.png"
menu_fond = py.image.load(img_fond)
img_logo = "images/menu/menu_logo.png"
menu_logo = py.image.load(img_logo)
img_instru = "images/menu/menu_instru.png"
menu_instru = py.image.load(img_instru)
img_quitter = "images/menu/menu_quitter.png"
menu_quitter = py.image.load(img_quitter)
img_jouer = "images/menu/menu_jouer.png"
menu_jouer = py.image.load(img_jouer)

# Initialisation mort
img_rejouer = "images/menu/menu_rejouer.png"
menu_rejouer = py.image.load(img_rejouer)
img_mort = "images/menu/menu_mort.png"
menu_mort = py.image.load(img_mort)


def depart(temp=False):  # fonction pour le menu de début
    global repeat
    while not temp:
        screen.blit(menu_fond, (0, 0))
        screen.blit(menu_instru, (50, 550))
        screen.blit(menu_logo, (20, 120))
        screen.blit(menu_jouer, (25, 700))
        screen.blit(menu_quitter, (20, 20))
        py.display.update()
        for event in py.event.get():
            if event.type == QUIT:
                return True, True
            if event.type == py.KEYDOWN:
                if event.key == K_SPACE:
                    repeat = True
                    return True, False
                if event.key == K_ESCAPE:
                    return True, True

def fin(temp=False):  # fonction menu de fin (mort)
    global repeat
    if fu.colli_test(pos, projectile_list) or fu.colli_test(pos, proj_spe_list):
        if repeat :
            sound_gameover.play()
            py.mixer.music.stop()
            repeat = False
        screen.blit(menu_mort, (50, 200))
        screen.blit(menu_rejouer, (25, 700))
        return True
    return False

depart1 = False
fin1 = False
while not continuer:  # boucle principale du jeu
    while not depart1:  # boucle pour le menu de début
        depart1, continuer = depart()
        if depart1 :
            sound_play.play() #sound effect
            py.mixer.music.stop()
            music_maintheme = py.mixer.music.load("music/music.ogg")
            py.mixer.music.play(-1)

    py.time.Clock().tick(fps)  # Paramétrage du rafraichissement du programme

    # Vérification de la mort------------------------------------------------------------

    fin1 = fin()
    if fin1 is False:  # permet de geler le jeu en cas de mort
        for event in py.event.get():
            if event.type == QUIT:
                continuer = True
            if event.type == py.KEYDOWN:  # si une touche est pressé
                if event.key == K_ESCAPE:
                    continuer = True
                if event.key == K_z or event.key == K_UP:  # pour faire les touches de déplacements
                    keyship[0] = True
                if event.key == K_s or event.key == K_DOWN:
                    keyship[1] = True
                if event.key == K_d or event.key == K_RIGHT:
                    keyship[2] = True
                if event.key == K_q or event.key == K_LEFT:
                    keyship[3] = True
            if event.type == py.KEYUP:  # Retire l'état de déplacement si la touche n'est plus pressé
                if event.key == K_z or event.key == K_UP:  # pour faire les touches de déplacements
                    keyship[0] = False
                if event.key == K_s or event.key == K_DOWN:
                    keyship[1] = False
                if event.key == K_d or event.key == K_RIGHT:
                    keyship[2] = False
                if event.key == K_q or event.key == K_LEFT:
                    keyship[3] = False
        
        if keyship[0]:
            if vy > -speedlimit:
                vy -= 1
        if keyship[1]:
            if vy < speedlimit:
                vy += 1
        if keyship[2]:
            if vx < speedlimit:
                vx += 1
        if keyship[3]:
            if vx > -speedlimit:
                vx -= 1

        if speedtimer == 0: # Déplacement inertiel du vaisseau
            if not keyship[0] and not keyship[1]:
                while vy != 0:
                    if vy>0:
                        vy-=1
                    else:
                        vy+=1
            if not keyship[2] and not keyship[3]:
                while vx != 0:
                    if vx>0:
                        vx-=0.5
                    else:
                        vx+=0.5
            speedtimer = 35
        else:
            speedtimer-=1

        screen.fill(0x000000)  # Rafraichit l'écran (noir)

        # Image de la plateforme de départ
        if deprect.y < 800:
            deprect.y += 3
            screen.blit(depimg,deprect)

        # Appliquer les paramètres de mouvement avec vérification pour rester dans les confins de l'écran
        pos = pos.move(int(vx), int(vy)).clamp(rectScreen)

        # Création du fond mouvant (étoiles et planètes)
        if len(background_list_star) < 100 and timer[0] <= 0:
            timer[0] = 15
            background_list_star.append(st.backstar_1(max_y))
        else:
            timer[0] -= 1

        if len(background_list_planet) < 2 and timer[1] <= 0:
            timer[1] = random.randint(250,600)
            background_list_planet.append(st.planet(max_y))
        else:
            timer[1] -= 1

        for star in background_list_star:
            star.rect = star.rect.move(star.speed)
            if star.rect.y > max_x:
                background_list_star.remove(star)
            screen.blit(star.img, star.rect)

        for plan in background_list_planet:
            plan.rect = plan.rect.move(plan.speed)
            if plan.rect.y > max_x:
                background_list_planet.remove(plan)
            screen.blit(plan.img, plan.rect)

        # Création/Gestion des projectiles------------------------------------------------------------
        if len(projectile_list) < 20:  # sécurité pour éviter trop de projectile à l'écran
            if random.randint(1, 1000) + score / 1000 > 997:
                projectile_list.append(projectile_class[random.randint(0, len(projectile_class) - 1)](score, max_y))

        for proj in projectile_list[:]: # Rafraichissement du comportement des projectiles existants
            proj.rect = proj.rect.move(proj.speed)
            proj.rect.x = proj.xsave+proj.traj()

            if proj.rect.y > max_x:  # Supprimer le projectile dès qu'il sort de l'écran
                projectile_list.remove(proj)
            screen.blit(proj.img, proj.rect)

        # Création/Gestion des projectiles spéciaux---------------------------------------------------
        if len(proj_spe_list) < 1:  # sécurité pour éviter trop de projectile à l'écran
            if random.randint(1, 5000) + score / 1000 > 4999:
                proj_spe_list.append(proj_spe[random.randint(0,len(proj_spe))-1](max_y))

        for sp in proj_spe_list: # Rafraichissement du comportement des projectiles existants
            sp.sx = pos.x
            sp.sy = pos.y
            if sp.time > 0:
                sp.time -= 1
                sp.temptraj=sp.traj()
            sp.rect = sp.rect.move(sp.temptraj)
            if sp.sx > max_y or sp.sx < 0 or sp.sy > max_x or sp.sy < -50 : 
                proj_spe_list.remove(sp)
            screen.blit(sp.img, sp.rect)
        
        # Création/Gestion des trous noirs---------------------------------------------------
        if len(BH_list) < 1:  # sécurité pour éviter trop de trou noir à l'écran
            if random.randint(1, 7000) + score / 1000 > 6999:
                BH_list.append(infi.black_hole(max_y))
        for bH in BH_list:
            bH.rect.y += 1
            tempposmovBH = [0,0]
        
            for proj in projectile_list: # Rafraichissement du comportement du trou noir
                tempposmovBH = infi.blackholesuck(proj.rect.x,bH.rect.x,proj.rect.y,bH.rect.y,500)
                proj.rect.x += tempposmovBH[0]
                proj.rect.y += tempposmovBH[1]
            tempposmovBH = infi.blackholesuck(pos.x,bH.rect.x,pos.y,bH.rect.y,500)
            pos.x += tempposmovBH[0]
            pos.y += tempposmovBH[1]
            if bH.rect.x > max_y or bH.rect.x < 0 or bH.rect.y > max_x or bH.rect.y < -100 : 
                BH_list.remove(bH)
            screen.blit(bH.img,bH.rect)

        # Ecriture du Score------------------------------------------------------------
        writingbestscore = write.render("Meilleur score: " + str(int(MAXscore)), True, White)
        writingscore = write.render("Score: " + str(int(score)), True, White)
        score += 0.01
        if score > MAXscore:
            MAXscore = score
        screen.blit(writingscore, (10, 30))
        screen.blit(writingbestscore, (10, 10))
        screen.blit(vaisseau, pos)
    else:
        # En cas de mort tout est réinitialisé pour la nouvelle partie
        for event in py.event.get():
            if event.type == py.KEYDOWN:
                if event.key == K_ESCAPE:
                    continuer = True
                if event.key == K_SPACE:
                    sound_play.play() #sound effect
                    music_menu = py.mixer.music.load("music/menu.ogg")
                    py.mixer.music.play(-1)
                    continuer = False  # remise des variables
                    depart1 = False
                    fin1 = False
                    score = 0
                    keyship = [False,False,False,False]
                    deprect.x = 0
                    deprect.y = 400
                    pos = pos.move(-500, 800).clamp(rectScreen) # Réinitialisation de la position du vaisseau
                    pos = pos.move(250, 100).clamp(rectScreen)

                    projectile_list = []
                    proj_spe_list = []
                    BH_list = []

    py.display.update()  # mise à jour de l'écran

with open("bank.txt","w") as f: # Enregistrement du meilleur score
    f.write(str(int(MAXscore)))
py.quit()