import pygame
import sys

# Initialize pygame
pygame.init()
WIDTH = 1280
HEIGHT = 720
TITLE = "Run Baby Run"
MAX_FRAME_RATE = 60
GROUND_LEVEL = 665
USER_OFFSET =30
SLIME_OFFSET = 55

font_path = "../assets/font/04B_30__.TTF"
slime_one_path = "../assets/Slime/slime1_left_walk.png"
test_font = pygame.font.Font(font_path, 50)

# Display surface
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# regular surface
sky_surface = pygame.image.load('../assets/sky.png').convert()
ground_surface = pygame.image.load("../assets/ground.png").convert()
slime_surface = pygame.image.load(slime_one_path).convert_alpha()
slime_surface_scaled  =pygame.transform.scale(slime_surface,(slime_surface.get_width()*3,slime_surface.get_width()*3))
slime_surface_rect = slime_surface_scaled.get_rect(midbottom=(WIDTH, GROUND_LEVEL + SLIME_OFFSET))

user_surface = pygame.image.load("../assets/user/user_walk.png").convert_alpha()
print(user_surface.get_height(),user_surface.get_width())
user_surface_scaled = pygame.transform.scale(user_surface,(user_surface.get_width()*3,user_surface.get_height()*3))
user_surface_rect = user_surface_scaled.get_rect(midbottom=(50, GROUND_LEVEL+USER_OFFSET))
print(user_surface_scaled.get_height(),user_surface_scaled.get_width())

user_gravity = 0
game_active = True

pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()
test_surface = test_font.render(TITLE, True, "dark blue")
test_surface_rect = test_surface.get_rect(center=(WIDTH / 2, 250))
start_time_milli = 0


def get_timer_surface():
    current_time = int((pygame.time.get_ticks() - start_time_milli) / 1000)
    timer_surface = test_font.render(f"{current_time}", True, "red")
    timer_surface_rec = timer_surface.get_rect(center=(WIDTH / 2, 100))
    screen.blit(timer_surface, timer_surface_rec)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game_active:
                if event.key == pygame.K_SPACE and user_surface_rect.bottom == (GROUND_LEVEL+USER_OFFSET):
                    user_gravity = -30
            else:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    start_time_milli = pygame.time.get_ticks()

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 420))
        pygame.draw.rect(screen, "yellow", test_surface_rect)
        pygame.draw.rect(screen, "yellow", test_surface_rect, 20, 30)
        pygame.draw.rect(screen, "yellow", user_surface_rect, 20, 30)
        screen.blit(test_surface, test_surface_rect)
        screen.blit(slime_surface, slime_surface_rect)
        screen.blit(slime_surface_scaled, slime_surface_rect)
        pygame.draw.rect(screen,"red",slime_surface_rect,20,30)
        get_timer_surface()

        # slime_x = slime_x - 5
        slime_surface_rect.left -= 1
        user_surface_rect.left += 1
        if slime_surface_rect.right < 0:
            slime_surface_rect.left = WIDTH

        if user_surface_rect.left > WIDTH:
            user_surface_rect.left = 0

        # if user_surface_rect.bottom <GROUND_LEVEL:
        #     user_surface_rect.bottom += 2

        user_gravity += 1
        user_surface_rect.y += user_gravity

        if user_surface_rect.bottom > GROUND_LEVEL +USER_OFFSET:
            user_surface_rect.bottom = GROUND_LEVEL+USER_OFFSET

        screen.blit(user_surface_scaled, user_surface_rect)
        if slime_surface_rect.collidepoint(user_surface_rect.midbottom):
            game_active = False

    else:
        print("GAME OVER")

    pygame.display.update()
    clock.tick(MAX_FRAME_RATE)
