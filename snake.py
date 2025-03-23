import pygame
import random
import sys

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('audios/Dana_Glover_-_It_Is_You_I_Have_Loved_54898325.mp3')
pygame.mixer.music.play(-1)
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 10
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game with Levels")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = "RIGHT"
change_to = snake_direction
speed = 15

# Генерация еды, избегая змейки

def generate_food():
    while True:
        pos = [random.randrange(0, WIDTH // GRID_SIZE) * GRID_SIZE,
               random.randrange(0, HEIGHT // GRID_SIZE) * GRID_SIZE]
        if pos not in snake_body:
            return pos

food_pos = generate_food()
food_spawn = True

game_score = 0
level = 1
food_needed_for_next_level = 3

isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                change_to = "UP"
            if event.key == pygame.K_DOWN and snake_direction != "UP":
                change_to = "DOWN"
            if event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                change_to = "RIGHT"

    snake_direction = change_to
    if snake_direction == "UP":
        snake_pos[1] -= GRID_SIZE
    elif snake_direction == "DOWN":
        snake_pos[1] += GRID_SIZE
    elif snake_direction == "LEFT":
        snake_pos[0] -= GRID_SIZE
    elif snake_direction == "RIGHT":
        snake_pos[0] += GRID_SIZE

    # Проверка столкновений с границами
    if snake_pos[0] < 0 or snake_pos[0] >= WIDTH or snake_pos[1] < 0 or snake_pos[1] >= HEIGHT:
        isRunning = False
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        food_spawn = False
        game_score += 1
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = generate_food()
        food_spawn = True

    # Проверка столкновений с собой
    for block in snake_body[1:]:
        if snake_pos == block:
            isRunning = False

    # Повышение уровня
    if game_score % food_needed_for_next_level == 0 and game_score != 0:
        level += 1
        speed += 2  # Увеличение скорости
        food_needed_for_next_level += 3  # Следующий уровень требует больше еды
    screen.fill(BLACK)
    for p in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(p[0], p[1], GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], GRID_SIZE, GRID_SIZE))

    # Вывод счета и уровня
    score_text = font.render(f"Score: {game_score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (20, 20))
    screen.blit(level_text, (20, 50))

    pygame.display.update()
    clock.tick(speed)
game_over_text = font.render("GAME OVER", True, WHITE)
game_over_rectangle = game_over_text.get_rect()
game_over_rectangle.center = (WIDTH / 2, HEIGHT / 2)
screen.blit(game_over_text, game_over_rectangle)
pygame.display.update()
pygame.time.wait(3000)
