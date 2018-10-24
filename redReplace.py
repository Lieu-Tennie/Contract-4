import pygame, sys
from pygame.locals import *

WINDOWHEIGHT = 400
WINDOWWIDTH = 300
DISPLAYSURF = pygame.display.set_mode((WINDOWHEIGHT, WINDOWWIDTH))
FPSCLOCK = pygame.time.Clock()
FPS = 30
RED = (255, 0, 0)

def main(): # main game loop
    pygame.init()
    halfRed = False
    bad_boii_up = pygame.image.load("BadBoiUp.PNG")
    bad_boii_up.convert()
    while True:
        DISPLAYSURF.blit(bad_boii_up, (0,0,WINDOWWIDTH, WINDOWHEIGHT))
        if halfRed == False:
            decreaseRed(bad_boii_up)
            halfRed = True

        checkForQuit()
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def checkForQuit():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

def decreaseRed(picture):
    picWidth, picHeight = picture.get_size()
    pxArray = pygame.PixelArray(picture)
    for x in range(0, picWidth):
        for y in range(0, picHeight):
            red = picture.get_at((x,y)).r
            green = picture.get_at((x, y)).g
            blue = picture.get_at((x, y)).b
            red = int(red/2)
            pxArray[x, y] = (red, green, blue)


if __name__ == '__main__':
    main()
