import pygame

run = True
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Hollow Nait But Bad")
icon = pygame.image.load("./res/img/icon.png")
pygame.display.set_icon(icon)
bg = (41, 41, 41)
R = (255, 0, 0)
G = (0, 255, 0)
B = (0, 0, 255)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(bg)
    pygame.display.flip()

pygame.quit()
