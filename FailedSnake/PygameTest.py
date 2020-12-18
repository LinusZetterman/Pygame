#videon jag utgick från https://www.youtube.com/watch?v=i6xMBig-pP4

import pygame


def gameSetup(): #creates the game window
    pygame.init()

    global win
    win = pygame.display.set_mode((500, 500))

    pygame.display.set_caption("Test")

gameSetup()

x = 50
y = 50
width =  40
height = 60
vel = 5

run = True
while run: #Main game loop
    pygame.time.delay(100) #Time delay in ms

    for event in pygame.event.get(): #Waits for events
        if event.type == pygame.QUIT: #Waits for the player to quit the game window
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    win.fill((0 ,0 ,0))

    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height)) #Draws player
    pygame.display.update()

pygame.QUIT