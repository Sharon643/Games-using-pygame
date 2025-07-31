import pygame, sys
import numpy as np

pygame.init()
WIDTH=600
HEIGHT=600
LINE_WIDTH=15
bg_color=(157, 193, 131)
line_color=(128, 128, 128)
cross_color=(249,245,236)
white=(255,0,0)
space=55
board_rows=3
board_cols=3
player=1
game_over=False
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("TicTacToe")
screen.fill(bg_color)
board=np.zeros((board_rows,board_cols))
def draw_lines():
    #1st horizontal line
    pygame.draw.line(screen,line_color,(0,200),(600,200),LINE_WIDTH)
    #2nd horizontal line
    pygame.draw.line(screen,line_color,(0,400),(600,400),LINE_WIDTH)
    #1st vertical line
    pygame.draw.line(screen,line_color,(200,0),(200,600),LINE_WIDTH)
    #2nd vertical line
    pygame.draw.line(screen,line_color,(400,0),(400,600),LINE_WIDTH)
def mark_square(row,col,player):
    board[row][col]=player

def is_square_available(row,col):
    if board[row][col]==0:
        return True
    else:
        return False
def is_board_full():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col]==0:
                return False
    return True 
def draw_figures():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col]==1:
                pygame.draw.circle(screen,cross_color,(int(col*200+100),int(row*200+100)),55,15) 
            elif board[row][col]==2:
                pygame.draw.line(screen,cross_color,(col*200+space,row*200+200-space),(col*200+200-space,row*200+space),25) 
                pygame.draw.line(screen,cross_color,(col*200+space,row*200+space),(col*200+200-space,row*200+200-space),25)
def check_win(player):
    #vertical win check
    for col in range(board_cols):
        if board[0][col]==player and board[1][col]==player and board[2][col]==player:
            draw_vertical_win_line(col,player)
            return True
    #horizontal win check
    for row in range(board_rows):
        if board[row][1]==player and board[row][1]==player and board[row][2]==player:
            draw_horizontal_winning_line(row,player)
            return True
    #diagonal win check asc
    if board[2][0]==player and board[1][1]==player and board[0][2]==player:
        draw_asc_diag_line(player)
        return True
    #diagonal win check desc
    if board[0][0]==player and board[1][1]==player and board[2][2]==player:
        draw_desc_diag_line(player)
        return True
    return False
def draw_vertical_win_line(col,player):
    posX=col*200+100
    pygame.draw.line(screen,cross_color,(posX,15),(posX,HEIGHT-15),15)
def draw_horizontal_winning_line(row,player):
    posY=row*200+100
    pygame.draw.line(screen,cross_color,(15,posY),(WIDTH-15,posY),15)
def draw_asc_diag_line(player):
    pygame.draw.line(screen,cross_color,(15,HEIGHT-15),(WIDTH-15,15),15)
def draw_desc_diag_line(player):
    pygame.draw.line(screen,cross_color,(15,15),(WIDTH-15,HEIGHT-15),15)
def restart():
    global player, game_over
    screen.fill(bg_color)
    draw_lines()
    player=1
    game_over=False
    for row in range(board_rows):
        for col in range(board_cols):
            board[row][col]=0
draw_lines()
# for row in range(board_rows):
#         for col in range(board_cols):
#             if board[row][col]==0:
#                 mark_square(row,col,1) 
# print(board)
# print(is_board_full())
#mainloop
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        
        if event.type==pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX=event.pos[0]
            mouseY=event.pos[1]

            clicked_row=int(mouseY//200)
            clicked_col=int(mouseX//200)
        
            if is_square_available(clicked_row,clicked_col):
                if player==1:
                    mark_square(clicked_row,clicked_col,1)
                    if check_win(player):
                        game_over=True
                    player=2
                elif player==2:
                    mark_square(clicked_row,clicked_col,2)
                    if check_win(player):
                        game_over=True
                    player=1
                draw_figures()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_r:
                restart()
        if game_over:
            font = pygame.font.SysFont("monospace", 25, bold=True)
            if player == 2:
                win_msg = font.render("Player 1 wins", True, white)
            else:
                win_msg = font.render("Player 2 wins", True, white)
            restart_msg = font.render("Press R to restart", True, white)
            screen.blit(win_msg, (WIDTH//2 - win_msg.get_width()//2, HEIGHT//2 - 40))
            screen.blit(restart_msg, (WIDTH//2 - restart_msg.get_width()//2, HEIGHT//2 + 10))
    pygame.display.update()