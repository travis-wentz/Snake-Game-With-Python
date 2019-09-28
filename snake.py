from pygame.locals import *
import pygame
import time

def snake():

	pygame.init()

	go = True

	#loop to constantly listen for user input
	while(go):
		pygame.event.pump()
		keys = pygame.key.get_pressed()
		
		if (keys[K_RIGHT]):
	   		print("Right arrow pressed.")
	   	if (keys[K_LEFT]):
	   		print("Left arrow pressed.")
		if (keys[K_UP]):
	   		print("Up arrow pressed.")
	   	if (keys[K_DOWN]):
	   		print("Down arrow pressed.")
	   	if (keys[K_ESCAPE]):
	   		go = False

if __name__ == "__main__":
    snake()