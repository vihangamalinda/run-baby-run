import logging

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
slime_surface_rect = slime_surface.get_rect(midbottom=(WIDTH/2, 665))
user_surface = pygame.image.load("../assets/user/user_walk.png").convert_alpha()
user_surface_rect = user_surface.get_rect(midbottom=(50, 665))

pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()
test_surface = test_font.render(TITLE, True, "dark blue")
test_surface_rect = test_surface.get_rect(center=(WIDTH / 2, 250))
print(ground_surface.get_height())
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 420))
    screen.blit(test_surface, test_surface_rect)
    screen.blit(slime_surface, slime_surface_rect)
    screen.blit(user_surface, user_surface_rect)
    # slime_x = slime_x - 5
    slime_surface_rect.left -=3
    user_surface_rect.left +=3
    if slime_surface_rect.right <0:
        slime_surface_rect.left = WIDTH

    if user_surface_rect.left >WIDTH :
        user_surface_rect.left =0


    pygame.display.update()
    clock.tick(MAX_FRAME_RATE)
