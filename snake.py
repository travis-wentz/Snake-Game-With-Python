from os import system
from pygame.locals import *
import pygame
import time
import queue
import copy

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
	snek.put((int(x - 2), y))
	snek.put((int(x - 1), y))
	snek.put((x, y))

	go = True

	#loop to constantly listen for user input
	while(go):
		pygame.event.pump()
		keys = pygame.key.get_pressed()
		
		if (keys[K_RIGHT]):
			direction = "right"
		elif (keys[K_LEFT]):
			direction = "left"
		elif (keys[K_UP]):
			direction = "up"
		elif (keys[K_DOWN]):
			direction = "down"
		elif (keys[K_ESCAPE]):
			go = False

		time.sleep (50.0 / (speed * 100.0));
		slither()
		printMap()

def buildMap():
	temp = []

	for i in range(height + 2):
		row = []
		for j in range(width + 2):
			if (i == 0 or i == height + 1):
				row.append("-")
			elif(j == 0 or j == width + 1):
				row.append("|")
			else:
				row.append(" ")
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

	# TODO if snake just ate an apple don't delete tail
	map[tail[1]][tail[0]] = " " #remove tail from map

	# TODO would be faster to just add new head to map b/c body is already there
	
	#add snake to map
	for i in range(snek.qsize()):
		t = snek.get()
		map[t[1]][t[0]] = "X"
		snek.put(t)


if __name__ == "__main__":
	snake()