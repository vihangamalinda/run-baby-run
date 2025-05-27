import  pygame
import sys

from pygame.examples.grid import TITLE

# Initialize pygame
pygame.init()
WIDTH =800
HEIGHT =400
TITLE ="Run Baby Run"
MAX_FRAME_RATE =60

# Display surface
screen =pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Draw all our objects
    #update everything
    pygame.display.update()
    clock.tick(MAX_FRAME_RATE)