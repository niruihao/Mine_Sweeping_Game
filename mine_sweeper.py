'''
Author: Ruihao Ni

This is a python game to realize the mine sweeper game
originated from the Windows XP system using the pygame module.

'''

import sys
import pygame
import time
import random
from enum import Enum
from pygame.locals import *

block_width = 9  # height of the block
block_height = 9  # height of the block
mine_count = 10  # number of  mines in the game
size = 20  # size of each block

# Easy mode: 9*9 with 10 mines
# Medium mode: 16*16 with 40 mines
# Hard mode: 30*16 with 99 mines

# Width of the screen
screen_width = block_width * size
# Height of the screen
screen_height = (block_height + 2) * size

class blockstat(Enum):
    # record the status of block.
    normal = 1  # not_clicked, the initial state
    opened = 2  # clicked
    mine = 3    # mine
    flag = 4    # mark that there is a mine in the box
    ask = 5     # set a ?
    bomb = 6    # step on the bomb
    hint = 7    # blocks around the both click
    double = 8  # both click the mouse

class Mine:

    # set five variables for Mine class
    # x, y, value, mine_around and status
    # getter and setter and property function
    # reference on how to use getter, setter, property
    # https://www.geeksforgeeks.org/getter-and-setter-in-python/

    def __init__(self, x, y, value=0):
        self._x = x
        self._y = y
        self._value = 0
        self._mine_around = -1
        self._status = blockstat.normal
        self.set_value(value)

    def __repr__(self):
        return str(self._value)
    # position(coordination) of the block
    # x
    def get_x(self):
        return self._x

    def set_x(self):
        self._x = x

    x = property(fget=get_x, fset=set_x)

    # y
    def get_y(self):
        return self._y

    def set_y(self):
        self._y = y

    y = property(fget=get_y, fset=set_y)

    # value: mine or not mine in this block
    def get_value(self):
        return self._value

    def set_value(self, value):
        if value:
            self._value = 1
        else:
            self._value = 0

    value = property(fget=get_value, fset=set_value, doc='0:non-mine 1:mine')

    # mine around: how many mines around the block
    def get_mine_around(self):
        return self._mine_around

    def set_mine_around(self, mine_around):
        self._mine_around = mine_around

    mine_around = property(fget=get_mine_around, fset=set_mine_around, doc='mine_nnumber')

    # status: the blockstat class: opened/ mine/ flag/ bomb etc.
    def get_status(self):
        return self._status

    def set_status(self, value):
        self._status = value

    status = property(fget=get_status, fset=set_status, doc='blockstat')

