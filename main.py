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
        self.image = scale(pygame.image.load("images/alpine-landscape-rock-rubble-01g-al1.png"), (50, 50))
        self.rect = pygame.Rect(x, y, 50, 50)
        self.yvel = 5
    def update(self):
        self.rect.y += 30
        if self.rect.y > 900:
            self.kill()
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Gem(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = scale(pygame.image.load("images/Dream_Flying_Gem_Sprite.png"), (50, 50))
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
    def update(self, left1, right1, up1, down1, asteroids, gems):
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
        for gem in gems:
            # если область, занимаемая астероидом пересекает область корабля
            if self.rect.colliderect(gem.rect):
                gem.kill()
                self.score += 10
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
        self.image = scale(pygame.image.load("images/887d9872643d696f81599530d6e79fc1.png"), (100, 200))
        self.xvel = 0
        self.yvel = 0
        self.score = 0
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    # добавим группу с астероидами в обновление координат корабля
    def update(self, left2, right2, up2, down2, asteroids,gems):
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
        for gem in gems:
            # если область, занимаемая астероидом пересекает область корабля
            if self.rect.colliderect(gem.rect):
                gem.kill()
                self.score += 10

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
pygame.display.set_caption("Death race")
pygame.mixer.music.load("music/mainSong.mp3")
pygame.mixer.music.play()
road = Road(0, 0)

ship1 = Player1(500, 300)
ship2 = Player2(700, 300)

left1 = False
right1 = False
up1 = False
down1 = False
left2 = False
right2 = False
up2 = False
down2 = False

asteroids = pygame.sprite.Group()
gems = pygame.sprite.Group()
dist = 10000;
# загрузим системный шрифт
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
#основной цикл
f = True
while True:

    road.update()
    road.draw(screen)

    if(ship1.rect.x < 1):
        ship1.rect.x = 1
    if (ship2.rect.x < 1):
        ship2.rect.x = 1
    if (f == True):
        if random.randint(1, 1000) > 950:
            gem_x = random.randint(325, 900)
            gem_y = -100
            gem = Gem(gem_x, gem_y)
            gems.add(gem)

        if random.randint(1, 1000) > 950:
            asteroid_x = random.randint(325, 900)
            asteroid_y = -100
            asteroid = Asteroid(asteroid_x, asteroid_y)
            asteroids.add(asteroid)


    if(f == True):
      for e in pygame.event.get():
        if e.type == pygame.QUIT:
            raise SystemExit("QUIT")
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
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            raise SystemExit("QUIT")

    # добавим группу астероидов в параметры
    ship1.update(left1, right1, up1, down1, asteroids, gems)
    ship1.draw(screen)
    ship2.update(left2, right2, up2, down2, asteroids, gems)
    ship2.draw(screen)

    for asteroid in asteroids:
        asteroid.update()
        asteroid.draw(screen)

    for gem in gems:
        gem.update()
        gem.draw(screen)
    dist -= 20
    # выведем жизнь на экран белым цветом
    score1 = font.render(f'player 1: {ship1.score}', False, (255, 255, 255))
    score2 = font.render(f'player 2: {ship2.score}', False, (255, 255, 255))
    distTo = font.render(f'Distance to finish: {dist}', False, (255, 255, 255))
    screen.blit(score1, (20, 20))
    screen.blit(score2, (1000, 20))
    screen.blit(distTo, (500, 40))
    if (dist <= 0):
        f = False
        dist += 20
        ship1.rect.x = 470
        ship2.rect.x = 695
        ship1.xvel = 0
        ship2.xvel = 0
        ship1.yvel = 0
        ship2.yvel = 0
        pygame.mixer.music.stop()
        font = pygame.font.SysFont('Arial', 30)
        if (ship2.score > ship1.score):
            end = font.render(f'Player 2 win', False, (255, 0, 0))
            screen.blit(end, (540, 100))
        elif (ship1.score > ship2.score):
            end = font.render(f'Player 1 win', False, (255, 0, 0))
            screen.blit(end, (540, 100))
        else:
            end = font.render(f'Draw', False, (255, 0, 0))
            screen.blit(end, (600, 100))


    pygame.display.update()