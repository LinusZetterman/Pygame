#videon jag utgick från https://www.youtube.com/watch?v=i6xMBig-pP4

import pygame


def gameSetup(): #creates the game window
    pygame.init()

    global win
    win = pygame.display.set_mode((1000, 1000))

    pygame.display.set_caption("Test")


def fillScreen():

    for y in range(1000):
        for x in range(1000):
            win.set_at((x, y), (225, 0, 0))

            x += 2
        y += 2


gameSetup()


pos = {"x": 50, "y": 50}
size = {"width": 50, "height": 50}

originalVel = {"x": 10,
               "y": 10}
vel = {"x": originalVel["x"],
       "y": originalVel["y"]}

run = True
while run: #Main game loop
    pygame.time.delay(100) #Time delay in ms

    for event in pygame.event.get(): #Waits for events
        if event.type == pygame.QUIT: #Waits for the player to quit the game window
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                win.fill((225, 0, 0))
                vel["x"] = -originalVel["x"]
                vel["y"] = 0
            elif event.key == pygame.K_RIGHT:
                vel["x"] = originalVel["x"]
                vel["y"] = 0
            elif event.key == pygame.K_UP:
                vel["x"] = 0
                vel["y"] = -originalVel["y"]
            elif event.key == pygame.K_DOWN:
                vel["x"] = 0
                vel["y"] = originalVel["y"]

    keys = pygame.key.get_pressed()


    fillScreen()

    pygame.draw.rect(win, (255, 0, 0), (pos["x"], pos["y"], size["width"], size["height"])) #Draws player
    pygame.display.update()

    pos["x"] += vel["x"]
    pos["y"] += vel["y"]

pygame.QUIT