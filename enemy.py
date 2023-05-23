import pygame

statusStop = 0
statusFall = 1
statusRunLeft = 2
statusRunRight = 3
statusHangingLeft = 4
statusHangingRight = 5
statusHangingStop = 6
statusClimbDown = 7
statusClimbUp = 8
statusFireRight = 9
statusFireLeft = 10


class Enemy:
    def __init__(self, screen):
        self.hanging = False
        self.screen = screen
        self.x = 1
        self.y = 0
        self.status = statusStop
        self.frames = 0
        self.LoadEnemy()
    def LoadEnemy(self):
        self.enemy_standing_l = pygame.image.load('pics/enemy_standing_l.png')
        self.enemy_standing_l = pygame.transform.scale(self.enemy_standing_l, (32, 32))
        self.enemy_standing_l_rect = self.enemy_standing_l.get_rect()
        self.enemy_standing_r = pygame.image.load('pics/enemy_standing_r.png')
        self.enemy_standing_r = pygame.transform.scale(self.enemy_standing_r, (32, 32))
        self.enemy_standing_r_rect = self.enemy_standing_r.get_rect()
        self.enemyl2 = pygame.image.load('pics/enemyl2.png')
        self.enemyl2 = pygame.transform.scale(self.enemyl2, (32, 32))
        self.enemyl2_rect = self.enemyl2.get_rect()
        self.enemyl1 = pygame.image.load('pics/enemyl1.png')
        self.enemyl1 = pygame.transform.scale(self.enemyl1, (32, 32))
        self.enemyl1_rect = self.enemyl1.get_rect()
        self.enemyr1 = pygame.image.load('pics/enemyr1.png')
        self.enemyr1 = pygame.transform.scale(self.enemyr1, (32, 32))
        self.enemyr1_rect = self.enemyr1.get_rect()
        self.enemyr2 = pygame.image.load('pics/enemyr2.png')
        self.enemyr2 = pygame.transform.scale(self.enemyr2, (32, 32))
        self.enemyr2_rect = self.enemyr2.get_rect()
        self.enemy_climbl = pygame.image.load('pics/enemy_climbl.png')
        self.enemy_climbl = pygame.transform.scale(self.enemy_climbl, (32, 32))
        self.enemy_climbl_rect = self.enemy_climbl.get_rect()
        self.enemy_climbr = pygame.image.load('pics/enemy_climbr.png')
        self.enemy_climbr = pygame.transform.scale(self.enemy_climbr, (32, 32))
        self.enemy_climbr_rect = self.enemy_climbr.get_rect()
        self.enemy_hanging = pygame.image.load('pics/enemy_hanging.png')
        self.enemy_hanging = pygame.transform.scale(self.enemy_hanging, (32, 32))
        self.enemy_hanging_rect = self.enemy_hanging.get_rect()
        self.enemy_hanging2 = pygame.image.load('pics/enemy_hanging2.png')
        self.enemy_hanging2 = pygame.transform.scale(self.enemy_hanging2, (32, 32))
        self.enemy_hanging2_rect = self.enemy_hanging2.get_rect()
        self.enemy_hangingr = pygame.image.load('pics/enemy_hangingr.png')
        self.enemy_hangingr = pygame.transform.scale(self.enemy_hangingr, (32, 32))
        self.enemy_hangingr_rect = self.enemy_hangingr.get_rect()
        self.enemy_hanging2r = pygame.image.load('pics/enemy_hanging2r.png')
        self.enemy_hanging2r = pygame.transform.scale(self.enemy_hanging2r, (32, 32))
        self.enemy_hanging2r_rect = self.enemy_hanging2r.get_rect()
        self.enemy_hanging_stop = pygame.image.load('pics/enemy_hanging_stop.png')
        self.enemy_hanging_stop = pygame.transform.scale(self.enemy_hanging_stop, (32, 32))
        self.enemy_hanging_stop_rect = self.enemy_hanging_stop.get_rect()
        self.enemy_hanging_stop2 = pygame.image.load('pics/enemy_hanging_stop2.png')
        self.enemy_hanging_stop2 = pygame.transform.scale(self.enemy_hanging_stop2, (32, 32))
        self.enemy_hanging_stop2_rect = self.enemy_hanging_stop2.get_rect()
        self.enemy_fall = pygame.image.load('pics/enemy_fall.png')
        self.enemy_fall = pygame.transform.scale(self.enemy_fall, (32, 32))
        self.enemy_fall_rect = self.enemy_fall.get_rect()
        self.enemy_fall2 = pygame.image.load('pics/enemy_fall2.png')
        self.enemy_fall2 = pygame.transform.scale(self.enemy_fall2, (32, 32))
        self.enemy_fall2_rect = self.enemy_fall2.get_rect()

    def Display(self):
        self.frames += 1
        if self.status == statusStop:
            if self.hanging:
                self.DisplayHangingStop()
                return
            self.DisplayStop()
        if self.status == statusRunLeft:
            self.DisplayRunLeft()
        if self.status == statusRunRight:
            self.DisplayRunRight()
        if self.status == statusClimbUp:
            self.DisplayClimbUp()
        if self.status == statusClimbDown:
            self.DisplayClimbDown()
        if self.status == statusFall:
            self.DisplayFall()
        if self.status == statusHangingLeft:
            self.DisplayHangingLeft()
        if self.status == statusHangingRight:
            self.DisplayHangingRight()
        if self.status == statusHangingStop:
            self.DisplayHangingStop()
    def DisplayStop(self):
        x = self.x * 32
        y = self.y * 32
        if self.frames < 15:
            self.enemy_standing_l_rect.x = x
            self.enemy_standing_l_rect.y = y
            self.screen.blit(self.enemy_standing_l, self.enemy_standing_l_rect)
        else:
            self.enemy_standing_r_rect.x = x
            self.enemy_standing_r_rect.y = y
            self.screen.blit(self.enemy_standing_r, self.enemy_standing_r_rect)
        if self.frames >= 30:
            self.frames = 0
    def DisplayRunLeft(self):
        x = self.x * 32 - 32 * self.frames / 30.0
        y = self.y * 32
        if self.frames < 15:
            self.enemyl1_rect.x = x
            self.enemyl1_rect.y = y
            self.screen.blit(self.enemyl1, self.enemyl1_rect)
        else:
            self.enemyl2_rect.x = x
            self.enemyl2_rect.y = y
            self.screen.blit(self.enemyl2, self.enemyl2_rect)
        if self.frames >= 30:
            self.x -= 1
            self.status = statusStop
    def DisplayRunRight(self):
        x = self.x * 32 + 32 * self.frames / 30.0
        y = self.y * 32
        if self.frames < 15:
            self.enemyr1_rect.x = x
            self.enemyr1_rect.y = y
            self.screen.blit(self.enemyr1, self.enemyr1_rect)
        else:
            self.enemyr2_rect.x = x
            self.enemyr2_rect.y = y
            self.screen.blit(self.enemyr2, self.enemyr2_rect)
        if self.frames >= 30:
            self.x += 1
            self.status = statusStop
    def DisplayClimbUp(self):
        x = self.x * 32
        y = self.y * 32 - 32 * self.frames / 30.0
        if self.frames < 15:
            self.enemy_climbl_rect.x = x
            self.enemy_climbl_rect.y = y
            self.screen.blit(self.enemy_climbl, self.enemy_climbl_rect)
        else:
            self.enemy_climbr_rect.x = x
            self.enemy_climbr_rect.y = y
            self.screen.blit(self.enemy_climbr, self.enemy_climbr_rect)
        if self.frames >= 30:
            self.y -= 1
            self.status = statusStop
    def DisplayClimbDown(self):
        x = self.x * 32
        y = self.y * 32 + 32 * self.frames / 30.0
        if self.frames < 15:
            self.enemy_climbl_rect.x = x
            self.enemy_climbl_rect.y = y
            self.screen.blit(self.enemy_climbl, self.enemy_climbl_rect)
        else:
            self.enemy_climbr_rect.x = x
            self.enemy_climbr_rect.y = y
            self.screen.blit(self.enemy_climbr, self.enemy_climbr_rect)
        if self.frames >= 30:
            self.y += 1
            self.status = statusStop
    def DisplayFall(self):
        x = self.x * 32
        y = self.y * 32 + 32 * self.frames / 30.0
        if self.frames < 15:
            self.enemy_fall_rect.x = x
            self.enemy_fall_rect.y = y
            self.screen.blit(self.enemy_fall, self.enemy_fall_rect)
        else:
            self.enemy_fall2_rect.x = x
            self.enemy_fall2_rect.y = y
            self.screen.blit(self.enemy_fall2, self.enemy_fall2_rect)
        if self.frames >= 30:
            self.y += 1
            self.status = statusStop

    def DisplayHangingLeft(self):
        x = self.x * 32 - 32 * self.frames / 30.0
        y = self.y * 32
        if self.frames < 15:
            self.enemy_hanging_rect.x = x
            self.enemy_hanging_rect.y = y
            self.screen.blit(self.enemy_hanging, self.enemy_hanging_rect)
        else:
            self.enemy_hanging2_rect.x = x
            self.enemy_hanging2_rect.y = y
            self.screen.blit(self.enemy_hanging2, self.enemy_hanging2_rect)
        if self.frames >= 30:
            self.x -= 1
            self.status = statusStop
    def DisplayHangingRight(self):
        x = self.x * 32 + 32 * self.frames / 30.0
        y = self.y * 32
        if self.frames < 15:
            self.enemy_hangingr_rect.x = x
            self.enemy_hangingr_rect.y = y
            self.screen.blit(self.enemy_hangingr, self.enemy_hangingr_rect)
        else:
            self.enemy_hanging2r_rect.x = x
            self.enemy_hanging2r_rect.y = y
            self.screen.blit(self.enemy_hanging2r, self.enemy_hanging2r_rect)
        if self.frames >= 30:
            self.x += 1
            self.status = statusStop
    def DisplayHangingStop(self):
        x = self.x * 32
        y = self.y * 32
        if self.frames < 15:
            self.enemy_hanging_stop_rect.x = x
            self.enemy_hanging_stop_rect.y = y
            self.screen.blit(self.enemy_hanging_stop, self.enemy_hanging_stop_rect)
        else:
            self.enemy_hanging_stop2_rect.x = x
            self.enemy_hanging_stop2_rect.y = y
            self.screen.blit(self.enemy_hanging_stop2, self.enemy_hanging_stop2_rect)
        if self.frames >= 30:
            self.frames = 0