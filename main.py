import pygame
import random
import time
from pygame.transform import scale

class Road(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 1280, 1024)
        self.image = scale(pygame.image.load("images/road.png"), (1280, 1024))
        self.yvel = 0

    def update(self):
        self.rect.y += 30
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
        self.rect.y += 30
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
        self.score = 0
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    # добавим группу с астероидами в обновление координат корабля
    def update(self, left1, right1, up1, down1, asteroids, another):
        if left1:
            self.xvel -= 5
        # если нажата клавиша вправо, увеличиваем скорость
        if right1:
            self.xvel += 5
        if up1:
            self.yvel -= 5
        if down1:
            self.yvel += 5
        # если ничего не нажато - тормозим
        if not (left1 or right1 or down1 or up1):
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
        for asteroid in asteroids:
            # если область, занимаемая астероидом пересекает область корабля
            if self.rect.colliderect(asteroid.rect):
                # уменьшаем очки
                asteroid.kill()
                if self.score >= 10:
                    self.score -= 10
        self.rect.x += self.xvel
        self.rect.y += self.yvel


class Player2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 60, 195)
        self.image = scale(pygame.image.load("images/car.png"), (100, 200))
        self.xvel = 0
        self.yvel = 0
        self.score = 0
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    # добавим группу с астероидами в обновление координат корабля
    def update(self, left2, right2, up2, down2, asteroids,another):
        if left2:
            self.xvel -= 5
        # если нажата клавиша вправо, увеличиваем скорость
        if right2:
            self.xvel += 5
        if up2:
            self.yvel -= 5
        if down2:
            self.yvel += 5
        # если ничего не нажато - тормозим
        if not (left2 or right2 or down2 or up2):
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
        # изменяем координаты на скорости
        # для каждого астероида
        for asteroid in asteroids:
            # если область, занимаемая астероидом пересекает область корабля
            if self.rect.colliderect(asteroid.rect):
                # уменьшаем жизнь
                asteroid.kill()
                if self.score >= 10:
                    self.score -= 10
        self.rect.x += self.xvel
        self.rect.y += self.yvel

pygame.init()
screen = pygame.display.set_mode((1280, 1024))
pygame.display.set_caption("Asteroids")
pygame.mixer.music.load("music/mainSong.mp3")
pygame.mixer.music.play()
road = Road(0, 0)

ship1 = Player1(300, 300)
ship2 = Player2(500, 300)

left1 = False
right1 = False
up1 = False
down1 = False
left2 = False
right2 = False
up2 = False
down2 = False

asteroids = pygame.sprite.Group()

# загрузим системный шрифт
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
# Let it play for up to 30 seconds, then sto
#основной цикл
while True:

    road.update()
    road.draw(screen)

    if(ship1.rect.x < 1):
        ship1.rect.x = 1
    if (ship2.rect.x < 1):
        ship2.rect.x = 1
    if random.randint(1, 1000) > 950:
        asteroid_x = random.randint(325, 900)
        asteroid_y = -100
        asteroid = Asteroid(asteroid_x, asteroid_y)
        asteroids.add(asteroid)

    for e in pygame.event.get():

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

        if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
            left2 = True
        if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
            right2 = True
        if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
            up2 = True
        if e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN:
            down2 = True

        if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
            left2 = False
        if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
            right2 = False
        if e.type == pygame.KEYUP and e.key == pygame.K_UP:
            up2 = False
        if e.type == pygame.KEYUP and e.key == pygame.K_DOWN:
            down2 = False

        if e.type == pygame.QUIT:
            raise SystemExit("QUIT")


    # добавим группу астероидов в параметры
    ship1.update(left1, right1, up1, down1, asteroids, ship2)
    ship1.draw(screen)
    ship2.update(left2, right2, up2, down2, asteroids, ship1)
    ship2.draw(screen)

    for asteroid in asteroids:
        asteroid.update()
        asteroid.draw(screen)

    # выведем жизнь на экран белым цветом
    score1 = font.render(f'player 1: {ship1.score}', False, (255, 255, 255))
    score2 = font.render(f'player 2: {ship2.score}', False, (255, 255, 255))
    screen.blit(score1, (20, 20))
    screen.blit(score2, (1000, 20))
    pygame.display.update()