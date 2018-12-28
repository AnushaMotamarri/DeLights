import numpy as np
import pygame
import sys
import math
import random
import time
from numpy.linalg import inv
from copy import deepcopy
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
	board=np.zeros((ROW_COUNT*COLUMN_COUNT),dtype=int)
	ic=random.sample(range(0,ROW_COUNT*COLUMN_COUNT),4)
	board[ic]=1
	board.shape =((ROW_COUNT,COLUMN_COUNT))
	return ic,board




def findeffmoves():
	k=0
	m=np.zeros((ROW_COUNT*COLUMN_COUNT,ROW_COUNT*COLUMN_COUNT),dtype=int)
	for i in range(ROW_COUNT):
		for j in range(COLUMN_COUNT):
			b=np.zeros((ROW_COUNT,COLUMN_COUNT))
			b[i][j]=1
			if i-1>=0:
				b[i-1][j]=1
			if i+1<ROW_COUNT:
				b[i+1][j]=1
			if j-1>=0:
				b[i][j-1]=1
			if j+1<COLUMN_COUNT:
				b[i][j+1]=1
			b.shape=((ROW_COUNT*COLUMN_COUNT))
			m[k]=b
			k+=1
	return m




def findminmoves(effmoves,board):
	ic=board[:]

	ic.shape=(ROW_COUNT*COLUMN_COUNT)
	ainv=[[ 1, 0, 1, 0, 0, 1, 1, 1, 0],
		  [ 0, 0, 0, 0, 1, 0, 1, 1, 1],
		  [ 1, 0, 1, 1, 0, 0, 0, 1, 1],
		  [ 0, 0, 1, 0, 1, 1, 0, 0, 1],
		  [ 0, 1, 0, 1, 1, 1, 0, 1, 0],
		  [ 1, 0, 0, 1, 1, 0, 1, 0, 0],
		  [ 1, 1, 0, 0, 0, 1, 1, 0, 1],
		  [ 1, 1, 1, 0, 1, 0, 0, 0, 0],
		  [ 0, 1, 1, 1, 0, 0, 1, 0, 1]]
	ans=np.dot(ainv,ic)%2
	minmoves= sum(ans)
	return ans,minmoves




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
	ic,board = create_board()
	bf=deepcopy(board)
	effmoves=findeffmoves()
	ans,mxmoves=findminmoves(effmoves,board)
	print "max moves= "+str(mxmoves)
	game_over = False
	pygame.init()
	screen = pygame.display.set_mode(size)
	pygame.display.update()
	myfont = pygame.font.SysFont("monospace", 75)
	draw_board(board)
	while not game_over:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			pygame.display.update()
			if event.type == pygame.MOUSEBUTTONDOWN:
				nmoves+=1
				print str(mxmoves-nmoves) + " moves left"
				if nmoves>=mxmoves:
					#print "here"
					bg=pygame.image.load('GO.png')
					screen= pygame.display.set_mode(size)
					screen.fill((0,0,0))
					screen.blit(bg,(SQUARESIZE/2,SQUARESIZE/2))

					print ans
					
				else:
					draw_board(board)
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
