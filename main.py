import pygame

#define fps
clock = pygame.time.Clock()
fps = 60

screen_width = 600
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Fruit Invaders')


#load in image
bg = pygame.image.load("img/bg.png")

def draw_bg():
    screen.blit(bg, (0,0))

#Klassen
class spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
    
    def update(self):
        speed = 8

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= speed
        if key[pygame.K_RIGHT]:
            self.rect.x += speed
        if key[pygame.K_UP]:
            self.rect.y -= speed
        if key[pygame.K_DOWN]:
            self.rect.y += speed


#Groups
spaceship_group = pygame.sprite.Group()

#Player
spaceship = spaceship(int(screen_width / 2), screen_height - 100)
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


    spaceship.update()

    pygame.display.update()

    #draw backgroundw
    draw_bg()

    #update sprite groups
    spaceship_group.draw(screen)

pygame.QUIT()
