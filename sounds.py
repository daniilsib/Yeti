import pygame
import sys
class GameSound:
    def __init__(self):
        self.soundTeapot = pygame.mixer.Sound('teapot.mp3')
        self.soundBrokeGrass = pygame.mixer.Sound('broke_grass.mp3')
        self.soundMenu = pygame.mixer.Sound('menu.mp3')
    def PlayTeapot(self):
        self.soundTeapot.play()
    def PlayBrokeGrass(self):
        self.soundBrokeGrass.play()
    def PlayMenu(self):
        self.soundMenu.play()
    def StopMenu(self):
        self.soundMenu.stop()