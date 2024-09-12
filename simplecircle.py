import pygame
import random

pygame.init()
screen = pygame.display.set_mode((960,600))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() // 2, screen.get_height() // 2)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill('blue')

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt 
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt 
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt 
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt 
    if keys[pygame.K_e]:
        player_pos.x = (random.randint(10,950))
        player_pos.y = (random.randint(10,590))
    
    pygame.display.flip()


    dt = clock.tick(60) / 1000

pygame.quit()