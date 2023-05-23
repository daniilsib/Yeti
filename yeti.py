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

class Yeti:
    def __init__(self, screen):
        self.hanging = False
        self.screen = screen
        self.x = 1
        self.y = 14
        self.status = statusStop
        self.frames = 0
        self.LoadYeti()
    def LoadYeti(self):
        self.yeti_standing_l = pygame.image.load('pics/yeti_standing_l.png')
        self.yeti_standing_l = pygame.transform.scale(self.yeti_standing_l, (32, 32))
        self.yeti_standing_l_rect = self.yeti_standing_l.get_rect()
        self.yeti_standing_r = pygame.image.load('pics/yeti_standing_r.png')
        self.yeti_standing_r = pygame.transform.scale(self.yeti_standing_r, (32, 32))
        self.yeti_standing_r_rect = self.yeti_standing_r.get_rect()
        self.yetil2 = pygame.image.load('pics/yetil2.png')
        self.yetil2 = pygame.transform.scale(self.yetil2, (32, 32))
        self.yetil2_rect = self.yetil2.get_rect()
        self.yetil1 = pygame.image.load('pics/yetil1.png')
        self.yetil1 = pygame.transform.scale(self.yetil1, (32, 32))
        self.yetil1_rect = self.yetil1.get_rect()
        self.yetir1 = pygame.image.load('pics/yetir1.png')
        self.yetir1 = pygame.transform.scale(self.yetir1, (32, 32))
        self.yetir1_rect = self.yetir1.get_rect()
        self.yetir2 = pygame.image.load('pics/yetir2.png')
        self.yetir2 = pygame.transform.scale(self.yetir2, (32, 32))
        self.yetir2_rect = self.yetir2.get_rect()
        self.yeti_climbl = pygame.image.load('pics/yeti_climbl.png')
        self.yeti_climbl = pygame.transform.scale(self.yeti_climbl, (32, 32))
        self.yeti_climbl_rect = self.yeti_climbl.get_rect()
        self.yeti_climbr = pygame.image.load('pics/yeti_climbr.png')
        self.yeti_climbr = pygame.transform.scale(self.yeti_climbr, (32, 32))
        self.yeti_climbr_rect = self.yeti_climbr.get_rect()
        self.yeti_canding = pygame.image.load('pics/yeti_canging.png')
        self.yeti_canding = pygame.transform.scale(self.yeti_canding, (32, 32))
        self.yeti_canding_rect = self.yeti_canding.get_rect()
        self.yeti_canding2 = pygame.image.load('pics/yeti_canding2.png')
        self.yeti_canding2 = pygame.transform.scale(self.yeti_canding2, (32, 32))
        self.yeti_canding2_rect = self.yeti_canding2.get_rect()
        self.yeti_candingr = pygame.image.load('pics/yeti_cangingr.png')
        self.yeti_candingr = pygame.transform.scale(self.yeti_candingr, (32, 32))
        self.yeti_candingr_rect = self.yeti_candingr.get_rect()
        self.yeti_canging2r = pygame.image.load('pics/yeti_canding2r.png')
        self.yeti_canging2r = pygame.transform.scale(self.yeti_canging2r, (32, 32))
        self.yeti_canging2r_rect = self.yeti_canging2r.get_rect()
        self.yeti_hanging_stop = pygame.image.load('pics/yeti_hanging_stop.png')
        self.yeti_hanging_stop = pygame.transform.scale(self.yeti_hanging_stop, (32, 32))
        self.yeti_hanging_stop_rect = self.yeti_hanging_stop.get_rect()
        self.yeti_hanging_stop2 = pygame.image.load('pics/yeti_hanging_stop2.png')
        self.yeti_hanging_stop2 = pygame.transform.scale(self.yeti_hanging_stop2, (32, 32))
        self.yeti_hanging_stop2_rect = self.yeti_hanging_stop2.get_rect()
        self.yeti_fall = pygame.image.load('pics/yeti_fall.png')
        self.yeti_fall = pygame.transform.scale(self.yeti_fall, (32, 32))
        self.yeti_fall_rect = self.yeti_fall.get_rect()
        self.yeti_fall2 = pygame.image.load('pics/yeti_fall2.png')
        self.yeti_fall2 = pygame.transform.scale(self.yeti_fall2, (32, 32))
        self.yeti_fall2_rect = self.yeti_fall2.get_rect()
        self.yeti_firel = pygame.image.load('pics/yeti_firel.png')
        self.yeti_firel = pygame.transform.scale(self.yeti_firel, (32, 32))
        self.yeti_firel_rect = self.yeti_firel.get_rect()
        self.yeti_firel2 = pygame.image.load('pics/yeti_firel2.png')
        self.yeti_firel2 = pygame.transform.scale(self.yeti_firel2, (32, 32))
        self.yeti_firel2_rect = self.yeti_firel2.get_rect()
        self.yeti_firer = pygame.image.load('pics/yeti_firer.png')
        self.yeti_firer = pygame.transform.scale(self.yeti_firer, (32, 32))
        self.yeti_firer_rect = self.yeti_firer.get_rect()
        self.yeti_firer2 = pygame.image.load('pics/yeti_firer2.png')
        self.yeti_firer2 = pygame.transform.scale(self.yeti_firer2, (32, 32))
        self.yeti_firer2_rect = self.yeti_firer2.get_rect()
        self.broken_grass = pygame.image.load('pics/broken_grass.png')
        self.broken_grass = pygame.transform.scale(self.broken_grass, (32, 32))
        self.broken_grass_rect = self.broken_grass.get_rect()
        self.broken_grassr = pygame.image.load('pics/broken_grassr.png')
        self.broken_grassr = pygame.transform.scale(self.broken_grassr, (32, 32))
        self.broken_grassr_rect = self.broken_grassr.get_rect()
        self.broken_grass2 = pygame.image.load('pics/broken_grass2.png')
        self.broken_grass2 = pygame.transform.scale(self.broken_grass2, (32, 32))
        self.broken_grass2_rect = self.broken_grass2.get_rect()
        self.broken_grass3 = pygame.image.load('pics/broken_grass3.png')
        self.broken_grass3 = pygame.transform.scale(self.broken_grass3, (32, 32))
        self.broken_grass3_rect = self.broken_grass3.get_rect()

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
        if self.status == statusFireRight:
            self.DisplayFireRight()
        if self.status == statusFireLeft:
            self.DisplayFireLeft()
    def DisplayStop(self):
        x = self.x * 32
        y = self.y * 32
        if self.frames < 15:
            self.yeti_standing_l_rect.x = x
            self.yeti_standing_l_rect.y = y
            self.screen.blit(self.yeti_standing_l, self.yeti_standing_l_rect)
        else:
            self.yeti_standing_r_rect.x = x
            self.yeti_standing_r_rect.y = y
            self.screen.blit(self.yeti_standing_r, self.yeti_standing_r_rect)
        if self.frames >= 30:
            self.frames = 0
    def DisplayRunLeft(self):
        x = self.x * 32 - 32 * self.frames / 30.0
        y = self.y * 32
        if self.frames < 15:
            self.yetil1_rect.x = x
            self.yetil1_rect.y = y
            self.screen.blit(self.yetil1, self.yetil1_rect)
        else:
            self.yetil2_rect.x = x
            self.yetil2_rect.y = y
            self.screen.blit(self.yetil2, self.yetil2_rect)
        if self.frames >= 30:
            self.x -= 1
            self.status = statusStop
    def DisplayRunRight(self):
        x = self.x * 32 + 32 * self.frames / 30.0
        y = self.y * 32
        if self.frames < 15:
            self.yetir1_rect.x = x
            self.yetir1_rect.y = y
            self.screen.blit(self.yetir1, self.yetir1_rect)
        else:
            self.yetir2_rect.x = x
            self.yetir2_rect.y = y
            self.screen.blit(self.yetir2, self.yetir2_rect)
        if self.frames >= 30:
            self.x += 1
            self.status = statusStop
    def DisplayClimbUp(self):
        x = self.x * 32
        y = self.y * 32 - 32 * self.frames / 30.0
        if self.frames < 15:
            self.yeti_climbl_rect.x = x
            self.yeti_climbl_rect.y = y
            self.screen.blit(self.yeti_climbl, self.yeti_climbl_rect)
        else:
            self.yeti_climbr_rect.x = x
            self.yeti_climbr_rect.y = y
            self.screen.blit(self.yeti_climbr, self.yeti_climbr_rect)
        if self.frames >= 30:
            self.y -= 1
            self.status = statusStop
    def DisplayClimbDown(self):
        x = self.x * 32
        y = self.y * 32 + 32 * self.frames / 30.0
        if self.frames < 15:
            self.yeti_climbl_rect.x = x
            self.yeti_climbl_rect.y = y
            self.screen.blit(self.yeti_climbl, self.yeti_climbl_rect)
        else:
            self.yeti_climbr_rect.x = x
            self.yeti_climbr_rect.y = y
            self.screen.blit(self.yeti_climbr, self.yeti_climbr_rect)
        if self.frames >= 30:
            self.y += 1
            self.status = statusStop
    def DisplayFall(self):
        x = self.x * 32
        y = self.y * 32 + 32 * self.frames / 30.0
        if self.frames < 15:
            self.yeti_fall_rect.x = x
            self.yeti_fall_rect.y = y
            self.screen.blit(self.yeti_fall, self.yeti_fall_rect)
        else:
            self.yeti_fall2_rect.x = x
            self.yeti_fall2_rect.y = y
            self.screen.blit(self.yeti_fall2, self.yeti_fall2_rect)
        if self.frames >= 30:
            self.y += 1
            self.status = statusStop

    def DisplayHangingLeft(self):
        x = self.x * 32 - 32 * self.frames / 30.0
        y = self.y * 32
        if self.frames < 15:
            self.yeti_canding_rect.x = x
            self.yeti_canding_rect.y = y
            self.screen.blit(self.yeti_canding, self.yeti_canding_rect)
        else:
            self.yeti_canding2_rect.x = x
            self.yeti_canding2_rect.y = y
            self.screen.blit(self.yeti_canding2, self.yeti_canding2_rect)
        if self.frames >= 30:
            self.x -= 1
            self.status = statusStop
    def DisplayHangingRight(self):
        x = self.x * 32 + 32 * self.frames / 30.0
        y = self.y * 32
        if self.frames < 15:
            self.yeti_candingr_rect.x = x
            self.yeti_candingr_rect.y = y
            self.screen.blit(self.yeti_candingr, self.yeti_candingr_rect)
        else:
            self.yeti_canging2r_rect.x = x
            self.yeti_canging2r_rect.y = y
            self.screen.blit(self.yeti_canging2r, self.yeti_canging2r_rect)
        if self.frames >= 30:
            self.x += 1
            self.status = statusStop
    def DisplayHangingStop(self):
        x = self.x * 32
        y = self.y * 32
        if self.frames < 15:
            self.yeti_hanging_stop_rect.x = x
            self.yeti_hanging_stop_rect.y = y
            self.screen.blit(self.yeti_hanging_stop, self.yeti_hanging_stop_rect)
        else:
            self.yeti_hanging_stop2_rect.x = x
            self.yeti_hanging_stop2_rect.y = y
            self.screen.blit(self.yeti_hanging_stop2, self.yeti_hanging_stop2_rect)
        if self.frames >= 30:
            self.frames = 0
    def DisplayFireRight(self):
        x = self.x * 32
        y = self.y * 32

        if self.frames < 15:
            self.yeti_firer_rect.x = x
            self.yeti_firer_rect.y = y
            x32 = self.yeti_firer_rect.x + 32
            y32 = self.yeti_firer_rect.y + 32
            self.broken_grass_rect.x = x32
            self.broken_grass_rect.y = y32
            self.broken_grass2_rect.x = x32
            self.broken_grass2_rect.y = y
            self.screen.blit(self.broken_grass, self.broken_grass_rect)
            self.screen.blit(self.broken_grass2, self.broken_grass2_rect)
            self.screen.blit(self.yeti_firer, self.yeti_firer_rect)
        else:
            x32 = self.yeti_firer2_rect.x + 32
            y32 = self.yeti_firer2_rect.y + 32
            self.broken_grass3_rect.x = x32
            self.broken_grass3_rect.y = y32
            self.yeti_firel2_rect.x = x
            self.yeti_firel2_rect.y = y
            self.screen.blit(self.broken_grass3, self.broken_grass3_rect)
            self.yeti_firer2_rect.x = x
            self.yeti_firer2_rect.y = y
            self.screen.blit(self.yeti_firer2, self.yeti_firer2_rect)
        if self.frames >= 30:
            self.frames = 0
            self.status = statusStop
    def DisplayFireLeft(self):
        x = self.x * 32
        y = self.y * 32
        if self.frames < 15:
            self.yeti_firel_rect.x = x
            self.yeti_firel_rect.y = y
            self.screen.blit(self.yeti_firel, self.yeti_firel_rect)
            x32 = self.yeti_firel_rect.x - 32
            y32 = self.yeti_firel_rect.y + 32
            self.broken_grassr_rect.x = x32
            self.broken_grassr_rect.y = y32
            self.broken_grass2_rect.x = x32
            self.broken_grass2_rect.y = y
            self.screen.blit(self.broken_grassr, self.broken_grassr_rect)
            self.screen.blit(self.broken_grass2, self.broken_grass2_rect)
        else:
            x32 = self.yeti_firel2_rect.x - 32
            y32 = self.yeti_firel2_rect.y + 32
            self.broken_grass3_rect.x = x32
            self.broken_grass3_rect.y = y32
            self.yeti_firel2_rect.x = x
            self.yeti_firel2_rect.y = y
            self.screen.blit(self.broken_grass3, self.broken_grass3_rect)
            self.screen.blit(self.yeti_firel2, self.yeti_firel2_rect)
        if self.frames >= 30:
            self.frames = 0
            self.status = statusStop