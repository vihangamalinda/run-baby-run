import pygame
import sys

# Initialize pygame
pygame.init()
WIDTH = 1280
HEIGHT = 720
TITLE = "Run Baby Run"
MAX_FRAME_RATE = 60

# Display surface
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# regular surface
sky_surface = pygame.image.load('../assets/sky.png')
ground_surface = pygame.image.load("../assets/ground.png")

pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 420))

    pygame.display.update()
    clock.tick(MAX_FRAME_RATE)
