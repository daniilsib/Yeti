import pygame

class Level:
  def __init__(self, screen):
    self.screen = screen
    self.locationString = ""
    rows = 15
    cols = 16

    self.levelMap = [['s']*cols for i in range(rows)]

    self.LoadString()
    self.LoadMap(0)
    self.levelMap[2][2] = 'D'
    self.LoadBlocks()
    self.DisplayText()
  def Display(self):
    for i in range (15):
      #print(" ")
      for j in range (16):
        x = j * 32
        y = i * 32
        #print(self.levelMap[i][j], end="")
        if self.levelMap[i][j] == "g":
          self.grass_rect.x = x
          self.grass_rect.y = y
          self.screen.blit(self.grass, self.grass_rect)
        if self.levelMap[i][j] == "b":
          self.brick_rect.x = x
          self.brick_rect.y = y
          self.screen.blit(self.brick, self.brick_rect)
        if self.levelMap[i][j] == "h":
          self.hbar_rect.x = x
          self.hbar_rect.y = y
          self.screen.blit(self.hbar, self.hbar_rect)
        if self.levelMap[i][j] == "s":
          self.stairs_rect.x = x
          self.stairs_rect.y = y
          self.screen.blit(self.stairs, self.stairs_rect)
  def DisplayText(self):
    for i in range (15):
      print(" ")
      for j in range (16):
        print(self.levelMap[i][j], end="")
  def LoadMap(self, levelNum):
      if levelNum == 0:
        lines = self.locationString0.splitlines()
      if levelNum == 1:
        lines = self.locationString1.splitlines()
      if levelNum == 2:
        lines = self.locationString2.splitlines()
      if levelNum == 3:
        lines = self.locationString3.splitlines()
      if levelNum == 4:
        lines = self.locationString4.splitlines()
      for i in range (15):
        for j in range (16):
          k=lines[i][j]
          self.levelMap[i][j] = k
        print(" ")
  def LoadBlocks(self):
    self.stairs = pygame.image.load('pics/stairs.png')
    self.stairs = pygame.transform.scale(self.stairs, (32, 32))
    self.stairs_rect = self.stairs.get_rect()
    self.grass = pygame.image.load('pics/grass.png')
    self.grass = pygame.transform.scale(self.grass, (32, 32))
    self.grass_rect = self.grass.get_rect()
    self.brick = pygame.image.load('pics/brick.png')
    self.brick = pygame.transform.scale(self.brick, (32, 32))
    self.brick_rect = self.brick.get_rect()
    self.hbar = pygame.image.load('pics/hbar.png')
    self.hbar = pygame.transform.scale(self.hbar, (32, 32))
    self.hbar_rect = self.hbar.get_rect()
    self.teapot = pygame.image.load('pics/teapot.png')
    self.teapot = pygame.transform.scale(self.teapot, (32, 32))
    self.teapot_rect = self.teapot.get_rect()
  def LoadString(self):
    self.locationString0 = """bs  hhhhhhhhhhsb
bs t          sb
bs gh  t sggggsb
bs     ggs     b
bs       s     b
bs   t   sht   b
bshhhs   s gggsb
b    s   s    sb
b    s   s    sb
bsgggbs  s  sbsb
bs    s  s  s  b
bs    s  s  s  b
bs    shhs  s  b
bs    s  b  s  b
bs t  s  bt s  b"""
    self.locationString1 = """bshhhhhhhhhhshhb
bs          s  b
bs t  t  t  s tb
bs          s  b
bs          s  b
bs shhs  shhshhb
bs s  s  s  s  b
bs s  ssss  s  b
bsgsgggssgggsggb
b  s   ss   s  b
b  s   ss   s  b
b  s   ss   s  b
bhhshhhsshhhshhb
b  s t ss t s  b
b  s   ss   s  b"""
    self.locationString2 = """b      shhhhhhhb
bs     s       b
bs     shhsg   b
bshhhhhs   t   b
b      s       b
b      s     sgb
bshhhhhsbggb sgb
bs           sgb
bs t     t   sgb
bshhhhhhhhhs sgb
b          s  tb
bshhhhhs   sbbgb
bs     s   s   b
bs     sgggbs  b
bs     sggtbs tb"""
    self.locationString3 = """bshhhhhhhhhhhh b
bs             b
bs bbbb  bbbbb b
bs hhhs  hhhs  b
bs t  s  t  s  b
bs    s     s  b
bdggs ggggs ggsb
b   s     s   sb
b   s     s t sb
b t shhhhhs ggsb
b ggs     s    b
b   s bgb s   tb
b   s btb shhhsb
b   s     s   sb
bsggsgggggsggggb"""
    self.locationString4 = """bshhhhh  t    hb
bs  t  sbbbsbs b
bsgggggs   s s b
b bt   s   shh b
b bb t s   s   b
b    ggsgggsgggb
b t    s t s   b
bsbb   s b s  sb
bshhhhhs s s  sb
bs   t sbbsbggsb
bs   g s  s   sb
bs     s ts t sb
b gsbsbbbgsbbbsb
b  sbs    s   sb
b tsbs    s  tsb"""