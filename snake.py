from os import system
from pygame.locals import *
import pygame
import time

width = 10 #width of grid
height = 10 #height of grid
x = width / 2 #current x position (start in middle)
y = height / 2 #current y position (start in middle)
direction = "right" #direction the snake is currently moving
map = None

def snake():

	pygame.init()
	buildMap()

	global x
	global y
	global direction
	global map
	go = True

	#loop to constantly listen for user input
	while(go):
		pygame.event.pump()
		keys = pygame.key.get_pressed()
		
		if (keys[K_RIGHT]):
			direction = "right"
			x = x + 1
			buildMap()
		if (keys[K_LEFT]):
			direction = "left"
			x = x - 1
			buildMap()
		if (keys[K_UP]):
			direction = "up"
			y = y - 1
			buildMap()
		if (keys[K_DOWN]):
			direction = "down"
			y = y + 1
			buildMap()
		if (keys[K_ESCAPE]):
			go = False
		time.sleep (50.0 / 1000.0);

def buildMap():
	_ = system('clear')
	temp = []

	for i in range(height + 2):
		row = []
		for j in range(width + 2):
			if (i == 0 or i == height + 1):
				row.append("-")
			elif(j == 0 or j == width + 1):
				row.append("|")
			elif(i == y and j == x):
				row.append("X")
			else:
				row.append(" ")
		temp.append(row)

	global map
	map = temp
	printMap()

def printMap():
	global map
	for row in map:
		full_row = ""
		for r in row:
			full_row = full_row + r + " "
		print(full_row)


if __name__ == "__main__":
	snake()