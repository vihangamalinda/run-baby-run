import  pygame
import sys

from pygame.examples.grid import TITLE

# Initialize pygame
pygame.init()
WIDTH =800
HEIGHT =400
TITLE ="Run Baby Run"

# Display surface
screen =pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Draw all our objects
    #update everything
    pygame.display.update()