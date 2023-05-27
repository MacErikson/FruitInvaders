import pygame
import random

#define fps
clock = pygame.time.Clock()
fps = 60

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Fruit Invaders')

#variablen
rows = 5
cols = 5

#define colors
red = (255, 0, 0)
green = (0, 255, 0)


#load in image
bg = pygame.image.load("img/bg.png")

def draw_bg():
    screen.blit(bg, (0,0))

#Klassen
class spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y, health):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.health_start = health
        self.health_remaining = health
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        speed = 8
        cooldown = 500

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= speed
        if key[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += speed
        if key[pygame.K_UP] and self.rect.top > 400:
            self.rect.y -= speed
        if key[pygame.K_DOWN] and self.rect.bottom < screen_height -20:
            self.rect.y += speed

        #Zeit
        time_now = pygame.time.get_ticks()
        #shoot
        if key[pygame.K_SPACE] and time_now - self.last_shot > cooldown:
            bullet = Bullets(self.rect.centerx, self.rect.top)
            bullet_group.add(bullet)
            self.last_shot = time_now
        
        #draw healthbar
        pygame.draw.rect(screen, red, (self.rect.x, (self.rect.bottom + 10), self.rect.width, 15))
        if self.health_remaining > 0:
            pygame.draw.rect(screen, green, (self.rect.x, (self.rect.bottom + 10), int(self.rect.width * (self.health_remaining / self.health_start)), 15))

#Bullet 
class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y -= 5
        if self.rect.bottom < 0:
            self.kill()

#Food
class Food(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/food" + str(random.randint(1, 80)) + ".png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        pass


        
#Groups
spaceship_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
food_group = pygame.sprite.Group()

def create_food():
    for row in range(rows):
        for item in range(cols):
            food = Food(100 +item * 100, 100 + row * 70)
            food_group.add(food)

create_food()


#Player
spaceship = spaceship(int(screen_width / 2), screen_height - 100, 3)
spaceship_group.add(spaceship)

run = True
while run:

    clock.tick(fps)
    

    #draw backgroundw
    #draw_bg()



    #event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

#updates
    spaceship.update()
    bullet_group.update()
    pygame.display.update()
    food_group.update()

    #draw backgroundw
    draw_bg()

    #draw sprite groups
    spaceship_group.draw(screen)
    bullet_group.draw(screen)
    food_group.draw(screen)

pygame.QUIT()
