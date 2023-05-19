import level
import yeti
import pygame
import math
import random
import game
import finish_screen
import enemy

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

screen = pygame.display.set_mode((512,448))
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
  
  if not curGame.Win and not curGame.Lose:
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

  screen.fill(black)
  curLevel.Display()
  curGame.DisplayLevelDetails()
  curYeti.Display()
  curEnemy.Display()
  curEnemy2.Display()
  if curGame.Win:
    curFinish.DisplayWin()
  if curGame.Lose:
    curFinish.DisplayLose()
  pygame.display.flip()
  clock.tick(60)