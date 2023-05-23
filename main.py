import level
import yeti
import pygame
import math
import random
import game
import finish_screen
import enemy

pygame.init()

modeMainMenu = 1
modeGame = 2
modeShowAutors = 3
modeWin = 4
modeLost = 5

curMode = modeMainMenu

white = (255, 255, 255)
black = (0, 0, 0)

screen = pygame.display.set_mode((512,480))
curLevel = level.Level(screen)
curYeti = yeti.Yeti(screen)
curEnemy = enemy.Enemy(screen)
curEnemy2 = enemy.Enemy(screen)
curGame = game.Game(curYeti, curLevel, curEnemy, curEnemy2)
curFinish = finish_screen.FinishScreen(screen)

pygame.display.set_caption('YetiRM')

running = True

clock = pygame.time.Clock()

while running:
  events = pygame.event.get()
  for event in events:
    if event.type == pygame.QUIT:
      running = False
  keys = pygame.key.get_pressed()
  if curMode == modeWin:
    if keys[pygame.K_SPACE]:
      curMode = modeMainMenu
      curGame.RestartGame()
    curFinish.DisplayWin()
  if curMode == modeLost:
    if keys[pygame.K_SPACE]:
      curMode = modeMainMenu
      curGame.RestartGame()
    curFinish.DisplayLose()
  if curMode == modeShowAutors:
    curFinish.DisplayShowAutors()
    if keys[pygame.K_SPACE]:
      curMode = modeMainMenu
  if curMode == modeMainMenu:
    curFinish.DisplayMainMenu()
    if keys[pygame.K_1]:
      curMode = modeGame
    if keys[pygame.K_2]:
      curMode = modeShowAutors
    if keys[pygame.K_3]:
      exit(1)
  if curMode == modeGame:
    curGame.TeaCheck()
    curGame.Check(curYeti)
    curGame.CheckEnemy(curEnemy)
    curGame.Check(curEnemy)
    curGame.CheckEnemy2(curEnemy2)
    curGame.Check(curEnemy2)
    curGame.CatchCheck()
    if keys[pygame.K_LEFT]:
      curGame.GoLeft(curYeti)
    if keys[pygame.K_RIGHT]:
      curGame.GoRight(curYeti)
    if keys[pygame.K_DOWN]:
      curGame.GoDown(curYeti)
    if keys[pygame.K_UP]:
      curGame.GoUp(curYeti)
    if keys[pygame.K_w]:
      curGame.FireRight(curYeti)
    if keys[pygame.K_q]:
      curGame.FireLeft(curYeti)
    screen.fill(black)
    curLevel.Display()
    curGame.DisplayLevelDetails()
    curYeti.Display()
    curEnemy.Display()
    curEnemy2.Display()
    if curGame.Win:
      curMode = modeWin
    if curGame.Lose:
      curMode = modeLost

  pygame.display.flip()
  clock.tick(60)