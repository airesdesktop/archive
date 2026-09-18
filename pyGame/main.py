import sys # import sys
import pygame # import pygame

pygame.init() # Init
pygame.display.set_caption('pygame_tutorial01') # set window name
display = pygame.display.set_mode((640, 480)) # display var.
clock = pygame.time.Clock() # clock var.

while True: # main loop
    for event in pygame.event.get(): # go through the events
        if event.type == pygame.QUIT: # if player quits
            pygame.quit() # quit pygame
            sys.exit() # exit aplication
        
    pygame.display.update() # update display
    clock.tick(60) # limit fps