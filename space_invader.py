import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Space Invaders")

PlayerImg = pygame.image.load("spaceship (1).png")
playerX = 370

playerY = 480

def player(x,y):
    screen.blit(PlayerImg,(x,y))

running = True
while running:
    playerY -= 0.1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((250, 150, 150))
    player(playerX,playerY)
    pygame.display.update()