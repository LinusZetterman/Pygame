import pygame
import random

pygame.init()

def start():
    global direction, head, moves, delay, tail, map, origTiles, tiles, coordinates, apple, win, display

    direction = ""
    head = {"x": 5, "y": 5, "vel": 1}

    moves = []
    tail = {"x": 5, "y": 5, "del": 2}

    map = {"width": 24, "height": 16}
    origTiles = []
    tiles = []

    apple = {"x": random.randint(round(map["width"]/2), map["width"]), "y": random.randint(round(map["height"]/2), map["height"])}

    win = pygame.display.set_mode((600, 400))
    display = pygame.Surface((map["width"], map["height"]))

def setCoordinates():
    for x in range(map["width"]):
        origTiles.append([])
        tiles.append([])
        for y in range(map["height"]):
            if x % 2:
                if y % 2:
                    origTiles[x].append(0)
                    tiles[x].append(0)
                else:
                    origTiles[x].append(1)
                    tiles[x].append(1)
            else:
                if y % 2:
                    origTiles[x].append(1)
                    tiles[x].append(1)
                else:
                    origTiles[x].append(0)
                    tiles[x].append(0)

def generateApple ():
    randX = random.randint(0, map["width"]-1)
    randY = random.randint(0, map["height"]-1)

    while tiles[randX][randY] == 3:
        randX = random.randint(0, map["width"]-1) #?
        randY = random.randint(0, map["height"]-1)

    apple["x"] = randX
    apple["y"] = randY
    tail["del"] += 1

def updateTiles (x, y):
    if x == tail["x"] and y == tail["y"]:
        tiles[x][y] = origTiles[x][y]
    if x == head["x"] and y == head["y"]:
        tiles[x][y] = 3
    if x == apple["x"] and y == apple["y"]:
        tiles[x][y] = 2
    if head["x"] == apple["x"] and head["y"] == apple["y"]:
        generateApple()

def drawDisplay():
    for x in range(len(tiles)):
        for y in range(len(tiles[x])):
            updateTiles(x, y)
            if tiles[x][y] == 0:
                display.set_at((x, y), (0, 0, 0))
            if tiles[x][y] == 1:
                display.set_at((x, y), (10, 10, 10))
            if tiles[x][y] == 2:
                display.set_at((x, y), (255, 0, 0))
            if tiles[x][y] == 3:
                display.set_at((x, y), (0, 255, 0))

run = True

def detectCollision ():
    if tail["del"] > 2:
        if tiles[head["x"]][head["y"]] == 3:
            global run
            run = False

start()
setCoordinates()

while run:
    pygame.time.delay(180)

    if head["x"] < 0 or head["x"] >= map["width"] or head["y"] < 0 or head["y"] >= map["height"]:
        run = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if direction == "up" or direction == "down" or direction == "":
                if event.key == pygame.K_LEFT:
                    direction = "left"
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
            if direction == "left" or direction == "right" or direction == "":
                if event.key == pygame.K_UP:
                    direction = "up"
                elif event.key == pygame.K_DOWN:
                    direction = "down"

    if direction == "left":
        head["x"] -= 1
    if direction == "right":
        head["x"] += 1
    if direction == "up":
        head["y"] -= 1
    if direction == "down":
        head["y"] += 1

    if not direction == "":
        moves.append(direction)

        if len(moves) > tail["del"]:
            if moves[0] == "left":
                tail["x"] -= 1
            if moves[0] == "right":
                tail["x"] += 1
            if moves[0] == "up":
                tail["y"] -= 1
            if moves[0] == "down":
                tail["y"] += 1
        elif len(moves) == tail["del"]:
            if moves[0] == "left":
                tail["x"] -= 1
            if moves[0] == "right":
                tail["x"] += 1
            if moves[0] == "up":
                tail["y"] -= 1
            if moves[0] == "down":
                tail["y"] += 1
            moves.pop(0)

    detectCollision()
    drawDisplay()

    surf = pygame.transform.scale(display, (600, 400), win)
    win.blit(surf, (0, 0))

    pygame.display.update()