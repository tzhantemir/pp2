import pygame
pygame.init()
WIDTH, HEIGHT = 500,500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ball_radius = 25
x, y = WIDTH // 2, HEIGHT // 2
speed = 20

running = True
while running:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x - speed - ball_radius >= 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x + speed + ball_radius <= WIDTH:
        x += speed
    if keys[pygame.K_UP] and y - speed - ball_radius >= 0:
        y -= speed
    if keys[pygame.K_DOWN] and y + speed + ball_radius <= HEIGHT:
        y += speed

    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), ball_radius)
    pygame.display.update()

pygame.quit()
