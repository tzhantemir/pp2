import pygame
import time
pygame.init()
WIDTH, HEIGHT = 577, 433
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")
background = pygame.image.load("images/mickey_bg-r-preview.png")
right_hand = pygame.image.load("images/mickey_bg-rem-preview.png")
left_hand = pygame.image.load("images/mickey_bg-removebg-preview (1).png")
center = (WIDTH // 2, HEIGHT // 2)

clock = pygame.time.Clock()
running = True

while running:
    screen.fill((255, 255, 255))
    screen.blit(background, (0,0) )
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec
    angle_minutes = -(minutes * 6)
    angle_seconds = -(seconds * 6)
    rotated_right_hand = pygame.transform.rotate(right_hand, angle_minutes)
    rotated_left_hand = pygame.transform.rotate(left_hand, angle_seconds)
    screen.blit(rotated_right_hand, rotated_right_hand.get_rect(center=center))
    screen.blit(rotated_left_hand, rotated_left_hand.get_rect(center=center))

    pygame.display.flip()
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()