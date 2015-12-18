import sys,pygame

class Display:

    def __init__(self,width=800,height=600,bgcolor=(255,255,255),lineC=(0,0,0),Ocolor=(0,0,255),Xcolor=(255,0,0)):
        self.width=width
        self.height=height

        self.bgcolor=bgcolor
        self.O=Ocolor
        self.X=Xcolor
        self.lineC=lineC
        
        m=min(height,width)
        self.xStart=(width-m)/2
        self.yStart=(height-m)/2

        self.squareSize=m/3



        #initilize
        self.screen = pygame.display.set_mode((width, height))
        self.screen.fill(bgcolor)
        for i in xrange(1,3):
            x=self.xStart+self.squareSize*i
            y=self.yStart+self.squareSize*i

            pygame.draw.line(self.screen,lineC,(x,self.yStart),(x,height-self.yStart))
            pygame.draw.line(self.screen,lineC,(self.xStart,y),(width-self.xStart,y))

        pygame.display.flip()
        #

    def getCenter(self,col,row):#starting from top left row and col are 0
        return self.getTopLeft(col+.5,row+.5)

    def getTopLeft(self,col,row):
        X=self.xStart+col*self.squareSize
        Y=self.yStart+row*self.squareSize
        return (int(X),int(Y))

    def convert(self,x,y):
        x=x-self.xStart
        y=y-self.yStart
        if max(x,y)>min(self.width,self.height):
            return []
        if min(x,y)<0:
            return []

        return [x/self.squareSize,y/self.squareSize]
        
    def drawX(self,col,row):
        TL=self.getTopLeft(col,row)
        TR=(TL[0]+self.squareSize,TL[1])
        BR=(TR[0],TR[1]+self.squareSize)
        BL=(TL[0],TL[1]+self.squareSize)
        
        pygame.draw.line(self.screen,self.X,TR,BL)
        pygame.draw.line(self.screen,self.X,TL,BR)

    def drawO(self,col,row):
        pygame.draw.circle(self.screen, self.O, self.getCenter(col,row), self.squareSize/2,1)

    def update(self,move):
        if move[2]=='x':
            self.drawX(move[0],move[1])
        else:
            self.drawO(move[0],move[1])

        pygame.display.flip()

    def inCaseOfExit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()






        
