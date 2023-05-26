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
      if levelNum == 5:
        lines = self.locationString5.splitlines()
      if levelNum == 6:
        lines = self.locationString6.splitlines()
      if levelNum == 7:
        lines = self.locationString7.splitlines()
      if levelNum == 8:
        lines = self.locationString8.splitlines()
      if levelNum == 9:
        lines = self.locationString9.splitlines()
      if levelNum == 10:
        lines = self.locationString10.splitlines()
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
    self.locationString5 = """bs      hhhhshhb
bsggggsg  t s  b
bsggggsg sb s gb
bs  t sg s  s tb
bs    sg sbbs sb
bsbbbgsg s  s  b
bs     t sg s gb
bs        t s tb
bs          s bb
bsggggsbbbggs  b
bsgg  s  tg s  b
bs t  s   s s  b
bs g bsbggbbsggb
bss   s     sggb
bs    s     sgtb"""
    self.locationString6 = """b hhhhhhh      b
b        gsggbbb
bs   ggs tsgg  b
bs   t s  sggt b
bs     s  sgsggb
bs     s  sbs tb
bsg sg s  sbggsb
b t s  s  s   sb
b   s  s  s   sb
b   s  sbbsbggsb
b   s t   s   sb
b   shh   s   sb
bgbbs  sbbsbbgsb
b   s  s     gbb
b   s  s   bs tb"""
    self.locationString7 = """bshh  hhhhs   hb
bs shh    shhh b
bs s  ggsbs   tb
bs st t sbs t gb
bs s  s sbs    b
bs s  s s  sg  b
bshs  s s  shhtb
bs s   ss  t  gb
bs s  s s  s   b
bs s s  s  s  sb
bs ss   s  gggsb
bs ssgggs     sb
bshssgtgsbs   sb
b  ssgsgsbs   sb
b  s    sbs   sb
"""
    self.locationString8 = """bs   hhhhhhhshhb
bs          s  b
bs  t       s  b
ba       gggs  b
bsggbbbs bg s tb
b t    s st s gb
b g    s bb s  b
b s    s    s  b
b gsbbbb    s  b
b  s     sbbb  b
b  s   t s  hhsb
b  sgggs s    sb
b  s t s s  t sb
b  sgggs shhh sb
b      t s    sb
"""
    self.locationString9 = """b  sht   shhhh b
b  s     s    tb
b  s  shhsggg gb
b  bggb  s gg  b
b  bggt  s  g  b
b  bgbb  s  t  b
b        s     b
bshhhhhhhshhhhsb
bs     t s    sb
bs     g s gg sb
bs     t s tt sb
bshshshshshhshsb
b  s s s s  s sb
b  s s s s  s sb
b  s s s s  s sb"""
    self.locationString10 = """b hhhhhhshhhhhhb
b t t   s      b
b   sbbbs     bb
bs  s      g s b
bshhshhhhsbs s b
bs         s s b
b   sb     s s b
bt  sb     s s b
b   sbhhh  sts b
b   sb    bbsb b
b t sb   t  s  b
b   sb      s tb
b   sbshhsbbs bb
b   s       s  b
b   s       s  b"""