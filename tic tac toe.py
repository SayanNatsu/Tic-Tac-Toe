import pygame, sys 
import numpy as np


#initialize pygame 
pygame.init()

# ----------
# CONSTANTS
# ----------

BG_COLOR = (102, 178, 255 )
LINE_COLOR = (0, 128, 255 ) 
RED = (255, 0, 0)
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CIRCLE_COLOR = (255, 255, 255)
CROSS_WIDTH = 25
SPACE = 50 
CROSS_COLOR = (66, 66, 66)
player = 1
game_over = False
top_font = pygame.font.Font("Abel.ttf", 25)
name_font = pygame.font.Font("Abel.ttf", 15)

#create the screen ( width , height )
screen = pygame.display.set_mode((600, 600))

#for the caption in title 
pygame.display.set_caption( 'TIC TAC TOE' )
screen.fill(BG_COLOR)

#creating a board of 3x3
board = np.zeros( (3, 3))
print(board)


def draw_lines():
    #1st horizontal line 
    pygame.draw.line(screen, LINE_COLOR, (50, 200 ), (550, 200 ), 10)
    #2nd horizontal line 
    pygame.draw.line(screen, LINE_COLOR, (50, 400 ), (550, 400 ), 10)
    #1st vertical line 
    pygame.draw.line(screen, LINE_COLOR, (200, 50 ), (200, 550 ), 10)
    #2nd vertical line 
    pygame.draw.line(screen, LINE_COLOR, (400, 50 ), (400, 550 ), 10)

draw_lines( )

def draw_figures():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 1: #for player 1 only 
                pygame.draw.circle(screen, CIRCLE_COLOR, (int( col * 200 + 100 ), int(row * 200 + 100)), CIRCLE_RADIUS, CIRCLE_WIDTH )
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + 200 - SPACE), (col * 200 + 200 - SPACE, row * 200 + SPACE), CROSS_WIDTH )
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + SPACE), (col * 200 + 200 - SPACE, row *200 + 200 - SPACE), CROSS_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col ):
    return board[row][col] == 0

def is_board_ful():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                return False
    return True

def check_win(player):
    #vertical win check
    for col in range (3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_win_line(col, player)
            return True

    #horizontal win check
    for row in range (3):
        if board[row][0] ==  player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_win_line(row, player)
            return True

    #asc diagonal win check (bottom left to top right)
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True

    #desc diagonal win check (top left to bottom right )
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True

    return False    #that means none of the above executed i.e no one won 

def draw_vertical_win_line(col, player):
    posX = col * 200 + 100
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (posX, 20), (posX, 600 - 20), 10)

def draw_horizontal_win_line(row, player):
    posY = row * 200 + 100
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (20, posY), (600 - 20, posY), 10)

def draw_asc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    
    pygame.draw.line(screen, color, (40, 600 - 40), (600 - 40, 40), 10)

def draw_desc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line (screen, color, (40, 40), (600 - 40, 600 - 40), 10)

def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    player = 1
    for row in range (3):
        for col in range (3):
            board[row][col] = 0

def top_text():
    top_text = top_font.render("PLAYER 1 is O  |  PLAYER 2 is X", True, (0, 0, 0))
    name_text = name_font.render("@ Sayan_Natsu", True,(0, 0, 0))
    screen.blit(top_text, (150,10))
    screen.blit(name_text, (490,570))


def game_over_text():
    pass
    

#mainloop
running = True
while running:

    #for holding the screen window
    for event in pygame.event.get():
        if event.type== pygame.QUIT :
            running = False
            
        
        top_text( )

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0] #x
            mouseY = event.pos[1] #y

            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            if available_square(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    if check_win(player):
                        game_over = True
                    player = 2
                
                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    if check_win(player):
                        game_over = True
                    player = 1
                
                draw_figures()

        #for restart        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:     #if keyword "r" is pressed 
                restart()
                game_over = False

    pygame.display.update()

    pass 