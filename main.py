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

player1 = pygame.image.load('pics/yetil1.png')
player1_rect = player1.get_rect()

player2 = pygame.image.load('pics/yeti_fall.png')
player2_rect = player2.get_rect()

food = pygame.image.load('pics/teapot.png')
food_rect = food.get_rect()

food_rect.x = 400
food_rect.y = 300

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
  if keys[pygame.K_a]:
    dir1 += 1
  if keys[pygame.K_d]:
    dir1 -= 1
  if keys[pygame.K_w]:
    player1_rect.x -= math.sin(dir1*(math.pi/180)) * 5
    player1_rect.y -= math.cos(dir1*(math.pi/180)) * 5
  if keys[pygame.K_s]:
    player1_rect.x += math.sin(dir1*(math.pi/180)) * 5
    player1_rect.y += math.cos(dir1*(math.pi/180)) * 5
  
  dir1 = dir1%360
  
  player1_rot = pygame.transform.rotate(player1, dir1)
  player1_rect_rot = player1_rot.get_rect(center = player1_rect.center)
  curGame.Check()
  if keys[pygame.K_LEFT]:
    curGame.GoLeft()
  if keys[pygame.K_RIGHT]:
    curGame.GoRight()
  if keys[pygame.K_SPACE]:
    curYeti.status = yeti.statusStop
  if keys[pygame.K_DOWN]:
    curGame.GoDown()
  if keys[pygame.K_UP]:
    curGame.GoUp()
  if keys[pygame.K_f]:
    curYeti.status = yeti.statusFall
  if keys[pygame.K_o]:
    curYeti.status = yeti.statusHangingLeft
  if keys[pygame.K_p]:
    curYeti.status = yeti.statusHangingRight
  if keys[pygame.K_q]:
    curYeti.status = yeti.statusHangingStop

  if food_rect.colliderect(player1_rect):
    food_rect.x = random.randint(0, 750)
    food_rect.x = random.randint(0, 550)
  
  if food_rect.colliderect(player2_rect):
    food_rect.x = random.randint(0, 750)
    food_rect.x = random.randint(0, 550)
  
  dir2 = dir2%360
  
  player2_rot = pygame.transform.rotate(player2, dir2)
  player2_rect_rot = player2_rot.get_rect(center = player2_rect.center)

  screen.fill(black)
  curLevel.Display()
  curYeti.Display()
  screen.blit(player1_rot, player1_rect_rot)
  screen.blit(player2_rot, player2_rect_rot)
  screen.blit(food, food_rect)

  
  pygame.display.flip()
  clock.tick(60)