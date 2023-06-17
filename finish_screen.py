import pygame
import level
import yeti
import math
import random
class FinishScreen:
    def __init__(self, screen, curLevel: level.Level, curYeti: yeti.Yeti):
        self.screen = screen
        self.framesPause = 0
        self.Level = curLevel
        self.Yeti = curYeti
        self.lightToI = 7
        self.lightToJ = 7.5
        self.lightI = 0
        self.lightJ = 0
        self.LoadWin()
    def LoadWin(self):
        self.win_pic = pygame.image.load('pics/Win.png')
        self.win_pic_rect = self.win_pic.get_rect()
        self.lose_pic = pygame.image.load('pics/lose.png')
        self.lose_pic_rect = self.lose_pic.get_rect()
        self.mainMenu = pygame.image.load('pics/mainMenu.png')
        self.mainMenu_rect = self.mainMenu.get_rect()
        self.autors = pygame.image.load('pics/Autors.png')
        self.autors_rect = self.autors.get_rect()
        self.pause = pygame.image.load('pics/pause.png')
        self.pause_rect = self.pause.get_rect()
        self.start = pygame.image.load('pics/start.png')
        self.start_rect = self.start.get_rect()

    def DisplayWin(self):
        self.screen.blit(self.win_pic, self.win_pic_rect)
    def DisplayLose(self):
        self.screen.blit(self.lose_pic, self.lose_pic_rect)
    def DisplayMainMenu(self):
        self.screen.blit(self.mainMenu, self.mainMenu_rect)
    def DisplayShowAutors(self):
        self.screen.blit(self.autors, self.autors_rect)
    def DisplayPause(self):
        self.framesPause += 1
        self.screen.fill((0, 0, 0))
        self.Level.DisplayLight(self.lightI, self.lightJ, 4)
        if self.framesPause < 60:
            self.screen.blit(self.pause, self.pause_rect)
        if self.framesPause >= 120:
            self.framesPause = 0
        if self.lightToI > self.lightI:
            self.lightI += 0.1
        if self.lightToJ > self.lightJ:
            self.lightJ += 0.1
        if self.lightToI < self.lightI:
            self.lightI -= 0.1
        if self.lightToJ < self.lightJ:
            self.lightJ -= 0.1
        if math.fabs(self.lightToI - self.lightI) < 0.2:
            self.lightToI = random.randint(0, 14)
        if math.fabs(self.lightToJ - self.lightJ) < 0.2:
            self.lightToJ = random.randint(0, 15)
    def DisplayStart(self):
        self.screen.blit(self.start, self.start_rect)