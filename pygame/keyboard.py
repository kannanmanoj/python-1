import pygame, sys
from pygame.locals  import *
catx = 10
caty = 10
screen = 0

def myquit():
    pygame.quit() 
    Sys.exit(0)
    
def check_inputs(events):
    global catx,caty,screen
    for event in events:
        if event.type == QUIT:
            quit()
        else:
           if event.type == KEYDOWN:
               if event.key == K_ESCAPE:
                  myquit()
               elif event.key == K_LEFT:
                     catx -=5
                     print("move rect left")
               elif event.key == K_RIGHT:
                     caty +=5
                     print("move rect right ")
               else:
                    print (event.key)

    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,255,255),catx(50,50,10))
    pygame.display.update()

def main():
     global screen
     pygame.init()
     screen_width = 600
     screen_height = 480
     window = pygame.display.set_mode((screen_width,screen_height))
     pygame.display.set_caption('slither.eat-the snake game')
     screen = pygame.display.get_surface()

     pygame.display.update()  

     while True:
        check_inputs(pygame.event.get())


main()




















	 
	
	   
	   