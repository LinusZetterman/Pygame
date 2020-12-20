import pygame
pygame.init()

def start():
    global direction, player, map, win, display

    direction = "right"
    player = {"x": 5, "y": 5, "vel": 1}

    map = {"width": 30, "height": 20}
    win = pygame.display.set_mode((600, 400))
    display = pygame.Surface((30, 20))

start()
run = True

while run:
    pygame.time.delay(150)
    if player["x"] < 0 or player["x"] >= map["width"] or player["y"] < 0 or player["y"] >= map["height"]:
        run = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if direction == "up" or direction == "down":
                if event.key == pygame.K_LEFT:
                    direction = "left"
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
            if direction == "left" or direction == "right":
                if event.key == pygame.K_UP:
                    direction = "up"
                elif event.key == pygame.K_DOWN:
                    direction = "down"

    if direction == "left":
        player["x"] -= 1
    if direction == "right":
        player["x"] += 1
    if direction == "up":
        player["y"] -= 1
    if direction == "down":
        player["y"] += 1

    display.set_at((player["x"], player["y"]), (0, 255, 0))

    surf = pygame.transform.scale(display, (600, 400), win)
    win.blit(surf, (0, 0))

    pygame.display.update()