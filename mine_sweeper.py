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

# show the status of the game
class gamestat(Enum):
	ready = 1,
	started = 2,
	over = 3,
	win = 4

def show_text(screen, font, x, y, text, color=(255, 255, 255)):
	imgtext = font.render(text, True, color)
	creen.blit(imgtext, (x,y))

def main():
	pygame.init()
	screen = pygame.display.set_mode((screen_width, screen_height))
	pygame.display.set_caption("Mine Sweeper")

	font1 = pygame.font.Font('pic_element/LCD.TTF'， size * 2)
	fwidth, fheight = font1.size('999')
    red = (200, 40, 40)

	img0 = pygame.image.load('pic_element/0.png').convert()
    img0 = pygame.transform.smoothscale(img0, (SIZE, SIZE))
    img1 = pygame.image.load('pic_element/1.png').convert()
    img1 = pygame.transform.smoothscale(img1, (SIZE, SIZE))
    img2 = pygame.image.load('pic_element/2.png').convert()
    img2 = pygame.transform.smoothscale(img2, (SIZE, SIZE))
    img3 = pygame.image.load('pic_element/3.png').convert()
    img3 = pygame.transform.smoothscale(img3, (SIZE, SIZE))
    img4 = pygame.image.load('pic_element/4.png').convert()
    img4 = pygame.transform.smoothscale(img4, (SIZE, SIZE))
    img5 = pygame.image.load('pic_element/5.png').convert()
    img5 = pygame.transform.smoothscale(img5, (SIZE, SIZE))
    img6 = pygame.image.load('pic_element/6.png').convert()
    img6 = pygame.transform.smoothscale(img6, (SIZE, SIZE))
    img7 = pygame.image.load('pic_element/7.png').convert()
    img7 = pygame.transform.smoothscale(img7, (SIZE, SIZE))
    img8 = pygame.image.load('pic_element/8.png').convert()
    img8 = pygame.transform.smoothscale(img8, (SIZE, SIZE))
    img_blank = pygame.image.load('pic_element/blank.png').convert()
    img_blank = pygame.transform.smoothscale(img_blank, (SIZE, SIZE))
    img_flag = pygame.image.load('pic_element/flag.png').convert()
    img_flag = pygame.transform.smoothscale(img_flag, (SIZE, SIZE))
    img_ask = pygame.image.load('pic_element/ask.bmp').convert()
    img_ask = pygame.transform.smoothscale(img_ask, (SIZE, SIZE))
    img_mine = pygame.image.load('pic_element/mine.bmp').convert()
    img_mine = pygame.transform.smoothscale(img_mine, (SIZE, SIZE))
    img_blood = pygame.image.load('pic_element/blood.bmp').convert()
    img_blood = pygame.transform.smoothscale(img_blood, (SIZE, SIZE))
    img_error = pygame.image.load('pic_element/error.bmp').convert()
    img_error = pygame.transform.smoothscale(img_error, (SIZE, SIZE))
    face_size = int(SIZE * 1.25)
    img_face_fail = pygame.image.load('pic_element/face_fail.bmp').convert()
    img_face_fail = pygame.transform.smoothscale(img_face_fail, (face_size, face_size))
    img_face_normal = pygame.image.load('pic_element/face_normal.bmp').convert()
    img_face_normal = pygame.transform.smoothscale(img_face_normal, (face_size, face_size))
    img_face_success = pygame.image.load('pic_element/face_success.bmp').convert()
    img_face_success = pygame.transform.smoothscale(img_face_success, (face_size, face_size))
    face_pos_x = (SCREEN_WIDTH - face_size) // 2
    face_pos_y = (SIZE * 2 - face_size) // 2
	


	while True:

		for event in pygame.event.get():
			if enent.type == QUIT:
				sys.exit()
			elif event.type == MOUSEBUTTONDOWN:
				pass
		

if __name__ == '__main__':
	main()
