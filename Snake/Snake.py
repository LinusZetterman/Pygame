import pygame

pygame.init()

win = pygame.display.set_mode((600, 400))
display = pygame.Surface((30, 20))

def createVariables():
    global tiles, moving, pos, size, origvel, vel

    tiles = []     #Programmera denna lista med alla rutor som kan vara gröna, svarta eller gråa. Gemför med en annan lista som innehåller rutornas originalform.

    moving = {"Left": False, "Right": False, "Up": False, "Down": False}
    pos = {"x": 5, "y": 5}
    size = {"x": 30, "y": 20}

    origVel = {"x": 1,
               "y": 1}
    vel = {"x": origVel["x"],
           "y": origVel["y"]}

def makeTiles():
    for y in range(size["y"]):
        tiles.append(y)
        for x in range(size["x"]):
            tiles[y] = [x]


    print(tiles)

    for x in range(size["x"]):
        if x % 2:
            for y in range(size["y"]):
                if not y % 2:
                    display.set_at((x, y), (10, 10, 10))
                else:
                    display.set_at((x, y), (0, 0, 0))
        if not x % 2:
            for y in range(size["y"]):
                if y % 2:
                    display.set_at((x, y), (10, 10, 10))
                else:
                    display.set_at((x, y), (0, 0, 0))

def fillScreen():
    pass

createVariables()
makeTiles()

run = True

while run:
    pygame.time.delay(100)

    if pos["x"] < 0 or pos["x"]+1 > size["x"] or pos["y"] < 0 or pos["y"]+1 > size["y"]:
        run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and not moving["Right"]:
                moving["Left"] = True
                moving["Right"] = False
                moving["Up"] = False
                moving["Down"] = False
            if event.key == pygame.K_RIGHT and not moving["Left"]:
                moving["Left"] = False
                moving["Right"] = True
                moving["Up"] = False
                moving["Down"] = False
            if event.key == pygame.K_UP and not moving["Down"]:
                moving["Left"] = False
                moving["Right"] = False
                moving["Up"] = True
                moving["Down"] = False
            if event.key == pygame.K_DOWN and not moving["Up"]:
                moving["Left"] = False
                moving["Right"] = False
                moving["Up"] = False
                moving["Down"] = True

    if moving["Left"]:
        pos["x"] -= vel["x"]
    if moving["Right"]:
        pos["x"] += vel["x"]
    if moving["Up"]:
        pos["y"] -= vel["y"]
    if moving["Down"]:
        pos["y"] += vel["y"]


    fillScreen()
    display.set_at((pos["x"], pos["y"]), (0, 255, 0))

    surf = (pygame.transform.scale(display, (600, 400), win))
    win.blit(surf, (0, 0))

    pygame.display.update()