import pygame
import sys
from random import randint

# Initialize pygame
pygame.init()

WIDTH = 1280
HEIGHT = 720
TITLE = "Run Baby Run"
MAX_FRAME_RATE = 60
GROUND_LEVEL = 665
USER_OFFSET = 30
SLIME_OFFSET = 30
BIRD_OFFSET = -315
USER_X_POSITION = 120

font_path = "../assets/font/04B_30__.TTF"
slime_one_path = "../assets/Slime/slime1_left_walk.png"
test_font = pygame.font.Font(font_path, 50)
font_size_30 = pygame.font.Font(font_path, 30)
font_size_15 = pygame.font.Font(font_path, 15)

# Display surface
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# regular surface
sky_surface = pygame.image.load('../assets/sky.png').convert()
ground_surface = pygame.image.load("../assets/ground.png").convert()

# Obstacles
slime_surface = pygame.image.load(slime_one_path).convert_alpha()
slime_surface_scaled = pygame.transform.scale(slime_surface,
                                              (slime_surface.get_width() * 2, slime_surface.get_width() * 2))
slime_surface_rect = slime_surface_scaled.get_rect(midbottom=(WIDTH, GROUND_LEVEL + SLIME_OFFSET))
print(slime_surface_scaled.get_rect().height)
print(slime_surface_scaled.get_rect().width)

bird_surface = pygame.image.load('../assets/bird/bird.png').convert_alpha()
bird_surface_scale = pygame.transform.scale(bird_surface, (bird_surface.get_width() / 6, bird_surface.get_height() / 6))
print(bird_surface_scale.get_height())
print(bird_surface_scale.get_width())
obstacle_rect_list = []

user_surface = pygame.image.load("../assets/user/user_walk.png").convert_alpha()
print(user_surface.get_height(), user_surface.get_width())
user_surface_scaled = pygame.transform.scale(user_surface,
                                             (user_surface.get_width() * 3, user_surface.get_height() * 3))
user_surface_rect = user_surface_scaled.get_rect(midbottom=(USER_X_POSITION, GROUND_LEVEL + USER_OFFSET))
print(user_surface_scaled.get_height(), user_surface_scaled.get_width())

intro_surface = pygame.image.load("../assets/intro/intro_grafield_dance.png").convert_alpha()
intro_surface_scaled = pygame.transform.scale(intro_surface,
                                              (intro_surface.get_width() * 3, intro_surface.get_height() * 3))
intro_surface_scaled_rect = intro_surface_scaled.get_rect(center=(WIDTH / 2, (HEIGHT / 2) + 100))

has_started = False
user_gravity = 0
game_active = False
user_x_movement = 0

pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()
test_surface = test_font.render(TITLE, True, "dark blue")
test_surface_rect = test_surface.get_rect(center=(WIDTH / 2, 250))
test_surface_intro_rect = test_surface.get_rect(center=(WIDTH / 2, 100))

start_time_milli = 0
score = 0

to_start = "Press SPACE to start"
to_start_font = font_size_30.render(to_start, True, "White")
to_start_font_rect = to_start_font.get_rect(center=(WIDTH / 2, 600))

instruction = " Press SPACE to jump over slimes"
instruction_font = font_size_15.render(instruction, True, "grey")
instruction_font_rect = instruction_font.get_rect(center=(WIDTH / 2, 650))

# Timer to custom timer event
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 3000)


def get_score():
    score_info = f"Score: {score}"
    score_info_font = test_font.render(score_info, True, "White")
    score_info_font_rect = score_info_font.get_rect(center=(WIDTH / 2, 250))
    screen.blit(score_info_font, score_info_font_rect)


def get_timer_surface():
    current_time = int((pygame.time.get_ticks() - start_time_milli) / 1000)
    timer_surface = test_font.render(f"{current_time}", True, "red")
    timer_surface_rec = timer_surface.get_rect(center=(WIDTH / 2, 100))
    screen.blit(timer_surface, timer_surface_rec)
    return current_time


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 8
            if obstacle_rect.y == 350:
                screen.blit(bird_surface_scale, obstacle_rect)
            else:
                screen.blit(slime_surface_scaled, obstacle_rect)
            pygame.draw.rect(screen, "red", obstacle_rect, 20, 3)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

    return obstacle_list


def is_obstacle_colliding(obstacle_list):
    is_colliding = False
    for obstacle_rect in obstacle_list:
        if obstacle_rect.colliderect(user_surface_rect):
            print("Collision")
            is_colliding = True
            break
    return not is_colliding


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game_active:
                if event.key == pygame.K_SPACE and user_surface_rect.bottom == (GROUND_LEVEL + USER_OFFSET):
                    user_gravity = -30
                # if event.key == pygame.K_RIGHT:
                #     user_x_movement =25
                # if event.key == pygame.K_LEFT:
                #     user_x_movement =-25

            else:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    has_started = True
                    user_surface_rect.move(USER_X_POSITION, GROUND_LEVEL + USER_OFFSET)
                    obstacle_rect_list.clear()
                    start_time_milli = pygame.time.get_ticks()

        if event.type == obstacle_timer and game_active:
            if randint(0, 1):
                obstacle_rect_list.append(
                    bird_surface_scale.get_rect(topleft=(randint(1400, 1600), GROUND_LEVEL + BIRD_OFFSET)))

            else:
                obstacle_rect_list.append(
                    slime_surface_scaled.get_rect(midbottom=(randint(1400, 1600), GROUND_LEVEL + SLIME_OFFSET)))

            print(len(obstacle_rect_list))

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 420))
        pygame.draw.rect(screen, "yellow", test_surface_rect)
        pygame.draw.rect(screen, "yellow", test_surface_rect, 20, 30)
        pygame.draw.rect(screen, "yellow", user_surface_rect, 20, 30)
        screen.blit(test_surface, test_surface_rect)
        # screen.blit(slime_surface_scaled, slime_surface_rect)
        # pygame.draw.rect(screen,"red",slime_surface_rect,20,30)
        score = get_timer_surface()

        if user_surface_rect.left > WIDTH:
            user_surface_rect.left = 0

        user_gravity += 1
        user_surface_rect.y += user_gravity

        game_active = is_obstacle_colliding(obstacle_rect_list)

        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        if user_surface_rect.bottom > GROUND_LEVEL + USER_OFFSET:
            user_surface_rect.bottom = GROUND_LEVEL + USER_OFFSET

        screen.blit(user_surface_scaled, user_surface_rect)
        if slime_surface_rect.collidepoint(user_surface_rect.midbottom):
            game_active = False

    else:
        screen.fill((3, 84, 84))
        screen.blit(test_surface, test_surface_intro_rect)
        screen.blit(intro_surface_scaled, intro_surface_scaled_rect)
        if has_started:
            get_score()
        screen.blit(to_start_font, to_start_font_rect)
        screen.blit(instruction_font, instruction_font_rect)

    pygame.display.update()
    clock.tick(MAX_FRAME_RATE)
