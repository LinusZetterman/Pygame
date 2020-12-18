import pygame

def gameSetup(): #creates the game window
    pygame.init()

    global win
    win = pygame.display.set_mode((1000, 1000))

    pygame.display.set_caption("Test")



def fillScreen(): #refreshes the screen with tiles

    for y in range(1000):
        for x in range(1000):
            win.set_at((x, y), (0, 0, 0))

            x += 2
        y += 2
