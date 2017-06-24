import pygame
import sys
from pygame.locals import *
from MapEdit import *



class PYGAME_BUTTON():
	LEFT	= 1
	RIGHT	= 3

class MAP_CASE():
	WALL	= 1
	GROUND	= 2
	UNKNOWN = -1

BLOC_SIZE=32

WHITE = pygame.Color(255,255,255)
BLACK = pygame.Color(0,0,0)

class Editor(object):
	"""description of class"""

	def __init__(self, _map):
		self.case			= []
		self.map			= _map
		self.camera_pos_x	= 0
		self.camera_pos_y	= 0
		self.width_display	= 20
		self.height_display = 20

	def run(self,screen):
		continue_editor=True
		#BOUCLE EDITEUR
		while continue_editor:
			#limitation de la vitesse de la boucle
			pygame.time.Clock().tick(30)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					stop=True
					continue_menu=0
					continue_game=0
					pygame.quit()
					sys.exit()

				if event.type==pygame.MOUSEBUTTONDOWN:
					if event.button==PYGAME_BUTTON.LEFT:
						self.map.setCaseType(int(event.pos[0]/BLOC_SIZE),int(event.pos[1]/BLOC_SIZE),MAP_CASE.GROUND)
					elif event.button==PYGAME_BUTTON.RIGHT:
						self.map.setCaseType(int(event.pos[0]/BLOC_SIZE),int(event.pos[1]/BLOC_SIZE),MAP_CASE.WALL)
				if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_KP_ENTER:
						self.map.save("TOTO.txt")
						#Lancement d l editeur
						#editeurRun()
					#if event.key==pygame.K_DOWN:
						#player_position=player_position.move(0,3)
				#screen.fill(BLACK)
			self.displayMap(screen)
			
			#re collage
			#sceen.blit(fond,(0,0))
			#sceen.blit(perso,position_perso)

			# update sceen
			pygame.display.flip()

	def displayMap(self,sceen):
		wall = pygame.image.load("../resources/wall.png").convert_alpha()
		ground = pygame.image.load("../resources/ground.png").convert_alpha()
		for j in range (self.camera_pos_y, self.camera_pos_y + self.height_display):
			for i in range (self.camera_pos_x, self.camera_pos_x + self.width_display):
				type=self.map.getCaseType(i,j)
				if(type==MAP_CASE.GROUND):
					sceen.blit(ground,(i*BLOC_SIZE,j*BLOC_SIZE))
					#pygame.gfxdraw.box(screen,(i,j,BLOC_SIZE,BLOC_SIZE),WHITE)
				elif(type==MAP_CASE.WALL):
					sceen.blit(wall,(i*BLOC_SIZE,j*BLOC_SIZE))
					#pygame.gfxdraw.box(screen,(i,j,BLOC_SIZE,BLOC_SIZE),BLACK)