class mine_block:
    def __init__(self):
        self._block = [[Mine(i, j) for i in range(block_width)] for j in range(block_height)]

        # randomly set the mine
        for i in random.sample(range(block_width * block_height), mine_count):
            self._block[i // block_width][i % block_width].value = 1

    # getter function for the block
    def get_block(self):
        return self._block

    block = property(fget=get_block)

    def getmine(self, x, y):
        return self._block[y][x]

    def open_mine(self, x, y):
        # step on the mine
        if self._block[y][x].value:
            self.block[y][x].status = blockstat.bomb
            return False

        # first we change the status to opened
        self._block[y][x].status = blockstat.opened

        around = _get_around(x, y)

        _sum = 0
        for i, j in around:
            if self._block[j][i].value:
                _sum += 1
        self._block[y][x].mine_around = _sum

        # if there is no mine around, then use recursion method to calculate
        # blocks around, the we can open a big range without mine with one click
        if _sum == 0:
            for i, j in around:
                if self._block[j][i].mine_around == -1:
                    self. open_mine(i, j)
        return True

    def double_mouse_button_down(self, x, y):
        # both button clicked to realize the hint function
        # pen the block if no mines around
        if self._block[y][x].mine_around == 0:
            return True

        self._block[y][x].status = blockstat.double

        around = _get_around(x, y)

        sumflag = 0  # the flagged mine around
        for i, j in _get_around(x, y):
            if self._block[j][i].status == blockstat.flag:
                sumflag += 1
        # all the mine around was marked
        result = True
        if sumflag == self._block[y][x].mine_around:
            for i, j in around:
                if self._block[j][i].status == blockstat.normal:
                    if not self.open_mine(i, j):
                        result = False
        else:
            for i, j in around:
                if self._block[j][i].status == blockstat.normal:
                    self.block[j][i].status = blockstat.hint
        return result

    def double_mouse_button_up(self, x, y):
        # open all the blocks around
        self._block[y][x].status = blockstat.opened

        for i, j in _get_around(x, y):
            if self._block[j][i].status == blockstat.hint:
                    self.block[j][i].status = blockstat.normal

def _get_around(x, y):
    # return coord of eight blocks around(x, y)
    return [(i, j) for i in range(max(0, x - 1), min(block_width - 1, x + 1) + 1)
            for j in range(max(0, y - 1), min(block_height - 1, y + 1) + 1) if i != x or j != y]


class gamestat(Enum):
    # show the status of the game
    ready = 1,  # ready to start the game
    started = 2,  # after one click on the board, start the game
    over = 3,  # when step on the mine, game over
    win = 4  # when all the mine was marked and all the other block was opened, game win

def show_text(screen, font, x, y, text, color=(255, 255, 255)):
    imgtext = font.render(text, True, color)
    screen.blit(imgtext, (x, y))

def main():
    # reference on how to use pygame:
    # https://www.pygame.org/wiki/GettingStarted
    # https://www.youtube.com/watch?v=FfWpgLFMI7w
    # initiate the pygame and open the window around.
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Mine Sweeper")

    # import the font and let the word looks like LCD display
    font1 = pygame.font.Font('pic_element/LCD.TTF', size * 2)
    fwidth, fheight = font1.size('999')
    red = (200, 40, 40)

    # load the picture resources and revert them to the same size
    # picture resources: https://github.com/maulik-vaghela/MineSweeper
    img0 = pygame.image.load('pic_element/0.png').convert()
    img0 = pygame.transform.smoothscale(img0, (size, size))
    img1 = pygame.image.load('pic_element/1.png').convert()
    img1 = pygame.transform.smoothscale(img1, (size, size))
    img2 = pygame.image.load('pic_element/2.png').convert()
    img2 = pygame.transform.smoothscale(img2, (size, size))
    img3 = pygame.image.load('pic_element/3.png').convert()
    img3 = pygame.transform.smoothscale(img3, (size, size))
    img4 = pygame.image.load('pic_element/4.png').convert()
    img4 = pygame.transform.smoothscale(img4, (size, size))
    img5 = pygame.image.load('pic_element/5.png').convert()
    img5 = pygame.transform.smoothscale(img5, (size, size))
    img6 = pygame.image.load('pic_element/6.png').convert()
    img6 = pygame.transform.smoothscale(img6, (size, size))
    img7 = pygame.image.load('pic_element/7.png').convert()
    img7 = pygame.transform.smoothscale(img7, (size, size))
    img8 = pygame.image.load('pic_element/8.png').convert()
    img8 = pygame.transform.smoothscale(img8, (size, size))
    img_blank = pygame.image.load('pic_element/blank.png').convert()
    img_blank = pygame.transform.smoothscale(img_blank, (size, size))
    img_flag = pygame.image.load('pic_element/flag.png').convert()
    img_flag = pygame.transform.smoothscale(img_flag, (size, size))
    img_ask = pygame.image.load('pic_element/ask.bmp').convert()
    img_ask = pygame.transform.smoothscale(img_ask, (size, size))
    img_mine = pygame.image.load('pic_element/mine.bmp').convert()
    img_mine = pygame.transform.smoothscale(img_mine, (size, size))
    img_blood = pygame.image.load('pic_element/blood.bmp').convert()
    img_blood = pygame.transform.smoothscale(img_blood, (size, size))
    img_error = pygame.image.load('pic_element/error.bmp').convert()
    img_error = pygame.transform.smoothscale(img_error, (size, size))
    face_size = int(size * 1.25)
    img_face_fail = pygame.image.load('pic_element/face_fail.bmp').convert()
    img_face_fail = pygame.transform.smoothscale(img_face_fail, (face_size, face_size))
    img_face_normal = pygame.image.load('pic_element/face_normal.bmp').convert()
    img_face_normal = pygame.transform.smoothscale(img_face_normal, (face_size, face_size))
    img_face_success = pygame.image.load('pic_element/face_success.bmp').convert()
    img_face_success = pygame.transform.smoothscale(img_face_success, (face_size, face_size))
    face_pos_x = (screen_width - face_size) // 2
    face_pos_y = (size * 2 - face_size) // 2

    # link the number of mine around with the corresponding picture
    img_dict = {
        0: img0,
        1: img1,
        2: img2,
        3: img3,
        4: img4,
        5: img5,
        6: img6,
        7: img7,
        8: img8
    }

    # background color (grey)
    bgcolor = (225, 225, 225)

    block = mine_block()
    game_status = gamestat.ready
    start_time = None  # start time
    elapsed_time = 0  # time needed

    # start the game

    while True:
        # fill the background color
        screen.fill(bgcolor)
        # start the game
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                x = mouse_x // size
                y = mouse_y // size - 2

                # b1 is the left button and b3 is the right button
                b1, b2, b3 = pygame.mouse.get_pressed()
                if game_status == gamestat.started:
                    # both button pressed at the same time, if all the mine was
                    # flagged, then open all the blocks around. if there're unflagged
                    # mine, act as all the block pressed at the same time
                    if b1 and b3:
                        mine = block.getmine(x, y)
                        if mine.status == blockstat.opened:
                            if not block.double_mouse_button_down(x, y):
                                game_status = gamestat.over

            elif event.type == MOUSEBUTTONUP:
                # when hit the face icon, restart the game
                if y < 0:
                    if face_pos_x <= mouse_x <= face_pos_x + face_size and face_pos_y <= mouse_y <= face_pos_y + face_size:
                        game_status = gamestat.ready
                        block = mine_block()
                        start_time = time.time()
                        elapsed_time = 0
                        continue
                # if not hit on the icon, start the game
                if game_status == gamestat.ready:
                    game_status = gamestat.started
                    start_time = time.time()
                    elapsed_time = 0
                # if the game has already started, then process the other logics
                if game_status == gamestat.started:
                    mine = block.getmine(x, y)
                    # hit the left button, and open the block, if got a mine, game over
                    if b1 and not b3:
                        if mine.status == blockstat.normal:
                            if not block.open_mine(x, y):
                                game_status = gamestat.over
                    # hit the right button, mark the block, change
                    # the change is a circle: normal, flagged and ?
                    elif not b1 and b3:
                        if mine.status == blockstat.normal:
                            mine.status = blockstat.flag
                        elif mine.status == blockstat.flag:
                            mine.status = blockstat.ask
                        elif mine.status == blockstat.ask:
                            mine.status = blockstat.normal

                    # hit both button, realize the hint function
                    elif b1 and b3:
                        if mine.status == blockstat.double:
                            block.double_mouse_button_up(x, y)

        # flag_count: how many flagged mines
        # how many opened mines
        flag_count = 0
        opened_count = 0

        # show the corresponding picture for each block according to their status
        for row in block.block:
            for mine in row:
                pos = (mine.x * size, (mine.y + 2) * size)
                if mine.status == blockstat.opened:
                    screen.blit(img_dict[mine.mine_around], pos)
                    opened_count += 1
                elif mine.status == blockstat.double:
                    screen.blit(img_dict[mine.mine_around], pos)
                elif mine.status == blockstat.bomb:
                    screen.blit(img_blood, pos)
                elif mine.status == blockstat.flag:
                    screen.blit(img_flag, pos)
                    flag_count += 1
                elif mine.status == blockstat.ask:
                    screen.blit(img_ask, pos)
                elif mine.status == blockstat.hint:
                    screen.blit(img0, pos)
                elif game_status == gamestat.over and mine.value:
                    screen.blit(img_mine, pos)
                elif mine.value == 0 and mine.status == blockstat.flag:
                    screen.blit(img_error, pos)
                elif mine.status == blockstat.normal:
                    screen.blit(img_blank, pos)
        # on the left of the face icon, shows how many mines are not marked yet.
        show_text(screen, font1, 30, (size * 2 - fheight) // 2 - 2, '%02d' % (mine_count - flag_count), red)
        # on the right of the face iocn, shows the elaspse time of the game.
        if game_status == gamestat.started:
            elapsed_time = int(time.time() - start_time)
        show_text(screen, font1, screen_width - fwidth - 22, (size * 2 - fheight) // 2 - 2, '%03d' % elapsed_time, red)
        # if all the mines are marked and all the other blockes are opened, win the game.
        if flag_count + opened_count == block_width * block_height:
            game_status = gamestat.win
        # show the different face icon in different situation.
        if game_status == gamestat.over:
            screen.blit(img_face_fail, (face_pos_x, face_pos_y))
        elif game_status == gamestat.win:
            screen.blit(img_face_success, (face_pos_x, face_pos_y))
        else:
            screen.blit(img_face_normal, (face_pos_x, face_pos_y))

        pygame.display.update()

if __name__ == '__main__':
    main()
