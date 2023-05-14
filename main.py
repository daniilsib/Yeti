import level
import yeti
import pygame
import math
import random
import game

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

screen = pygame.display.set_mode((512,448))
curLevel = level.Level(screen)
curYeti = yeti.Yeti(screen)
curGame = game.Game(curYeti, curLevel)
pygame.display.set_caption('YetiRM')

running = True

dir1 = 0
dir2 = 0

clock = pygame.time.Clock()

while running:
  events = pygame.event.get()
  for event in events:
    if event.type == pygame.QUIT:
      running = False
  keys = pygame.key.get_pressed()
  dir1 = dir1%360
  curGame.Check()
  if keys[pygame.K_LEFT]:
    curGame.GoLeft()
  if keys[pygame.K_RIGHT]:
    curGame.GoRight()
  if keys[pygame.K_DOWN]:
    curGame.GoDown()
  if keys[pygame.K_UP]:
    curGame.GoUp()

  screen.fill(black)
  curLevel.Display()
  curGame.DisplayLevelDetails()
  curYeti.Display()

  
  pygame.display.flip()
  clock.tick(60)