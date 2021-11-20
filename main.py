# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# importing pygamee library
import pygame as pg
import sys
import numpy as np

# intializing pygame
pg.init()

# setting the width and the height constents
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
ROWS = 3
COLUMNS =3

# rgb :
RED = (255, 0, 0)
BG_COLOR = (28, 200, 156)
LINE = (23, 145, 135)

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('TIC TAK TOE')
screen.fill(BG_COLOR)
,
# creating lines on the screen

# function to create the drawing lines
def draw_lines():
    # first horizontal lines
    pg.draw.line(screen, LINE, (0, 200), (600, 200), LINE_WIDTH)
    # second horizontal lines
    pg.draw.line(screen, LINE, (0, 400), (600, 400), LINE_WIDTH)
    # first vertical line
    pg.draw.line(screen, LINE, (200, 0), (200, 600), LINE_WIDTH)
    # second vertical line
    pg.draw.line(screen, LINE, (400, 0), (400, 600), LINE_WIDTH)


draw_lines()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        pg.display.update()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
