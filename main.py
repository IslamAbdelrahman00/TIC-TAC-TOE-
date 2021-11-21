# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# importing pygamee library
import pygame as pg
import sys
import numpy as np
import random as rd

# intializing pygame

pg.init()

# setting the  constents
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
ROWS = 3
COLUMNS = 3
FIGURE_C_RADIUS=60
FIGURE_C_WIDTH=15
X_WiDTH = 25
SPACE=55

# rgb :
RED = (255, 0, 0)
FIGURES=(224, 213, 56)
BACKGROUND_COLOR = (97, 97, 94)
LINE = (46, 46, 44)
X_COLOR=(26,26,26)

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('TIC TAK TOE')
screen.fill(BACKGROUND_COLOR)

# crating the board values
board = np.zeros((ROWS, COLUMNS))


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


# function to add marks in the matrix
def mark(row, col, player):
    board[row][col] = player

#function for ai to tick a square
def aiMark():
    highestScore= -1000
    bestMove_X= 0
    bestMove_Y=0
    for row in range(ROWS):
        for col in range(COLUMNS):
            if available_spots(row,col):
                board[row][col]= 2
                score = minimax(board,0,False)
                board[row][col] = 0
                if(score> highestScore):
                    highestScore=score
                    bestMove_X=row
                    bestMove_Y=col
    board[bestMove_X][bestMove_Y]=2
    return

# function to find availble spots returns true if spot is availble
def available_spots(row, col):
    if board[row][col] == 0:
        return True
    else:
        return False

#function to check if all fields in the board became full
def check_full_board():
    for row in range(ROWS):
        for col in range(COLUMNS):
            if board[row][col] ==0:
                return False
    return True

# function to draw figures on the gui
def draw_x_o():
    for r in range(ROWS):
        for c in range(COLUMNS):
            if board[r][c] ==1:
                pg.draw.circle(screen,FIGURES,(int(c*200+200/2),int(r*200+200/2)),FIGURE_C_RADIUS,FIGURE_C_WIDTH) # multiply by 200 to ge the respective corrdinates in the gui and we draw them in the center of the gui
            elif board[r][c] ==2:
                pg.draw.line(screen,X_COLOR,(c*200 +SPACE, r*200 + 200-SPACE),(c*200+200-SPACE,r*200+SPACE),X_WiDTH)
                pg.draw.line(screen,X_COLOR,(c*200+SPACE,r*200+SPACE),(c*200+200-SPACE,r*200+200-SPACE),X_WiDTH)

def check_winner(player):
    # vertical win
    for col in range(COLUMNS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_end_line(col,player)
            return True
    # Horizontal win
    for row in range(ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_Horizontal_end_line(row, player)
            return True
    # asc diagonal win
    if board[0][2]== player and board[1][1] == player and board[2][0] ==player:
        draw_asc_Diagional__line(player)
        return True
    # desc diagonal win
    if board[0][0]== player and board[1][1] == player and board[2][2] ==player:
        draw_des_Diagional__line(player)
        return True

    return False



#function to draw winning vertival line
def draw_vertical_end_line(col,player):
    postionX = col*200 +100
    if player ==1:
        color = FIGURES
    elif player ==2:
        color = X_COLOR
    pg.draw.line(screen,color,(postionX,15),(postionX,HEIGHT-15), LINE_WIDTH)

#function to draw winning Horizontal  line
def draw_Horizontal_end_line(row,player):
    postionY = row * 200 + 100
    if player == 1:
        color = FIGURES
    elif player == 2:
        color = X_COLOR
    pg.draw.line(screen, color, (15,postionY), (WIDTH - 15,postionY), LINE_WIDTH)

#function to draw winning ascending diagonal line
def draw_asc_Diagional__line(player):
    if player == 1:
        color = FIGURES
    elif player == 2:
        color = X_COLOR
    pg.draw.line(screen,color,(15,HEIGHT-15),(WIDTH-15,15),LINE_WIDTH)

#function to draw winning descending diagonal line
def draw_des_Diagional__line(player):
    if player == 1:
        color = FIGURES
    elif player == 2:
        color = X_COLOR
    pg.draw.line(screen,color,(15,15),(WIDTH-15,HEIGHT-15),LINE_WIDTH)

#function to restart the game
def restart():
    screen.fill(BACKGROUND_COLOR)
    draw_lines()
    player=1
    for row in range(ROWS):
        for col in range(COLUMNS):
            board[row][col]=0

draw_lines()
player = 1
game_over = False
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

            #if we click the screen we save the cordintess of the click location
            if event.type == pg.MOUSEBUTTONDOWN and not game_over:
                mouse_x= event.pos[0] # x_cordinates
                mouse_y= event.pos[1] # y_cordinates
                #CORDINTES WHERE BETWEEN 0 AND 600 AND EACH SQAURE IS 200X200 SO WEE NEED TO DIVID BY 200 to get THE x and y corrdinates in our board matrix

                c_column= int(mouse_x // 200)
                c_row = int(mouse_y//200)

                if available_spots(c_row,c_column):
                    if player== 1 :
                        mark(c_row,c_column,1)
                        if check_winner(player):
                            game_over=True
                        player=2

                    elif player ==2 :
                        if available_spots(c_row, c_column):
                            mark(c_row,c_column,2)
                            if check_winner(player):
                                game_over = True
                            player=1

                        player=1
                    draw_x_o()
                    print(board)

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    restart()
                    game_over=False

        pg.display.update()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
