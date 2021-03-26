import pygame, sys

pygame.init()

#GameBoard/Board Constants 
WIDTH = 600
HEIGHT = 600
LINE_WIDTH= 10

#color constants in rgb format (https://www.google.com/search?q=rgb+color+picker&oq=rgb+color+picker&aqs=chrome..69i57j0j0i20i263j0l7.3543j0j7&sourceid=chrome&ie=UTF-8)
LineColor = (0,0,0)
BackGroundColor =(50, 109, 168)


GameBoard = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
GameBoard.fill( BackGroundColor )
#pass in arguments, GameBoard, line color, and the starting point of a line using a tupal and the ending point for the line

#TEST DRAW LINE________
# pygame.draw.line(GameBoard, LineColor, (10, 10), (300, 300), 10)

#DRAW BOARD LINES _________
def draw_lines():
    #draw tic tac toe board lines

    #first horizontal line
    pygame.draw.line(GameBoard, LineColor, (0,200), (600, 200), LINE_WIDTH)
    #second horizontal line
    pygame.draw.line(GameBoard, LineColor, (0,400), (600, 400), LINE_WIDTH)

    #first virtical line
    pygame.draw.line(GameBoard, LineColor, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(GameBoard, LineColor, (400, 0), (400, 600), LINE_WIDTH)

draw_lines()

#mainLoop
while True: 
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()

    pygame.display.update()
