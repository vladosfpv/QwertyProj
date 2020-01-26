import pygame
import random
from pygame.transform import scale

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = scale(pygame.image.load("images/asteroid.png"), (50, 50))
        self.rect = pygame.Rect(x, y, 50, 50)
        self.yvel = 5

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.rect.y += self.yvel

        if self.rect.y > 900:
            self.kill()

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.rect = pygame.Rect(x, y, 50, 100)
        self.image = scale(pygame.image.load("images/car.png"), (100, 200))
        self.xvel = 0
        # добавим кораблю здоровье
        self.life = 100

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    # добавим группу с астероидами в обновление координат корабля
    def update(self, left, right, asteroids):
        flag = False
        if(self.rect.x > 300):
            if (left and flag != True):
                self.rect.x -= 200
                flag = True
        # если нажата клавиша вправо, увеличиваем скорость
        if(self.rect.x < 850):
            if (right and flag != True):
                self.rect.x += 200
                flag = True
        # если ничего не нажато - тормозим
        if not (left or right):
            flag = False
        # изменяем координаты на скорость


        # для каждого астероида
        for asteroid in asteroids:
            # если область, занимаемая астероидом пересекает область корабля
            if self.rect.colliderect(asteroid.rect):
                # уменьшаем жизнь
                asteroid.kill()
                self.life -= 10
            if (ship.life < 0):
                ship.kill()

pygame.init()
screen = pygame.display.set_mode((1280, 1024))
pygame.display.set_caption("Asteroids")

sky = scale(pygame.image.load("images/road.png"), (1280, 1024))

ship = Spaceship(300, 300)

left = False
right = False

asteroids = pygame.sprite.Group()

# загрузим системный шрифт
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

dist = 0

while True:
    if(ship.rect.x < 1):
        ship.rect.x = 1
    if random.randint(1, 1000) > 900:
        asteroid_x = random.randint(325, 325)
        asteroid_y = -100
        asteroid = Asteroid(asteroid_x, asteroid_y)
        asteroids.add(asteroid)

    for e in pygame.event.get():

        if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
            left = True
            flag = True
        if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
            right = True

        if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
            left = False
        if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
            right = False

        if e.type == pygame.QUIT:
            raise SystemExit("QUIT")

    screen.blit(sky, (0, 0))

    # добавим группу астероидов в параметры
    ship.update(left, right, asteroids)
    ship.draw(screen)

    for asteroid in asteroids:
        asteroid.update()
        asteroid.draw(screen)

    # выведем жизнь на экран белым цветом
    dist = dist + 1
    life = font.render(f'HP: {ship.life}', False, (255, 255, 255))
    distOUT = font.render(f'dist: {dist}', False, (255, 255, 255))
    screen.blit(life, (20, 20))
    screen.blit(distOUT, (1100, 20))
    if (ship.life < 1):
        ship.kill(ship)
    if (dist > 999):
        raise SystemExit("QUIT")


    pygame.display.update()
