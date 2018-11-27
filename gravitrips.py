import sys
import os

game = [['.' for i in range(0,7)] for i in range(0,6)]

def printGame():
	os.system('cls' if os.name == 'nt' else 'clear')
	for j in range(0,7):
		print (j+1),
	print ''
	for i in range(0,6):
		for j in range(0,7):
			print game[i][j],
		print ''

def gameOver(winner):
	if winner==1:
		print 'Player 1 won the game!'
	elif winner==2:
		print 'Player 2 won the game!'
	else:
		print 'The game ended in a tie.'

def lowestRow(column):
	for i in range(5,-1,-1):
		if game[i][column]=='.':
			return i
	return 6

def checkWinner():
	for i in range(0,6):
		# check for a horizontal line 
		for j in range(0,4):
			if game[i][j]=='X' and game[i][j+1]=='X' and game[i][j+2]=='X' and game[i][j+3]=='X':
				return 1
			elif game[i][j]=='O' and game[i][j+1]=='O' and game[i][j+2]=='O' and game[i][j+3]=='O':
				return 2

	for i in range(0,3):
		# check for a vertical line
		for j in range(0,7):
			if game[i][j]=='X' and game[i+1][j]=='X' and game[i+2][j]=='X' and game[i+3][j]=='X':
				return 1
			elif game[i][j]=='O' and game[i+1][j]=='O' and game[i+2][j]=='O' and game[i+3][j]=='O':
				return 2

		# check for a backward up diagonal
		for j in range(0,4):
			if game[i][j]=='X' and game[i+1][j+1]=='X' and game[i+2][j+2]=='X' and game[i+3][j+3]=='X':
				return 1
			elif  game[i][j]=='O' and game[i+1][j+1]=='O' and game[i+2][j+2]=='O' and game[i+3][j+3]=='O':
				return 2

	# check for a forward up diagonal
	for i in range(3,6):
		for j in range(0,4):
			if game[i][j]=='X' and game[i-1][j+1]=='X' and game[i-2][j+2]=='X' and game[i-3][j+3]=='X':
				return 1
			elif game[i][j]=='O' and game[i-1][j+1]=='O' and game[i-2][j+2]=='O' and game[i-3][j+3]=='O':
				return 2

	return 0

def twoPlayer():
	winner = 0
	move = 1
	moveCount = 0
	invalidMove=0
	while(moveCount<42):
		printGame()
		if invalidMove==1:
			print "Invalid move. Try again."
		print "Player",move,"please enter a column number (1-7) : ",
		column = int(raw_input(),10)-1
		if(game[0][column]!='.'):
			invalidMove=1
			continue
		else:
			invalidMove=0
			row = lowestRow(column)
			if move==1:
				game[row][column] = 'X'
			else:
				game[row][column] = 'O'
			moveCount += 1
			move = (move%2)+1
			winner = checkWinner()
			if winner!=0:
				break
	printGame()
	gameOver(winner)

if __name__ == '__main__':
	# Syntax : gravitrips.py [-p1/-p2] [-d1_-d10]
	if(len(sys.argv)==3 and sys.argv[1]=='-p1'):
		level = int(sys.argv[2][2:],10)
		if(level<1 or level>10):
			print "Difficulty level has to be between 1 and 10."
		else:
			print "single player with difficulty level",sys.argv[2][2:]
	elif(len(sys.argv)==2 and sys.argv[1]=='-p1'):
		print "single player with difficulty level",5
	elif(len(sys.argv)==2 and sys.argv[1]=='-p2'):
		print "two-player"
		twoPlayer()
	else:
		print "Invalid syntax."
		print "Usage : gravitrips.py { -p1 [ -d<level from 1 - 10>] | -p2 }"