import pygame
import random

pygame.init()

start = pygame.time.get_ticks()

# Screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

# Platform
platform_x = 0
platform_y = 590
platform_width = 800
platform_height = 10

# Character
character_width = 50
character_height = 50
character_x = (platform_x + platform_width / 2) - (character_width / 2)
character_y = platform_y - character_height
character_velocity_x = 0
character_velocity_y = 0
character_jump_velocity = -20
character_is_jumping = False

# Blocks

block_height = 10
block_velocity = 2
blocks = []
last_block_y = -block_height

# Game loop
running = True
while running:

    block_width = random.randint(200, 300)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Checking for collisions with the walls
    if character_x < 0:
        character_x = 0
        character_velocity_x = -character_velocity_x
    elif character_x + character_width > screen_width:
        character_x = screen_width - character_width
        character_velocity_x = -character_velocity_x

    # Input
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_LEFT]:
        character_velocity_x = -5
    elif pressed_keys[pygame.K_RIGHT]:
        character_velocity_x = 5
    else:
        character_velocity_x = 0

    if pressed_keys[pygame.K_SPACE] and not character_is_jumping:
        character_is_jumping = True
        character_velocity_y = character_jump_velocity

    # Updating the characters position and velocity
    character_x += character_velocity_x
    character_y += character_velocity_y
    character_velocity_y += 1

    # Checking for collisions with the platform
    if character_y + character_height > platform_y:
        character_y = platform_y - character_height
        character_is_jumping = False
        character_velocity_y = 0

    # Generating blocks

    now = pygame.time.get_ticks()

    if now - start > 2000:
        start = now
        new_block = {
            "x": random.randint(0, screen_width - block_width),
            "y": -block_height,
            "width": block_width,
            "height": block_height,
        }
        blocks.append(new_block)
        last_block_y = new_block["y"]
    # Updating blocks positions and velocities
    for block in blocks:
        block["y"] += block_velocity

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (platform_x, platform_y, platform_width, platform_height))
    pygame.draw.rect(screen, (0, 0, 255), (character_x, character_y, character_width, character_height))
    for block in blocks:
        pygame.draw.rect(screen, (255, 255, 255), (block["x"], block["y"], block["width"], block["height"]))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()