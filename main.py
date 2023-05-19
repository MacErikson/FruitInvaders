import pygame

screen_width = 600
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Fruit Invaders')


#load in image
bg = pygame.image.load("img/bg.png")

def draw_bg():
    screen.blit(bg, (0,0))

run = True
while run:



    #draw background
    draw_bg()



    #event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.QUIT()
