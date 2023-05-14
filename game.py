import pygame
import yeti
import level
import math

class Game:
    def __init__(self, curYeti: yeti.Yeti, curLevel: level.Level):
        self.Yeti = curYeti
        self.Level = curLevel
        self.teapot = []
        for i in range (14):
            for j in range (16):
                if self.Level.levelMap[i][j] == 't':
                    self.teapot.append((i, j))
    def DisplayLevelDetails(self):
        for (i, j) in self.teapot:
          x = j * 32
          y = i * 32
          self.Level.teapot_rect.x = x
          self.Level.teapot_rect.y = y
          self.Level.screen.blit(self.Level.teapot, self.Level.teapot_rect)
    def IsYetiHanging(self) -> bool:
        mapX = round(self.Yeti.x)
        mapY = round(self.Yeti.y)
        if self.Level.levelMap[mapY][mapX] == 'h':
            return True
        return False
    def IsYetiStanding(self) -> bool:
        mapX = round(self.Yeti.x)
        mapY = round(self.Yeti.y)
        if mapY == 13:
            return True
        if self.Level.levelMap[mapY + 1][mapX] == 'g' or self.Level.levelMap[mapY + 1][mapX] == 'b' or self.Level.levelMap[mapY + 1][mapX] == 's':
            return True
        if self.Level.levelMap[mapY][mapX] == 's':
            return True
        return False
    def GoRight(self):
        if self.Yeti.status != yeti.statusStop:
            return
        mapX = round(self.Yeti.x)
        mapY = round(self.Yeti.y)
        if self.IsYetiStanding():
            if self.Level.levelMap[mapY][mapX + 1] == 'b' or self.Level.levelMap[mapY][mapX + 1] == 'g':
                return
            self.Yeti.status = yeti.statusRunRight
            self.Yeti.frames = 0
            return
        if self.IsYetiHanging():
            if self.Level.levelMap[mapY][mapX + 1] == 'b' or self.Level.levelMap[mapY][mapX + 1] == 'g':
                return
            self.Yeti.status = yeti.statusHangingRight
            self.Yeti.frames = 0
            return
    def GoLeft(self):
        if self.Yeti.status != yeti.statusStop:
            return
        mapX = round(self.Yeti.x)
        mapY = round(self.Yeti.y)
        if self.IsYetiStanding():
            if self.Level.levelMap[mapY][mapX - 1] == 'b' or self.Level.levelMap[mapY][mapX - 1] == 'g':
                return
            self.Yeti.status = yeti.statusRunLeft
            self.Yeti.frames = 0
            return
        if self.IsYetiHanging():
            if self.Level.levelMap[mapY][mapX - 1] == 'b' or self.Level.levelMap[mapY][mapX - 1] == 'g':
                return
            self.Yeti.status = yeti.statusHangingLeft
            self.Yeti.frames = 0
            return
    def GoUp(self):
        if self.Yeti.status != yeti.statusStop:
            return
        mapX = round(self.Yeti.x)
        mapY = round(self.Yeti.y)
        if mapY == 0:
            return
        if self.Level.levelMap[mapY - 1][mapX] == 'b' or self.Level.levelMap[mapY - 1][mapX] == 'g':
            return
        if self.Level.levelMap[mapY][mapX] != 's':
            return
        self.Yeti.status = yeti.statusClimbUp
        self.Yeti.frames = 0
    def GoDown(self):
        if self.Yeti.status != yeti.statusStop:
            return
        mapX = round(self.Yeti.x)
        mapY = round(self.Yeti.y)
        if mapY == 13:
            return
        if self.Level.levelMap[mapY + 1][mapX] == 'b' or self.Level.levelMap[mapY + 1][mapX] == 'g':
            return
        if self.Level.levelMap[mapY][mapX] == 'h' and self.Level.levelMap[mapY + 1][mapX] != 's':
            self.Yeti.status = yeti.statusFall
            self.Yeti.frames = 0
            return
        if self.Level.levelMap[mapY][mapX] != 's' and self.Level.levelMap[mapY + 1][mapX] != 's':
            return
        self.Yeti.status = yeti.statusClimbDown
        self.Yeti.frames = 0
    def Check(self):
        for (i, j) in self.teapot:
            if self.Yeti.x == j and self.Yeti.y == i:
                self.teapot.remove((i, j))
        if self.Yeti.status != yeti.statusStop:
            return
        if self.IsYetiStanding():
            self.Yeti.hanging = False
            return
        if self.IsYetiHanging():
            self.Yeti.hanging = True
            return
        self.Yeti.status = yeti.statusFall
        self.Yeti.frames = 0