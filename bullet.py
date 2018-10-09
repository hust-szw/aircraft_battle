import pygame

class Bullet1(pygame.sprite.Sprite):
    def __init__(self,position):
        self.image = pygame.image.load('images/bullet1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left , self.rect.top = position
        self.speed = 12
        self.mask = pygame.mask.from_surface(self.image)
        self.active = True

    def move(self):
        self.rect.top -= self.speed

        if self.rect.top < 0:
            self.active = False

    def reset(self,position):
        self.rect.left,self.rect.top = position
        self.active = True