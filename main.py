import level
import yeti
import pygame
import sounds
import game
import finish_screen
import enemy
import time

levelStarting = 0

pygame.init()

modeMainMenu = 1
modeGame = 2
modeShowAutors = 3
modeWin = 4
modeLost = 5
modePause = 6
modeLevelStart = 7
modeLifeLost = 8
myFont = pygame.font.SysFont("impact", 21)
curMode = modeMainMenu

WHITE = (255, 255, 255)
black = (0, 0, 0)

screen = pygame.display.set_mode((512,480))
curLevel = level.Level(screen)
curYeti = yeti.Yeti(screen)
curSounds = sounds.GameSound()
curEnemy = enemy.Enemy(screen)
curEnemy2 = enemy.Enemy(screen)
curGame = game.Game(curYeti, curLevel, curEnemy, curEnemy2, curSounds)
curFinish = finish_screen.FinishScreen(screen, curLevel, curYeti)
circle = pygame.image.load('pics/circle.png')
circle = pygame.transform.scale(circle, (32, 32))
circle_rect = circle.get_rect()

pygame.display.set_caption('YetiRM')

running = True

clock = pygame.time.Clock()

while running:
  events = pygame.event.get()
  for event in events:
    if event.type == pygame.QUIT:
      running = False
  keys = pygame.key.get_pressed()
  text = myFont.render(str(curGame.lives), True, (255, 255, 255))
  if curMode == modeLevelStart:
    curLevel.Display()
    curFinish.DisplayStart()
    pygame.display.flip()
    time.sleep(2)
    curMode = modeGame
  if curMode == modeLifeLost:
    curGame.lives -= 1
    curMode = modeGame
  if curMode == modeWin:
    if keys[pygame.K_SPACE]:
      curMode = modeMainMenu
      curGame.RestartGame()
    curFinish.DisplayWin()
  if curMode == modePause:
    curFinish.DisplayPause()
    if keys[pygame.K_SPACE]:
      curMode = modeGame
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
    curSounds.PlayMenu()
    if keys[pygame.K_1]:
      curMode = modeGame
    if keys[pygame.K_2]:
      curMode = modeShowAutors
    if keys[pygame.K_3]:
      exit(1)
  if curMode == modeGame:
    curSounds.StopMenu()
    if levelStarting == 0:
       curMode = modeLevelStart
       for frame in range (0, 120):
        screen.fill(black)
        curLevel.DisplayStart(frame, curYeti)
        pygame.display.flip()
        clock.tick(60)
        levelStarting = 1
    if curGame.allTeapotsColl():
      for frame in range (0, 120):
        screen.fill(black)
        curLevel.DisplayLost(frame, curYeti)
        curYeti.Display()
        curEnemy.Display()
        curEnemy2.Display()
        pygame.display.flip()
        clock.tick(60)
      levelStarting = 0
      if curGame.levelNum == 10:
        curGame.Win = True
      curGame.lives += 1
      curGame.levelNum += 1
      curGame.RestartForLevelTwo(curGame.levelNum)
    curGame.Check(curYeti)
    curGame.CheckEnemy(curEnemy)
    curGame.Check(curEnemy)
    curGame.CheckEnemy2(curEnemy2)
    curGame.Check(curEnemy2)
    if curGame.IsCaught():
      for frame in range (0, 120):
        screen.fill(black)
        curLevel.DisplayLost(frame, curYeti)
        curYeti.Display()
        curEnemy.Display()
        curEnemy2.Display()
        pygame.display.flip()
        clock.tick(60)
      for frame in range (0, 120):
        screen.fill(black)
        curLevel.DisplayStart(frame, curYeti)
        pygame.display.flip()
        clock.tick(60)
        levelStarting = 1
      curMode = modeLifeLost
      curGame.RestartLevel(levelNum=curGame.levelNum)
      if curGame.lives <= 0:
        time.sleep(1)
        curGame.Lose = True
    if keys[pygame.K_w]:
      curGame.FireRight(curYeti)
    if keys[pygame.K_q]:
      curGame.FireLeft(curYeti)
    if keys[pygame.K_LEFT]:
      curGame.GoLeft(curYeti)
    if keys[pygame.K_RIGHT]:
      curGame.GoRight(curYeti)
    if keys[pygame.K_DOWN]:
      curGame.GoDown(curYeti)
    if keys[pygame.K_UP]:
      curGame.GoUp(curYeti)
    if keys[pygame.K_p]:
      curMode = modePause
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
    screen.blit(circle, circle_rect)
    screen.blit(text, (5, 2))

  pygame.display.flip()
  clock.tick(60)