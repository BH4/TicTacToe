import sys,pygame
from Display import Display
from game import TicTacToe
from time import sleep

waitTime=0.5

for i in xrange(10):
    board=Display()
    game=TicTacToe('minimax','minimax',Display=board)

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

    waitTime/=2.

pygame.quit()


sleep(2)
print 'Greetings, Professor Falken.'
sleep(2)
print 'A strange game. The only winning move is not to play. How about a nice game of chess?'
sys.exit()
