import pygame
import random

pygame.init()

def start():
    global direction, head, moves, delay, tail, map, origTiles, tiles, coordinates, win, display

    direction = ""
    head = {"x": 5, "y": 5, "vel": 1}

    moves = []
    tail = {"x": 5, "y": 5, "del": 2}

    map = {"width": 27, "height": 18}
    origTiles = []
    tiles = []

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



def updateTiles (x, y):
    if x == tail["x"] and y == tail["y"]:
        tiles[x][y] = origTiles[x][y]
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
            if tiles[x][y] == 2:
                display.set_at((x, y), (255, 0, 0))
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
            if event.key == pygame.K_SPACE:
                tail["del"] += 1

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
        print(moves)
        print(len(moves))

        if len(moves) > tail["del"]:
            if moves[0] == "left":
                tail["x"] -= 1
            if moves[0] == "right":
                tail["x"] += 1
            if moves[0] == "up":
                tail["y"] -= 1
            if moves[0] == "down":
                tail["y"] += 1
            print("wow")
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


    drawDisplay()

    surf = pygame.transform.scale(display, (600, 400), win)
    win.blit(surf, (0, 0))

    pygame.display.update()