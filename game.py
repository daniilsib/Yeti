import pygame
import yeti
import level
import enemy
import math

class Game:
    def __init__(self, curYeti: yeti.Yeti, curLevel: level.Level, curEnemy: enemy.Enemy, curEnemy2: enemy.Enemy):
        self.Yeti = curYeti
        self.Level = curLevel
        self.Enemy = curEnemy
        self.Enemy2 = curEnemy2
        self.Win = False
        self.Lose = False
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
    def IsHanging(self, Actor) -> bool:
        mapX = round(Actor.x)
        mapY = round(Actor.y)
        if self.Level.levelMap[mapY][mapX] == 'h':
            return True
        return False
    def IsStanding(self, Actor) -> bool:
        mapX = round(Actor.x)
        mapY = round(Actor.y)
        if mapY == 13:
            return True
        if self.Level.levelMap[mapY + 1][mapX] == 'g' or self.Level.levelMap[mapY + 1][mapX] == 'b' or self.Level.levelMap[mapY + 1][mapX] == 's':
            return True
        if self.Level.levelMap[mapY][mapX] == 's':
            return True
        return False
    def CanGoRight(self, Actor) -> bool:
        if Actor.status != yeti.statusStop:
            return False
        mapX = round(Actor.x)
        mapY = round(Actor.y)
        if self.IsStanding(Actor) or self.IsHanging(Actor):
            if self.Level.levelMap[mapY][mapX + 1] == 'b' or self.Level.levelMap[mapY][mapX + 1] == 'g':
                return False
            return True
    def CanGoLeft(self, Actor) -> bool:
        if Actor.status != yeti.statusStop:
            return False
        mapX = round(Actor.x)
        mapY = round(Actor.y)
        if self.IsStanding(Actor) or self.IsHanging(Actor):
            if self.Level.levelMap[mapY][mapX - 1] == 'b' or self.Level.levelMap[mapY][mapX - 1] == 'g':
                return False
            return True
    def GoRight(self, Actor):
        if Actor.status != yeti.statusStop:
            return
        mapX = round(Actor.x)
        mapY = round(Actor.y)
        if self.IsStanding(Actor):
            if self.Level.levelMap[mapY][mapX + 1] == 'b' or self.Level.levelMap[mapY][mapX + 1] == 'g':
                return
            Actor.status = yeti.statusRunRight
            Actor.frames = 0
            return
        if self.IsHanging(Actor):
            if self.Level.levelMap[mapY][mapX + 1] == 'b' or self.Level.levelMap[mapY][mapX + 1] == 'g':
                return
            Actor.status = yeti.statusHangingRight
            Actor.frames = 0
            return
    def GoLeft(self, Actor):
        if self.Yeti.status != yeti.statusStop:
            return
        mapX = round(Actor.x)
        mapY = round(Actor.y)
        if self.IsStanding(Actor):
            if self.Level.levelMap[mapY][mapX - 1] == 'b' or self.Level.levelMap[mapY][mapX - 1] == 'g':
                return
            Actor.status = yeti.statusRunLeft
            Actor.frames = 0
            return
        if self.IsHanging(Actor):
            if self.Level.levelMap[mapY][mapX - 1] == 'b' or self.Level.levelMap[mapY][mapX - 1] == 'g':
                return
            Actor.status = yeti.statusHangingLeft
            Actor.frames = 0
            return
    def CanGoUp(self, Actor) -> bool:
        if self.Yeti.status != yeti.statusStop:
            return False
        mapX = round(Actor.x)
        mapY = round(Actor.y)
        if mapY == 0:
            return False
        if self.Level.levelMap[mapY - 1][mapX] == 'b' or self.Level.levelMap[mapY - 1][mapX] == 'g':
            return False
        if self.Level.levelMap[mapY][mapX] != 's':
            return False
        return True
    def CanGoDown(self, Actor) -> bool:
        if self.Yeti.status != yeti.statusStop:
            return False
        mapX = round(Actor.x)
        mapY = round(Actor.y)
        if mapY == 13:
            return False
        if self.Level.levelMap[mapY + 1][mapX] == 'b' or self.Level.levelMap[mapY + 1][mapX] == 'g':
            return False
        if self.Level.levelMap[mapY][mapX] == 'h' and self.Level.levelMap[mapY + 1][mapX] != 's':
            return True
        if self.Level.levelMap[mapY][mapX] != 's' and self.Level.levelMap[mapY + 1][mapX] != 's':
            return False
        return True
    def GoUp(self, Actor):
        if self.Yeti.status != yeti.statusStop:
            return
        mapX = round(Actor.x)
        mapY = round(Actor.y)
        if mapY == 0:
            return
        if self.Level.levelMap[mapY - 1][mapX] == 'b' or self.Level.levelMap[mapY - 1][mapX] == 'g':
            return
        if self.Level.levelMap[mapY][mapX] != 's':
            return
        Actor.status = yeti.statusClimbUp
        Actor.frames = 0
    def GoDown(self, Actor):
        if self.Yeti.status != yeti.statusStop:
            return
        mapX = round(Actor.x)
        mapY = round(Actor.y)
        if mapY == 13:
            return
        if self.Level.levelMap[mapY + 1][mapX] == 'b' or self.Level.levelMap[mapY + 1][mapX] == 'g':
            return
        if self.Level.levelMap[mapY][mapX] == 'h' and self.Level.levelMap[mapY + 1][mapX] != 's':
            Actor.status = yeti.statusFall
            Actor.frames = 0
            return
        if self.Level.levelMap[mapY][mapX] != 's' and self.Level.levelMap[mapY + 1][mapX] != 's':
            return
        Actor.status = yeti.statusClimbDown
        Actor.frames = 0
    def Check(self, Actor):
        if Actor.status != yeti.statusStop:
            return
        if self.IsStanding(Actor):
            Actor.hanging = False
            return
        if self.IsHanging(Actor):
            Actor.hanging = True
            return
        Actor.status = yeti.statusFall
        Actor.frames = 0
    def TeaCheck(self):
        for (i, j) in self.teapot:
            if self.Yeti.x == j and self.Yeti.y == i:
                self.teapot.remove((i, j))
                if len(self.teapot) == 0:
                    self.Win = True
    def CatchCheck(self):
        if self.Yeti.x == self.Enemy.x and self.Yeti.y == self.Enemy.y:
            self.Lose = True
        if self.Yeti.x == self.Enemy2.x and self.Yeti.y == self.Enemy2.y:
            self.Lose = True
    def CheckEnemy(self, Actor):
        if Actor.status != yeti.statusStop:
            return
        if self.Yeti.x > Actor.x and self.CanGoRight(Actor):
            self.GoRight(Actor)
            return
        if self.Yeti.x < Actor.x and self.CanGoLeft(Actor):
            self.GoLeft(Actor)
            return
        if self.Yeti.y < Actor.y and self.CanGoUp(Actor):
            self.GoUp(Actor)
            return
        if self.Yeti.y > Actor.y and self.CanGoDown(Actor):
            self.GoDown(Actor)
            return
    def CheckEnemy2(self, Actor):
        if Actor.status != yeti.statusStop:
            return
        if self.Yeti.y < Actor.y and self.CanGoUp(Actor):
            self.GoUp(Actor)
            return
        if self.Yeti.y > Actor.y and self.CanGoDown(Actor):
            self.GoDown(Actor)
            return
        if self.Yeti.x > Actor.x and self.CanGoRight(Actor):
            self.GoRight(Actor)
            return
        if self.Yeti.x < Actor.x and self.CanGoLeft(Actor):
            self.GoLeft(Actor)
            return
        
        
    