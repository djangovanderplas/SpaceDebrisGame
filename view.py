# Handles all events related to running pygame

import pygame, sys
# Colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

def checkEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def openwindow(xmax, ymax):
    """ Init pygame, set up window, return scr (window Surface) """
    scr = pygame.display.set_mode((xmax, ymax))
    return scr

def clr(scr):
    """Clears surface, fill with black"""
    scr.fill(black)
    return

def flip(fps, clock):
    """Flip (update) display"""
    clock.tick(fps)
    pygame.display.flip()
    return

def closewindow():
    """Close window, quit pygame"""
    pygame.quit()
    sys.exit()
    return
