import pygame ,sys
from pygame.locals import * #load constants
red=[255,0,0]
pygame.init()
window=pygame.display.set_mode((1000,800))
pygame.display.set_caption('slither.eat -the snake game')
screen=pygame.display.get_surface()
screen.fill(red)
pygame.display.set_caption("snake")
pygame.display.flip()
while True:
      print("slither.eat-the snake game!")
      pass