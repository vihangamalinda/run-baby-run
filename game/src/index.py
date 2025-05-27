import pygame
import sys

# Initialize pygame
pygame.init()
WIDTH = 800
HEIGHT = 400
TITLE = "Run Baby Run"
MAX_FRAME_RATE = 60

# Display surface
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# regular surface
test_surface = pygame.Surface((100, 200))
test_surface.fill("red")

pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(test_surface, (200, 100))
    pygame.display.update()
    clock.tick(MAX_FRAME_RATE)
