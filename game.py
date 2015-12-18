import player
import minimax

class TicTacToe:
    playerList={'human':player,'minimax':minimax}
    def __init__(self,player1,player2,Display=None):
        self.board=[['','',''],['','',''],['','','']]

        self.player1=TicTacToe.playerList[player1].player(self,Display)
        self.player2=TicTacToe.playerList[player2].player(self,Display)

        self.currPlayer=1

    def checkForWin(self):#returns 'o' if o wins, 'x' if x wins 'tie' if tie and '' if not end state
        numFree=0
        testD1=''
        testD2=''
        for i in xrange(3):
            testD1+=self.board[i][i]
            testD2+=self.board[2-i][i]
            
            testH=''
            testV=''
            for j in xrange(3):
                if self.board[i][j]=='':
                    numFree+=1
                
                testH+=self.board[i][j]
                testV+=self.board[j][i]

            if testH=='ooo' or testV=='ooo':
                return 'o'
            if testH=='xxx' or testV=='xxx':
                return 'x'

        if testD1=='ooo' or testD2=='ooo':
            return 'o'
        if testD1=='xxx' or testD2=='xxx':
            return 'x'

        if numFree==0:
            return 'tie'

        return ''

    def check(self,board):#returns 'o' if o wins, 'x' if x wins 'tie' if tie and '' if not end state
        numFree=0
        testD1=''
        testD2=''
        for i in xrange(3):
            testD1+=board[i][i]
            testD2+=board[2-i][i]
            
            testH=''
            testV=''
            for j in xrange(3):
                if board[i][j]=='':
                    numFree+=1
                
                testH+=board[i][j]
                testV+=board[j][i]

            if testH=='ooo' or testV=='ooo':
                return 'o'
            if testH=='xxx' or testV=='xxx':
                return 'x'

        if testD1=='ooo' or testD2=='ooo':
            return 'o'
        if testD1=='xxx' or testD2=='xxx':
            return 'x'

        if numFree==0:
            return 'tie'

        return ''

    def getMove(self):
        if self.currPlayer==1:
            move=self.player1.getMove()
            self.currPlayer=2
            move.append('x')
        else:
            move=self.player2.getMove()
            self.currPlayer=1
            move.append('o')

        self.board[move[0]][move[1]]=move[2]
        return move

    def isLegal(self,move):
        return self.board[move[0]][move[1]]==''
        
