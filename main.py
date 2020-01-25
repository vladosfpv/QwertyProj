import pygame
import sys

pygame.init()

pygame.display.set_mode((600, 400))

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()