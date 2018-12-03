import sys
import os
from random import randint

game = [['.' for i in range(0, 7)] for i in range(0, 6)]


def printGame():
	# To clear screen every time the game is printed.
    os.system('cls' if os.name == 'nt' else 'clear')

    for j in range(0, 7):
        print(j+1),
    print ''
    for i in range(0, 6):
        for j in range(0, 7):
            print game[i][j],
        print ''


def gameOverTwoPlayer(winner):
    if winner == 1:
        print 'Player 1 won the game!'
    elif winner == 2:
        print 'Player 2 won the game!'
    else:
        print 'The game ended in a tie.'


def gameOverSinglePlayer(winner):
    if winner == 1:
        print 'Congratulations human, you won the game!'
    elif winner == 2:
        print 'Computer won the game!'
    else:
        print 'The game ended in a tie.'


def lowestRow(column):
    for i in range(5, -1, -1):
        if game[i][column] == '.':
            return i
    return 6


def checkWinner():
    for i in range(0, 6):
        # check for a horizontal line
        for j in range(0, 4):
            if game[i][j] == 'X' and game[i][j+1] == 'X' and game[i][j+2] == 'X' and game[i][j+3] == 'X':
                return 1
            elif game[i][j] == 'O' and game[i][j+1] == 'O' and game[i][j+2] == 'O' and game[i][j+3] == 'O':
                return 2

    for i in range(0, 3):
        # check for a vertical line
        for j in range(0, 7):
            if game[i][j] == 'X' and game[i+1][j] == 'X' and game[i+2][j] == 'X' and game[i+3][j] == 'X':
                return 1
            elif game[i][j] == 'O' and game[i+1][j] == 'O' and game[i+2][j] == 'O' and game[i+3][j] == 'O':
                return 2

        # check for a backward up diagonal
        for j in range(0, 4):
            if game[i][j] == 'X' and game[i+1][j+1] == 'X' and game[i+2][j+2] == 'X' and game[i+3][j+3] == 'X':
                return 1
            elif game[i][j] == 'O' and game[i+1][j+1] == 'O' and game[i+2][j+2] == 'O' and game[i+3][j+3] == 'O':
                return 2

    # check for a forward up diagonal
    for i in range(3, 6):
        for j in range(0, 4):
            if game[i][j] == 'X' and game[i-1][j+1] == 'X' and game[i-2][j+2] == 'X' and game[i-3][j+3] == 'X':
                return 1
            elif game[i][j] == 'O' and game[i-1][j+1] == 'O' and game[i-2][j+2] == 'O' and game[i-3][j+3] == 'O':
                return 2

    return 0


def twoPlayer():
    winner = 0
    move = 1
    moveCount = 0
    invalidMove = 0
    while(moveCount < 42):
        printGame()
        if invalidMove == 1:
            print "Invalid move. Try again."
        print "Player", move, "please enter a column number (1-7) : ",
        column = int(raw_input(), 10)-1
        if(game[0][column] != '.'):
            invalidMove = 1
            continue
        else:
            invalidMove = 0
            row = lowestRow(column)
            if move == 1:
                game[row][column] = 'X'
            else:
                game[row][column] = 'O'
            moveCount += 1
            move = (move % 2)+1
            winner = checkWinner()
            if winner != 0:
                break
    printGame()
    gameOverTwoPlayer(winner)


def sum(scores):
    sum = 0
    for i in range(0, len(scores)):
        sum += scores[i]
    return sum


def calculateScore(depth, move):
    score = [0 for i in range(0, 7)]
    if depth == 1:
        for i in range(0, 7):
            if game[0][i] != '.':
                continue
            row = lowestRow(i)
            if move == 1:
                game[row][i] = 'X'
            else:
                game[row][i] = 'O'
            winner = checkWinner()
            game[row][i] = '.'
            if winner == 2:
                score[i] = 1
            elif winner == 1:
                score[i] = -1
        return score
    else:
        for i in range(0, 7):
            if game[0][i] != '.':
                continue
            row = lowestRow(i)
            if move == 1:
                game[row][i] = 'X'
            else:
                game[row][i] = 'O'
            winner = checkWinner()
            if(winner == 1):
                score[i] = -pow(10, depth-1)
                game[row][i] = '.'
                continue
            elif(winner == 2):
                score[i] = pow(10, depth-1)
                game[row][i] = '.'
                continue
            score[i] = sum(calculateScore(depth-1, (move % 2)+1))
            game[row][i] = '.'

        return score


def bestMove(depth, move):
    score = calculateScore(depth, move)
    orig = list(score)
    flag = 0
    score.sort(reverse=True)
    c = 0
    ret = orig.index(score[c])
    while(game[0][ret] != '.'):
        c += 1
        ret = orig.index(score[c])
    return ret


def cpuMove():
    depth = 6
    move = bestMove(depth, 2)
    return move


def singlePlayer(level):
    winner = 0
    move = 1
    moveCount = 0
    invalidMove = 0
    while(moveCount < 42):
        printGame()
        if invalidMove == 1:
            print "Invalid move. Try again."
        if move == 1:
            print "Dear human, please enter a column number (1-7) : ",
            column = int(raw_input(), 10)-1
        else:
            print "Computer is thinking..."
            column = cpuMove()
        if(game[0][column] != '.'):
            invalidMove = 1
            continue
        else:
            invalidMove = 0
            row = lowestRow(column)
            if move == 1:
                game[row][column] = 'X'
            else:
                game[row][column] = 'O'
            moveCount += 1
            move = (move % 2)+1
            winner = checkWinner()
            if winner != 0:
                break
    printGame()
    gameOverSinglePlayer(winner)


if __name__ == '__main__':
    if(len(sys.argv) == 3 and sys.argv[1] == '-p1'):
        level = int(sys.argv[2][2:], 10)
        if(level < 1 or level > 10):
            print "Difficulty level has to be between 1 and 10."
        else:
            singlePlayer(sys.argv[2][2:])
    elif(len(sys.argv) == 2 and sys.argv[1] == '-p1'):
        singlePlayer(5)
    elif(len(sys.argv) == 2 and sys.argv[1] == '-p2'):
        twoPlayer()
    else:
        print "Invalid syntax."
        print "Usage : gravitrips.py { -p1 [ -d<level from 1 - 10>] | -p2 }"
