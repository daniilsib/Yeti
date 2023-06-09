import pygame
import yeti
import level
import enemy
import sounds
import math
import time

class Game:
    def __init__(self, curYeti: yeti.Yeti, curLevel: level.Level, curEnemy: enemy.Enemy, curEnemy2: enemy.Enemy, curSounds: sounds.GameSound):
        self.Yeti = curYeti
        self.Level = curLevel
        self.Enemy = curEnemy
        self.Enemy2 = curEnemy2
        self.Sound = curSounds
        self.Win = False
        self.Lose = False
        self.levelNum = 0
        self.lives = 15
        self.teapot = []
        for i in range (15):
            for j in range (16):
                if self.Level.levelMap[i][j] == 't':
                    self.teapot.append((i, j))
        self.burnedBlocks = []
    def DisplayLevelDetails(self):
        self.DisplayTeapot()
        self.DisplayBurnedBlocks()
    def DisplayTeapot(self):
        for (i, j) in self.teapot:
          x = j * 32
          y = i * 32
          self.Level.teapot_rect.x = x
          self.Level.teapot_rect.y = y
          self.Level.screen.blit(self.Level.teapot, self.Level.teapot_rect)
    def DisplayBurnedBlocks(self):
        newBurnedBlocks = []
        for (i, j, frames) in self.burnedBlocks:
          if frames == 0:
              self.Level.levelMap[i][j] = 'g'
          else:
              newBurnedBlocks.append((i, j, frames - 1))
          x = j * 32
          y = i * 32
          self.Yeti.broken_grass3_rect.x = x
          self.Yeti.broken_grass3_rect.y = y
          self.Level.screen.blit(self.Yeti.broken_grass3, self.Yeti.broken_grass3_rect)
          self.burnedBlocks = newBurnedBlocks
     
    def IsHanging(self, Actor) -> bool:
        mapX = round(Actor.x)
        mapY = round(Actor.y)
        if self.Level.levelMap[mapY][mapX] == 'h':
            return True
        return False
    def IsStanding(self, Actor) -> bool:
        mapX = round(Actor.x)
        mapY = round(Actor.y)
        if mapY == 14:
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
        if Actor.status != yeti.statusStop:
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
        if Actor.status != yeti.statusStop:
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
        if Actor.status != yeti.statusStop:
            return False
        mapX = round(Actor.x)
        mapY = round(Actor.y)
        if mapY == 14:
            return False
        if self.Level.levelMap[mapY + 1][mapX] == 'b' or self.Level.levelMap[mapY + 1][mapX] == 'g':
            return False
        if self.Level.levelMap[mapY][mapX] == 'h' and self.Level.levelMap[mapY + 1][mapX] != 's':
            return True
        if self.Level.levelMap[mapY + 1][mapX - 1] == 'g' and self.Level.levelMap[mapY][mapX] == ' ':
            return True
        if self.Level.levelMap[mapY][mapX] != 's' and self.Level.levelMap[mapY + 1][mapX] != 's':
            return False
        return True
    def CanFireRight(self, Actor) -> bool:
        if Actor.status != yeti.statusStop and Actor.frames > 2:
            return False
        mapX = round(Actor.x)
        mapY = round(Actor.y)
        if mapY == 14:
            return False
        if self.Level.levelMap[mapY][mapX + 1] != ' ' and self.Level.levelMap[mapY][mapX + 1] != 'h' and self.Level.levelMap[mapY][mapX + 1] != 't':
            return False
        if self.Level.levelMap[mapY + 1][mapX + 1] == 'g':
            return True
        return False
    def CanFireLeft(self, Actor) -> bool:
        if Actor.status != yeti.statusStop and Actor.frames > 2:
            return False
        mapX = round(Actor.x)
        mapY = round(Actor.y)
        if mapY == 14:
            return False
        if self.Level.levelMap[mapY][mapX - 1] != ' ' and self.Level.levelMap[mapY][mapX - 1] != 'h' and self.Level.levelMap[mapY][mapX - 1] != 't':
            return False
        if self.Level.levelMap[mapY + 1][mapX - 1] == 'g':
            return True
        return False
    def FireRight(self, Actor):
        if not self.CanFireRight(Actor):
            return
        self.Sound.PlayBrokeGrass()
        Actor.status = yeti.statusFireRight
        Actor.frames = 0
        mapX = round(Actor.x)
        mapY = round(Actor.y)
        self.Level.levelMap[mapY+1][mapX+1] = ' '
        self.burnedBlocks.append((mapY+1, mapX+1, 30 * 35))
    def FireLeft(self, Actor):
        if not self.CanFireLeft(Actor):
            return
        self.Sound.PlayBrokeGrass()
        Actor.status = yeti.statusFireLeft
        Actor.frames = 0
        mapX = round(Actor.x)
        mapY = round(Actor.y)
        self.Level.levelMap[mapY+1][mapX-1] = ' '
        self.burnedBlocks.append((mapY+1, mapX-1, 30 * 35))
    def GoUp(self, Actor):
        if Actor.status != yeti.statusStop:
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
        if Actor.status != yeti.statusStop:
            return
        mapX = round(Actor.x)
        mapY = round(Actor.y)
        if mapY == 14:
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
    def allTeapotsColl(self) -> bool:
        for (i, j) in self.teapot:
            if self.Yeti.x == j and self.Yeti.y == i:
                self.teapot.remove((i, j))
                self.Sound.PlayTeapot()
            if len(self.teapot) == 0:
                return True
                

    def IsCaught(self) -> bool:
        mapX = round(self.Yeti.x)
        mapY = round(self.Yeti.y)
        if self.Yeti.x == self.Enemy.x and self.Yeti.y == self.Enemy.y:
            return True
        if self.Yeti.x == self.Enemy2.x and self.Yeti.y == self.Enemy2.y:
            return True
        if self.Level.levelMap[mapY][mapX] == 'g':
            return True
        return False
    def CheckEnemy(self, Actor):
        if Actor.status != yeti.statusStop:
            return
        mapX = round(Actor.x)
        mapY = round(Actor.y)
        if self.Level.levelMap[mapY][mapX] == 'g':
            self.Enemy.x = 1
            self.Enemy.y = 0
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
        mapX = round(Actor.x)
        mapY = round(Actor.y)
        if self.Level.levelMap[mapY][mapX] == 'g':
            self.Enemy2.x = 1
            self.Enemy2.y = 0
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
    def RestartGame(self):
        self.RestartLevel(0)
        self.lives = 10
        self.Lose = False
        self.Win = False
        self.levelNum = 0
        self.teapot = []
        for i in range (15):
            for j in range (16):
                if self.Level.levelMap[i][j] == 't':
                    self.teapot.append((i, j))
    def RestartForLevelTwo(self, levelNum):
        self.Yeti.x = 1
        self.Yeti.y = 14
        self.Enemy.x = 1
        self.Enemy.y = 0
        self.Enemy2.x = 1
        self.Enemy2.y = 0
        self.levelNum = levelNum
        self.Yeti.status = yeti.statusStop
        self.Enemy.status = enemy.statusStop
        self.Enemy2.status = enemy.statusStop
        self.burnedBlocks = []
        self.Level.LoadMap(self.levelNum)
        self.teapot = []
        for i in range (15):
            for j in range (16):
                if self.Level.levelMap[i][j] == 't':
                    self.teapot.append((i, j))
    def RestartLevel(self, levelNum):
        self.Yeti.x = 1
        self.Yeti.y = 14
        self.Enemy.x = 1
        self.Enemy.y = 0
        self.Enemy2.x = 1
        self.Enemy2.y = 0
        self.levelNum = levelNum
        self.Yeti.status = yeti.statusStop
        self.Enemy.status = enemy.statusStop
        self.Enemy2.status = enemy.statusStop
        self.burnedBlocks = []
        self.Level.LoadMap(self.levelNum)