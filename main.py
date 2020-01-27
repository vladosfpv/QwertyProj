import pygame
import random
from pygame.transform import scale

class Road(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 1280, 1024)
        self.image = scale(pygame.image.load("images/road.png"), (1280, 1024))
        self.yvel = 0

    def update(self):
        self.rect.y += 20
        if self.rect.y > 1024:
            self.kill()
            self.rect.y = 0

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        screen.blit(self.image, (self.rect.x, self.rect.y - 1024))

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = scale(pygame.image.load("images/asteroid.png"), (50, 50))
        self.rect = pygame.Rect(x, y, 50, 50)
        self.yvel = 5
    def update(self):
        self.rect.y += 20
        if self.rect.y > 900:
            self.kill()
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Player1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 50, 195)
        self.image = scale(pygame.image.load("images/car.png"), (100, 200))
        self.xvel = 0
        self.yvel = 0
        self.life = 100
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    # добавим группу с астероидами в обновление координат корабля
    def update(self, left, right, up, down, asteroids):
        if left:
            self.xvel -= 5
        # если нажата клавиша вправо, увеличиваем скорость
        if right:
            self.xvel += 5
        if up:
            self.yvel -= 5
        if down:
            self.yvel += 5
        # если ничего не нажато - тормозим
        if not (left or right or down or up):
            # выравнивание по иксу
            if self.xvel > 0:
                self.xvel -= 5
            elif self.xvel < 0:
                self.xvel += 5
            # выравнивание по игрику
            if self.yvel < 0:
                self.yvel += 5
            if self.yvel > 0:
                self.yvel -= 5
            # автостопы
        if self.rect.x <= 210:
            self.xvel = 5
        if self.rect.x >= 970:
            self.xvel = -5
        if self.rect.y <= 0:
            self.yvel = +5
        if self.rect.y >= 1024:
            self.yvel = -5
        # изменяем координаты на скорость


        # для каждого астероида
        for asteroid in asteroids:
            # если область, занимаемая астероидом пересекает область корабля
            if self.rect.colliderect(asteroid.rect):
                # уменьшаем жизнь
                asteroid.kill()
                self.life -= 10

        self.rect.x += self.xvel
        self.rect.y += self.yvel
class Player2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 50, 195)
        self.image = scale(pygame.image.load("images/car.png"), (100, 200))
        self.xvel = 0
        self.yvel = 0
        self.life = 100
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    # добавим группу с астероидами в обновление координат корабля
    def update(self, left, right, up, down, asteroids):
        if left:
            self.xvel -= 5
        # если нажата клавиша вправо, увеличиваем скорость
        if right:
            self.xvel += 5
        if up:
            self.yvel -= 5
        if down:
            self.yvel += 5
        # если ничего не нажато - тормозим
        if not (left or right or down or up):
            # выравнивание по иксу
            if self.xvel > 0:
                self.xvel -= 5
            elif self.xvel < 0:
                self.xvel += 5
            # выравнивание по игрику
            if self.yvel < 0:
                self.yvel += 5
            if self.yvel > 0:
                self.yvel -= 5
            # автостопы
        if self.rect.x <= 210:
            self.xvel = 5
        if self.rect.x >= 970:
            self.xvel = -5
        if self.rect.y <= 0:
            self.yvel = +5
        if self.rect.y >= 1024:
            self.yvel = -5
        # изменяем координаты на скорость


        # для каждого астероида
        for asteroid in asteroids:
            # если область, занимаемая астероидом пересекает область корабля
            if self.rect.colliderect(asteroid.rect):
                # уменьшаем жизнь
                asteroid.kill()
                self.life -= 10

        self.rect.x += self.xvel
        self.rect.y += self.yvel

pygame.init()
screen = pygame.display.set_mode((1280, 1024))
pygame.display.set_caption("GONKA")
road1 = Road(0, 0)
road2 = Road(0, -1024)
ship = Player1(300, 300)



left1 = False
right1 = False
up1 = False
down1 = False

asteroids = pygame.sprite.Group()

# загрузим системный шрифт
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
dist = 0
#основной цикл
while True:
    road1.update()
    road1.draw(screen)

    if(ship.rect.x < 1):
        ship.rect.x = 1
    if random.randint(1, 150) > 149:
        asteroid_x = random.randint(325, 900)
        asteroid_y = -100
        asteroid = Asteroid(asteroid_x, asteroid_y)
        asteroids.add(asteroid)

    for e in pygame.event.get():

        if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
            left1 = True
        if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
            right1 = True
        if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
            up1 = True
        if e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN:
            down1 = True


        if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
            left1 = False
        if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
            right1 = False
        if e.type == pygame.KEYUP and e.key == pygame.K_UP:
            up1 = False
        if e.type == pygame.KEYUP and e.key == pygame.K_DOWN:
            down1 = False

        if e.type == pygame.KEYDOWN and e.key == pygame.K_a:
            left1 = True
        if e.type == pygame.KEYDOWN and e.key == pygame.K_d:
            right1 = True
        if e.type == pygame.KEYDOWN and e.key == pygame.K_w:
            up1 = True
        if e.type == pygame.KEYDOWN and e.key == pygame.K_s:
            down1 = True


        if e.type == pygame.KEYUP and e.key == pygame.K_a:
            left1 = False
        if e.type == pygame.KEYUP and e.key == pygame.K_d:
            right1 = False
        if e.type == pygame.KEYUP and e.key == pygame.K_w:
            up1 = False
        if e.type == pygame.KEYUP and e.key == pygame.K_s:
            down1 = False

        if e.type == pygame.QUIT:
            raise SystemExit("QUIT")

    # добавим группу астероидов в параметры
    ship.update(left1, right1, up1, down1, asteroids)
    ship.draw(screen)

    asteroids.update()
    asteroids.draw(screen)

    # выведем жизнь на экран белым цветом
    dist = dist + 1
    life = font.render(f'Score: {ship.life}', False, (0, 0, 0))
    distOUT = font.render(f'dist: {dist}', False, (0, 0, 0))
    screen.blit(life, (20, 20))
    screen.blit(distOUT, (1100, 20))
    pygame.display.update()