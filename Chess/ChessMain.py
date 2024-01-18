"""
This is our mian driver file. It will be responsible for handling user input and dsiplaying current GameState object
"""
import pygame as p
import ChessEngine


p.init()

WIDTH = 512
HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT/DIMENSION
MAX_FPS = 15
IMAGES = {}


"""
initilize a global dictionary of images
Will be caled only once in the main
"""
def loadImages():
    pieces = ["wp", "wR", "wN", "wB", "wK", "wQ","bp", "bR", "bN", "bB", "bK", "bQ"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE,SQ_SIZE))
        # we can now access an image by saying: IMAGES["wp"]

'''
the main driver will handle user input and updating graphics
'''

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages() # only load images once
    running = True
    sqSelected = () # keep track of the last click of the user, (tuple: (row,col))
    playerClicks = [] # keep track of the player clicks two tuples: [(6,5), (4,4)] [(first click), second click)]
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos # (x,y) location of mouse
                col = location[0] // SQ_SIZE # double divide to get integers
                row = location[1] // SQ_SIZE
                if sqSelected == (row,col): # check if user clicked the same square twice, this is typically to undo
                    sqSelected = () # deselect if we select the same square twice
                    playerClicks = [] # clear player click
                else:
                    sqSelected = (row,col)
                    playerClicks.append(sqSelected) # append for both 1st and 2nd clicks
                if len(playerClicks) == 2: #after the 2nd click, now we want to make our move!
                    


                
        drawGameState(screen, gs) # include this
        clock.tick(MAX_FPS)
        p.display.flip()
        

'''
Responsible for all graphics within a current game state
'''

def drawGameState(screen,gs):
    drawBoard(screen) # draw the squres on the board
    # add in piece highlightling / move suggestions
    drawPieces(screen,gs.board) # draw the oieces on top of the squares

'''
Draw the squares on the board
'''
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("dark green")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c)%2)] # clever way to generate alternate colors
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE,SQ_SIZE))
    
'''
Draw the pieces on the board using the current GameState.board
we could include this in the for loop above pretty easily
'''
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--": # not an empty square then draw piece
                screen.blit(IMAGES[piece],p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE,SQ_SIZE))
                
    
    

if __name__ == "__main__":
    main()









