import pygame
import sys
from pygame.locals import *
from MapEdit import *
from Editor import *
from Game import *
from Weapon import * 
#import Weapon

weap = Weapon();
weap.generate();
weap.displayInformations();

"""
class TEST():
	
	RIGHT	= 3

	class INTEST():
		WALL	= 1
		GROUND	= 2
		UNKNOWN = -1

print(TEST.INTEST.GROUND)

"""
pygame.init()

screen = pygame.display.set_mode((640,480))

fond = pygame.image.load("../resources/fond.jpg").convert()
screen.blit(fond, (0,0))



ant = pygame.image.load("../resources/ant.png").convert_alpha()
screen.blit(ant, (20,20))

perso=pygame.image.load("../resources/perso.png").convert_alpha()

#Green = pygame.Color(255,0,255)


#titre
pygame.display.set_caption("AntsMustDie")

map=MapEdit(20,20)
edit=Editor(map)



#BOUCLE PRINCIPALE
stop=False

while not stop:
	#affichage de l ecran d accueil
	welcome_screen=pygame.image.load("../resources/welcom_screen.png")
	screen.blit(welcome_screen,(0,0))

	#Refresh
	pygame.display.flip()

	continue_menu=True

	#BOUCLE MENU
	while continue_menu:
		#limitation de la vitesse de la boucle
		pygame.time.Clock().tick(30)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				stop=True
				continue_menu=0
				continue_game=0
				pygame.quit()
				sys.exit()

			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_F1:
					#Lancement d l editeur
					edit.run(screen)
				if event.key==pygame.K_F2:
					map.load("TOTO.txt")
					game=Game(map)
					game.run(screen)
				if event.key==pygame.K_DOWN:
					position_perso=position_perso.move(0,3)

	#re collage
	screen.blit(fond,(0,0))
	screen.blit(perso,position_perso)

	# update sceen
	pygame.display.flip()

	screen.blit(ant,(100,100))

pygame.display.flip()

pygame.display.update()

    	
#grid = [[0] * colonnes for _ in range(lignes)]
#screen.fill(Green)