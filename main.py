import json
import math

import pygame


def handle_movement(obj: dict, speed: int or float or hex):
    if not isinstance(obj['rect'], pygame.Rect) or not isinstance(obj['vel'], pygame.Vector2):
        raise TypeError("Obj argument not valid, required: {dict : 2} {'rect': <rect(int, int, int, int>,"
                        " 'vel': <Vector2(int, int)>}, got: ", obj)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and not obj['vel'].x < -2:
        obj['vel'].x -= speed
    if keys[pygame.K_d] and not obj['vel'].x > 2:
        obj['vel'].x += speed
    if obj['rect'].y > screen.get_height() - 50:
        vert_collision = True
    else:
        vert_collision = False
    if keys[pygame.K_SPACE] and not obj['vel'].y > .2:
        obj['vel'].y -= .1
    horizontal_collision = False
    if not vert_collision and not obj['vel'].y > 7:
        obj['vel'].y += .01
    else:
        if not keys[pygame.K_SPACE]:
            obj['vel'].y = 0
    if keys[pygame.K_a] or keys[pygame.K_d]:
        key_down = True
    else:
        key_down = False
    if not horizontal_collision and not obj['vel'].x == 0:
        if 0 < math.dist((obj['vel'].x, 0), (0, 0)) < 1 and not key_down:
            obj['vel'].x = 0
        else:
            if obj['vel'].x < 0:
                obj['vel'].x += 0.01
            if obj['vel'].x > 0:
                obj['vel'].x -= 0.01

    obj['rect'].x += obj['vel'].x
    obj['rect'].y += obj['vel'].y
    return obj


run = True
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Hollow Nait But Bad")
icon = pygame.image.load("./res/img/icon.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
bg = (41, 41, 41)
R = (255, 0, 0)
G = (0, 255, 0)
B = (0, 0, 255)
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_rect = pygame.Rect(player_pos.x, player_pos.y, 50, 50)
player = {
    'rect': player_rect,
    'vel': pygame.Vector2(0, 0)
}

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(bg)
    player = handle_movement(player, speed=.1)
    pygame.draw.rect(screen, G, player['rect'])
    pygame.display.flip()

pygame.quit()
