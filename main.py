# Import modules
import pygame
import sys
from pygame.locals import *
import random
import pathlib
from scr_bright_contr import *

print(ScreenBrightnessControl.get_current_brightness())


# Declare constants
BACKGROUND_COLOR = (100, 0, 250)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FRAMES_PER_SECOND = 30

# Initializing the environment
pygame.init()
window: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Initialize variables

# Main gameloop
while True:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            pass

    # actions

    window.fill(BACKGROUND_COLOR)

    # drawings

    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)



