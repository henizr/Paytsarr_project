# Import modules
import pygame
import sys
from pygame.locals import *


class Button():
    STATE_IDLE = 'idle'
    STATE_ARMED = 'armed'
    STATE_DISARMED = 'disarmed'
    
    def __init__(
            self,
            window: pygame.Surface,
            location: tuple,
            img_up: pygame.Surface,
            img_down: pygame.Surface
            ) -> None:
        self.window: pygame.Surface = window
        self.location = location
        self.surface_up: pygame.Surface = pygame.image.load(img_up)
        self.surface_down: pygame.Surface = pygame.image.load(img_down)
        self.rect: pygame.Rect = self.surface_up.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]

        self.state = Button.STATE_IDLE


    def handle_event(self):
        pass


    def draw(self):
        "Drawing the button"
        if self.state == Button.STATE_ARMED:
            self.window.blit(self.surface_up, self.location)
        else:
            self.window.blit(self.surface_down, self.location)



