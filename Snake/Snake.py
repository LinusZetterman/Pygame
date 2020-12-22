import pygame
pygame.init()

def start():
    global direction, head, tail, map, origTiles, coordinates, win, display

    direction = ""
    head = {"x": 5, "y": 5, "vel": 1}
    tail = {"x": 0, "y": 0, "vel": 1}

    map = {"width": 30, "height": 20}
    origTiles = []

    win = pygame.display.set_mode((600, 400))
    display = pygame.Surface((30, 20))

def setCoordinates():
    for x in range(map["width"]):
        origTiles.append([])
        for y in range(map["height"]):
            if x % 2:
                if y % 2:
                    origTiles[x].append(0)
                else:
                    origTiles[x].append(1)
            else:
                if y % 2:
                    origTiles[x].append(1)
                else:
                    origTiles[x].append(0)

    global tiles

    tiles = origTiles

def updateTiles (x, y):
    if x == head["x"] and y == head["y"]:
        tiles[x][y] = 3

def drawDisplay():
    for x in range(len(tiles)):
        for y in range(len(tiles[x])):
            updateTiles(x, y)
            if tiles[x][y] == 0:
                display.set_at((x, y), (0, 0, 0))
            if tiles[x][y] == 1:
                display.set_at((x, y), (10, 10, 10))
            if tiles[x][y] == 3:
                display.set_at((x, y), (0, 255, 0))
start()
setCoordinates()


run = True

while run:
    pygame.time.delay(150)

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

    drawDisplay()

    surf = pygame.transform.scale(display, (600, 400), win)
    win.blit(surf, (0, 0))

    pygame.display.update()