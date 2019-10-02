from os import system
from pygame.locals import *
import copy
import pygame
import queue
import random
import sys
import time

speed = 5 #speed the snake moves at
width = 20 #width of grid
height = 20 #height of grid
x = int(width / 2) #current x position (start in middle)
y = int(height / 2) #current y position (start in middle)
direction = "right"
map = None
snek = queue.Queue()

def snake():

	pygame.init()
	buildMap()

	global x
	global y
	global direction
	global map
	global snek
	snek.put((x - 3, y))
	snek.put((x - 2, y))
	snek.put((x - 1, y))
	snek.put((x, y))
	addApple()

	go = True

	#loop to constantly listen for user input
	while(go):
		pygame.event.pump()
		keys = pygame.key.get_pressed()
		
		if (keys[K_RIGHT] and direction != "left"):
			direction = "right"
		elif (keys[K_LEFT] and direction != "right"):
			direction = "left"
		elif (keys[K_UP] and direction != "down"):
			direction = "up"
		elif (keys[K_DOWN]and direction != "up"):
			direction = "down"
		elif (keys[K_ESCAPE]):
			go = False

		time.sleep (50.0 / (speed * 100.0));
		slither()

def buildMap():
	temp = []

	for i in range(height + 2):
		row = []
		for j in range(width + 2):
			if (i == 0 or i == height + 1):
				row.append('-')
			elif(j == 0 or j == width + 1):
				row.append('|')
			else:
				row.append(' ')
		temp.append(row)

	global map
	map = temp

def printMap():
	_ = system('clear')
	global map
	for row in map:
		full_row = ""
		for r in row:
			full_row = full_row + r + " "
		print(full_row)

def slither():
	global x
	global y
	global direction
	global snek
	global map

	# take away the tail and add to the head
	tail = snek.get()
	if(direction == "right"):
		x = x + 1
	elif(direction == "left"):
		x = x - 1
	elif(direction == "up"):
		y = y - 1
	elif(direction == "down"):
		y = y + 1

	snek.put((x,y))

	# TODO if snake just ate apple and there are no more free spaces
	#		show win and quit game.
	# TODO if snake just ate apple, call addApple()
	# TODO if snake just ate an apple don't delete tail
	map[tail[1]][tail[0]] = " " #remove tail from map
	map[y][x] = 'X' # add new head to map

	printMap()
	
	# kill snake if x,y is out of bounds
	if(x > width or x <= 0):
		dieSnakeDie()
	elif(y > height or y <= 0):
		dieSnakeDie()
	# TODO kill snake if it runs into itself
	

def dieSnakeDie():
	buildMap()
	sys.exit()

def addApple():
	freeSpace = randFreeSpace()

	map[freeSpace[1]][freeSpace[0]] = '*'

def randFreeSpace():
	location = 'X' # will be the location we're tryting to add apple to
	randX = 0
	randY = 0

	# TODO check that there is at least 1 empty space to avoid infinite loop
	while(location != ' '):
		# create a sudo-random coordinates for the apple
		# coord = randCoordinates()
		randX = random.randint(1, width)
		randY = random.randint(1, height)

		# make sure the coordinates are a free space
		location = map[randY][randX]

	return ((randX, randY))


if __name__ == "__main__":
	snake()