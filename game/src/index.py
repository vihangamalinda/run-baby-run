import pygame
import sys

# Initialize pygame
pygame.init()
WIDTH = 1280
HEIGHT = 720
TITLE = "Run Baby Run"
MAX_FRAME_RATE = 60
font_path = "../assets/font/04B_30__.TTF"
slime_one_path = "../assets/Slime/slime1_left_walk.png"
test_font = pygame.font.Font(font_path, 50)

# Display surface
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# regular surface
sky_surface = pygame.image.load('../assets/sky.png').convert()
ground_surface = pygame.image.load("../assets/ground.png").convert()
slime_surface = pygame.image.load(slime_one_path).convert_alpha()

pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()
test_surface = test_font.render(TITLE, True, "dark blue")

slime_x = WIDTH
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if slime_x < -100:
            slime_x = WIDTH

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 420))
    screen.blit(test_surface, (400, 100))
    screen.blit(slime_surface, (slime_x, 400))
    slime_x = slime_x - 5

    pygame.display.update()
    clock.tick(MAX_FRAME_RATE)
