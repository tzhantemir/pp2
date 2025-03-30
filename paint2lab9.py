import pygame

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing Tool")
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
current_color = BLACK
drawing = False
mode = "pen"  # 'pen', 'rect', 'circle', 'eraser', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus'
start_pos = None
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)

running = True
while running:
    screen.blit(canvas, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rect"
            elif event.key == pygame.K_o:
                mode = "circle"
            elif event.key == pygame.K_e:
                mode = "eraser"
            elif event.key == pygame.K_p:
                mode = "pen"
            elif event.key == pygame.K_q:
                mode = "square"  #квадрат
            elif event.key == pygame.K_t:
                mode = "right_triangle"  #прямоугольный треугольник
            elif event.key == pygame.K_y:
                mode = "equilateral_triangle"  #равносторонний треугольник
            elif event.key == pygame.K_d:
                mode = "rhombus"  #ромб
            elif event.key == pygame.K_1:
                current_color = BLACK
            elif event.key == pygame.K_2:
                current_color = RED
            elif event.key == pygame.K_3:
                current_color = GREEN
            elif event.key == pygame.K_4:
                current_color = BLUE
            elif event.key == pygame.K_5:
                current_color = YELLOW
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            if mode == "rect":
                rect_width = abs(end_pos[0] - start_pos[0])
                rect_height = abs(end_pos[1] - start_pos[1])
                pygame.draw.rect(canvas, current_color,
                                 (min(start_pos[0], end_pos[0]),
                                  min(start_pos[1], end_pos[1]),
                                  rect_width, rect_height), 2)
            elif mode == "square":
                size = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                pygame.draw.rect(canvas, current_color, (start_pos[0], start_pos[1], size, size), 2)
            elif mode == "circle":
                radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                pygame.draw.circle(canvas, current_color, start_pos, radius, 2)
            elif mode == "right_triangle":
                pygame.draw.polygon(canvas, current_color, [start_pos, (start_pos[0], end_pos[1]), end_pos], 2)
            elif mode == "equilateral_triangle":
                height = abs(end_pos[1] - start_pos[1])
                base = height * 2 / (3 ** 0.5)  #формула для равностороннего треугольника
                pygame.draw.polygon(canvas, current_color,
                                    [(start_pos[0], start_pos[1] - height),
                                     (start_pos[0] - base / 2, start_pos[1]),
                                     (start_pos[0] + base / 2, start_pos[1])], 2)
            elif mode == "rhombus":
                width = abs(end_pos[0] - start_pos[0])
                height = abs(end_pos[1] - start_pos[1])
                pygame.draw.polygon(canvas, current_color,
                                    [(start_pos[0], start_pos[1] - height // 2),
                                     (start_pos[0] - width // 2, start_pos[1]),
                                     (start_pos[0], start_pos[1] + height // 2),
                                     (start_pos[0] + width // 2, start_pos[1])], 2)

    if drawing and mode in ["pen", "eraser"]:
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.circle(canvas, WHITE if mode == "eraser" else current_color, mouse_pos, 5)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
