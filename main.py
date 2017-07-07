import sys,pygame
from Display import Display
from game import TicTacToe
from time import sleep

waitTime=.1

board=Display()
game=TicTacToe('human','minimax',Display=board)

win=''
while win=='':
    board.inCaseOfExit()

    #try:
    move=game.getMove()
    win=game.checkForWin()
    sleep(waitTime)

    board.update(move)
    #except:
    #    print 'broken'
    #    pygame.quit()
    #    sys.exit()

if win=='o':
    print 'O wins'
elif win=='x':
    print 'X wins'
else:
    print 'Tie'


pygame.quit()
sys.exit()
