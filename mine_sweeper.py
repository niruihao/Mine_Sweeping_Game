'''
author: Ruihao Ni

This is a python game to realize the mine sweeper game
under the pygame module.


'''


import sys
import pygame
# Width of the screen
screen_width = block_width * size
# Height of the screen
screen_height = (block_width + 2) * size

def main():
	pygame.init()
	screen = pygame.display.set_mode((screen_width, screen_height))
	pygame.display.set_caption("Mine Sweeper")
	
	while True:

		for event in pygame.event.get():
			if enent.type == QUIT:
				sys.exit()
			elif event.type == MOUSEBUTTONDOWN:
				pass
		

if __name__ == '__main__':
	main()	