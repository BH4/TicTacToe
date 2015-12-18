import pygame

class player:
    def __init__(self,game,display):
        self.game=game
        self.display=display
        
    def getMove(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    x,y=pygame.mouse.get_pos()

                    move=self.display.convert(x,y)

                    l=self.game.isLegal(move)

                    if l:
                        return move


            
            
