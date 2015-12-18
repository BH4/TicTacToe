from copy import deepcopy


def children(node):#node contains a copy of the board and the current player
    #children returns possible move possitions
    c=[]
    
    board=node[0]
    for i in xrange(3):
        for j in xrange(3):
            if board[i][j]=='':
                c.append((i,j))
    return c
    
def otherID(ID):
    if ID=='x':
        return 'o'
    return 'x'

class player:
    def __init__(self,game,display):
        self.game=game
        self.display=display

        self.id=''

    def getMove(self):
        d=self.game.currPlayer
        if d==1:
            self.id='x'
        else:
            self.id='o'
        
        return self.minimax()



    def minimax(self):
        node=(self.game.board,self.id)
        depth=100
        alpha=-10**8
        beta=10**8
        
        kids=children(node)

        val=-10**7
        best=None
        for child in kids:
            board=deepcopy(node[0])
            board[child[0]][child[1]]=node[1]

            ab=self.alphabeta((board,otherID(node[1])),depth-1,alpha,beta,False)

            if val<ab:
                best=child
                val=ab
            
            alpha=max(alpha,val)
            if beta<=alpha:
                break
        
        return [best[0],best[1]]

        

    def alphabeta(self,node,depth,alpha,beta,maximizingPlayer):
        if depth==0:
            return None
        
        win=self.game.check(node[0])
        if not win=='':
            if win==self.id:
                return 10**5
            elif win=='tie':
                return 0
            else:
                return -10**5

        kids=children(node)
        if maximizingPlayer:
            val=-10**7
            for child in kids:
                board=deepcopy(node[0])
                board[child[0]][child[1]]=node[1]
                val=max(val,self.alphabeta((board,otherID(node[1])),depth-1,alpha,beta,False))
                alpha=max(alpha,val)
                if beta<=alpha:
                    break
            return val
        else:
            val=10**7
            for child in kids:
                board=deepcopy(node[0])
                board[child[0]][child[1]]=node[1]
                val=min(val,self.alphabeta((board,otherID(node[1])),depth-1,alpha,beta,True))
                beta=min(beta,val)
                if beta<=alpha:
                    break
            return val















        
        
