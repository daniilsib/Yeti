import pygame

class FinishScreen:
    def __init__(self, screen):
        self.screen = screen
        self.LoadWin()
    def LoadWin(self):
        self.win_pic = pygame.image.load('pics/Win.png')
        self.win_pic_rect = self.win_pic.get_rect()
        self.lose_pic = pygame.image.load('pics/lose.png')
        self.lose_pic_rect = self.lose_pic.get_rect()
    def DisplayWin(self):
        self.screen.blit(self.win_pic, self.win_pic_rect)
    def DisplayLose(self):
        self.screen.blit(self.lose_pic, self.lose_pic_rect)