import pygame

pygame.init()
pygame.display.set_caption("Paint")

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)

color = BLACK
brush_size = 5
shape_size = 50
drawing = False
tool = "brush"
start_pos = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
            if tool in ["rect", "circle"]:
                shape_start = start_pos
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            if tool == "rect":
                pygame.draw.rect(screen, color, (start_pos[0], start_pos[1], shape_size, shape_size), 2)
            elif tool == "circle":
                pygame.draw.circle(screen, color, start_pos, shape_size, 2)
        elif event.type == pygame.MOUSEMOTION and drawing:
            if tool == "brush":
                pygame.draw.circle(screen, color, event.pos, brush_size)
            elif tool == "eraser":
                pygame.draw.circle(screen, WHITE, event.pos, brush_size)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                tool = "brush"
            elif event.key == pygame.K_w:
                tool = "rect"
            elif event.key == pygame.K_e:
                tool = "circle"
            elif event.key == pygame.K_r:
                tool = "eraser"
            elif event.key == pygame.K_1:
                color = RED
            elif event.key == pygame.K_2:
                color = GREEN
            elif event.key == pygame.K_3:
                color = BLUE
            elif event.key == pygame.K_4:
                color = BLACK
            elif event.key == pygame.K_5:
                color = WHITE
            elif event.key == pygame.K_6:
                shape_size += 5
            elif event.key == pygame.K_7:
                shape_size = max(5, shape_size - 5)
    
    pygame.display.flip()

pygame.quit()