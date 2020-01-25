import pygame

FPS = 60
W = 700  # ширина экрана
H = 300  # высота экрана
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RIGHT = "to the right"
LEFT = "to the left"
STOP = "stop"

pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

surf1 = pygame.Surface((200, 200))
surf1.fill((0, 0, 0))  # желтая
rect = pygame.Rect((60, 20, 600, 200))
# координаты и радиус круга
x = W // 2
y = H // 2
r = 50

motion = STOP

while 1:
    sc.fill(BLACK)
    pygame.draw.circle(surf1, WHITE, (x, y), r)
    pygame.display.update()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 3
    elif keys[pygame.K_RIGHT]:
        x += 3

clock.tick(FPS)