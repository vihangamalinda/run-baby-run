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
test_font = pygame.font.Font(font_path, 50)
font_size_30 = pygame.font.Font(font_path, 30)
font_size_15 = pygame.font.Font(font_path, 15)
grafield_intro_path = "../assets/intro/"
user_walk_path = "../assets/user/"
bird_fly_path = "../assets/bird/"
slime_walk_path = "../assets/slime/"


def get_sub_path(main_path):
    def get_full_path(index):
        return f"{main_path}/{index}.png"

    return get_full_path


get_intro_path = get_sub_path(grafield_intro_path)
get_user_path = get_sub_path(user_walk_path)
get_bird_fly_path = get_sub_path(bird_fly_path)
get_slime_slide_path = get_sub_path(slime_walk_path)

# Mentoring frames
intro_frame_index = 0
user_frame_index = 0
bird_frame_index = 0
slime_frame_index = 0


def get_frames_list(main_path, frames, scale):
    frames_list = []
    for i in range(frames):
        print(i)
        ori_img = pygame.image.load(main_path(i)).convert_alpha()
        scaled_img = pygame.transform.scale(ori_img, (ori_img.get_width() * scale, ori_img.get_height() * scale))
        frames_list.append(scaled_img)

    print("")
    print(len(frames_list))
    print()
    return frames_list


# Display surface
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# regular surface
sky_surface = pygame.image.load('../assets/sky.png').convert()
ground_surface = pygame.image.load("../assets/ground.png").convert()

# Obstacles
bird_fly_frames = get_frames_list(get_bird_fly_path, 10, 0.2)
slime_slide_frames = get_frames_list(get_slime_slide_path, 8, 2)
obstacle_rect_list = []

# Grafield intro
grafield_frames = get_frames_list(get_intro_path, 11, 3)

# User walk
user_walk_frames = get_frames_list(get_user_path, 12, 3)
user_surface_rect = user_walk_frames[user_frame_index].get_rect(midbottom=(USER_X_POSITION, GROUND_LEVEL + USER_OFFSET))

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

intro_timer = pygame.USEREVENT + 2
pygame.time.set_timer(intro_timer, 100)

user_timer = pygame.USEREVENT + 3
pygame.time.set_timer(user_timer, 100)

bird_timer = pygame.USEREVENT + 4
pygame.time.set_timer(bird_timer, 80)

slime_timer = pygame.USEREVENT + 5
pygame.time.set_timer(slime_timer, 100)


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
                screen.blit(bird_fly_frames[bird_frame_index], obstacle_rect)
            else:
                screen.blit(slime_slide_frames[slime_frame_index], obstacle_rect)
            pygame.draw.rect(screen, "red", obstacle_rect, 20, 3)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

    return obstacle_list


def is_obstacle_colliding(user_rec, obstacle_list):
    is_colliding = False
    for obstacle_rect in obstacle_list:
        if obstacle_rect.colliderect(user_rec):
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
            else:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    has_started = True
                    user_surface_rect.move(USER_X_POSITION, GROUND_LEVEL + USER_OFFSET)
                    obstacle_rect_list.clear()
                    start_time_milli = pygame.time.get_ticks()

        if game_active:
            if event.type == obstacle_timer:
                if randint(0, 1):
                    bird_scaled_rec = bird_fly_frames[bird_frame_index].get_rect(
                        topleft=(randint(1400, 1600), GROUND_LEVEL + BIRD_OFFSET))
                    obstacle_rect_list.append(bird_scaled_rec)

                else:
                    slime_scaled_rec = slime_slide_frames[slime_frame_index].get_rect(
                        midbottom=(randint(1400, 1600), GROUND_LEVEL + SLIME_OFFSET))
                    obstacle_rect_list.append(slime_scaled_rec)

            # print(len(obstacle_rect_list))
            if event.type == user_timer:
                user_frame_index += 1
                if user_frame_index >= len(user_walk_frames): user_frame_index = 0

            if event.type == bird_timer:
                bird_frame_index += 1
                if bird_frame_index >= len(bird_fly_frames): bird_frame_index = 0

            if event.type == slime_timer:
                slime_frame_index += 1
                if slime_frame_index >= len(slime_slide_frames): slime_frame_index = 0

        if event.type == intro_timer and not game_active:
            intro_frame_index += 1
            if intro_frame_index >= len(grafield_frames): intro_frame_index = 0
            print(f"frames:{intro_frame_index}")

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 420))
        pygame.draw.rect(screen, "yellow", test_surface_rect)
        pygame.draw.rect(screen, "yellow", test_surface_rect, 20, 30)
        pygame.draw.rect(screen, "yellow", user_surface_rect, 20, 30)
        screen.blit(test_surface, test_surface_rect)
        score = get_timer_surface()

        if user_surface_rect.left > WIDTH:
            user_surface_rect.left = 0

        user_gravity += 1
        user_surface_rect.y += user_gravity

        game_active = is_obstacle_colliding(user_surface_rect, obstacle_rect_list)

        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        if user_surface_rect.bottom > GROUND_LEVEL + USER_OFFSET:
            user_surface_rect.bottom = GROUND_LEVEL + USER_OFFSET

        screen.blit(user_walk_frames[user_frame_index], user_surface_rect)

    else:
        screen.fill((3, 84, 84))
        screen.blit(test_surface, test_surface_intro_rect)
        current_grafield_frame = grafield_frames[intro_frame_index]
        screen.blit(current_grafield_frame, current_grafield_frame.get_rect(center=(WIDTH / 2, (HEIGHT / 2) + 100)))

        if has_started:
            get_score()
        screen.blit(to_start_font, to_start_font_rect)
        screen.blit(instruction_font, instruction_font_rect)

    pygame.display.update()
    clock.tick(MAX_FRAME_RATE)
