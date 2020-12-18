# videon jag utgick från https://www.youtube.com/watch?v=i6xMBig-pP4

import pygame


def gameSetup():  # creates the game window
    pygame.init()

    global win
    win = pygame.display.set_mode((600, 400))

    pygame.display.set_caption("Test")


def fillScreen():  # refreshes the screen with tiles

    x = 1
    y = 1

    for y in range(400):
        for x in range(600):
            if y % 20:
                win.set_at((x, y), (255, 255, 255))
            else:
                win.set_at((x, y), (0, 0, 0))

    for x in range(600):
        for y in range(400):
            if x % 20:
                win.set_at((x, y), (255, 255, 255))

gameSetup()

pos = {"x": 20, "y": 20}
size = {"width": 20, "height": 20}

originalVel = {"x": 10,
               "y": 10}
vel = {"x": originalVel["x"],
       "y": originalVel["y"]}
direction = "right"

run = True
while run:  # Main game loop
    pygame.time.delay(200)  # Time delay in ms

    for event in pygame.event.get():  # Waits for events
        if event.type == pygame.QUIT:  # Waits for the player to quit the game window
            run = False

        if event.type == pygame.KEYDOWN:
            if not direction == ("left" or "right"):
                if event.key == pygame.K_LEFT:
                    direction = "left"
                elif event.key == pygame.K_RIGHT:
                    direction = "right"

            if not direction == ("up" or "down"):
                if event.key == pygame.K_UP:
                    direction = "up"
                elif event.key == pygame.K_DOWN:
                    direction = "down"

        print(pos["x"] % 20 and pos["y"] % 20)

        if (pos["x"] % 20) and (pos["y"] % 20):
            if direction == "left":
                vel["x"] = -originalVel["x"]
                vel["y"] = 0
            elif direction == "right":
                vel["x"] = originalVel["x"]
                vel["y"] = 0
            elif direction == "up":
                vel["x"] = 0
                vel["y"] = -originalVel["y"]
            elif direction == "down":
                vel["x"] = 0
                vel["y"] = originalVel["y"]

    keys = pygame.key.get_pressed()

    fillScreen()

    pygame.draw.rect(win, (255, 0, 0), (pos["x"], pos["y"], size["width"], size["height"]))  # Draws player
    pygame.display.update()

    pos["x"] += vel["x"]
    pos["y"] += vel["y"]

    print(direction)
    print(pos)

pygame.QUIT
