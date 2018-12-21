import numpy as np
import pygame
import sys
import math
import random

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
ROW_COUNT=COLUMN_COUNT = int(raw_input("Enter size of the Light board: "))
SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE
size = (width, height)
RADIUS = int(SQUARESIZE/2 - 5)
nmoves=0
mxmoves=0




def create_board():
	board=np.zeros((ROW_COUNT*COLUMN_COUNT))
	ic=random.sample(range(0,ROW_COUNT*COLUMN_COUNT),ROW_COUNT)
	board[ic]=1
	board.shape =((ROW_COUNT,COLUMN_COUNT))
	return board

def findminmoves(board):
	ic=board[:]
	ic.shape=(ROW_COUNT*COLUMN_COUNT)

def draw_board(board):
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):
			pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
			pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)

	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):
			if board[r][c] == 1:
				pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
	pygame.display.update()



if __name__=="__main__":
	board = create_board()
	effmoves=findeffmoves()
	mxmoves=findminmoves(effmoves,board)
	game_over = False
	pygame.init()
	screen = pygame.display.set_mode(size)
	pygame.display.update()
	myfont = pygame.font.SysFont("monospace", 75)

	while not game_over:
		draw_board(board)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			pygame.display.update()
			if event.type == pygame.MOUSEBUTTONDOWN:
				nmoves+=1
				x=(event.pos[1]-100)/100
				y=event.pos[0]/100
				board[x][y]=(board[x][y]+1)%2
				if x-1>=0:
					board[x-1][y]=(board[x-1][y]+1)%2
				if y-1>=0:
					board[x][y-1]=(board[x][y-1]+1)%2
				if x+1<ROW_COUNT:
					board[x+1][y]=(board[x+1][y]+1)%2
				if y+1<COLUMN_COUNT:
					board[x][y+1]=(board[x][y+1]+1)%2
				draw_board(board)
