import pygame
import random

class SmallEnemy(pygame.sprite.Sprite):
    energy = 1
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/enemy1.png").convert_alpha()
        self.destory_images = []
        self.destory_images.extend([ \
            pygame.image.load("images/enemy1_down1.png").convert_alpha(),
            pygame.image.load("images/enemy1_down2.png").convert_alpha(),
            pygame.image.load("images/enemy1_down3.png").convert_alpha(),
            pygame.image.load("images/enemy1_down4.png").convert_alpha()
            ])
        self.active = True
        self.rect = self.image.get_rect()
        self.width,self.height = bg_size[0],bg_size[1]
        self.speed = 2
        self.rect.left ,self.rect.top =\
            random.randint(0,self.width-self.rect.width),\
            random.randint(-5 * self.height , 0)
        self.mask = pygame.mask.from_surface(self.image)
        self.energy = SmallEnemy.energy
    def move(self):
         if self.rect.top > self.height:
             self.reset()
         else:
             self.rect.bottom += self.speed
    def reset(self):
        self.active = True
        self.rect.left, self.rect.top = \
            random.randint(0, self.width - self.rect.width), \
            random.randint(-5 * self.height, 0)
        self.energy = SmallEnemy.energy

class MidEnemy(pygame.sprite.Sprite):
    energy = 8
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/enemy2.png").convert_alpha()
        self.destory_images = []
        self.destory_images.extend([ \
            pygame.image.load("images/enemy2_down1.png").convert_alpha(),
            pygame.image.load("images/enemy2_down2.png").convert_alpha(),
            pygame.image.load("images/enemy2_down3.png").convert_alpha(),
            pygame.image.load("images/enemy2_down4.png").convert_alpha()
        ])
        self.active = True
        self.rect = self.image.get_rect()
        self.width,self.height = bg_size[0],bg_size[1]
        self.speed = 1
        self.rect.left ,self.rect.top =\
            random.randint(0,self.width-self.rect.width),\
            random.randint(-10 * self.height , -self.height)
        self.mask = pygame.mask.from_surface(self.image)
        self.energy = MidEnemy.energy
    def move(self):
         if self.rect.top > self.height:
             self.reset()
         else:
             self.rect.bottom += self.speed
    def reset(self):
        self.active = True
        self.energy = MidEnemy.energy
        self.rect.left, self.rect.top = \
            random.randint(0, self.width - self.rect.width), \
            random.randint(-10 * self.height , -self.height)

class BigEnemy(pygame.sprite.Sprite):
    energy = 20
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image1 = pygame.image.load("images/enemy3_n1.png").convert_alpha()
        self.image2 = pygame.image.load("images/enemy3_n2.png").convert_alpha()
        self.destory_images = []
        self.destory_images.extend([ \
            pygame.image.load("images/enemy3_down1.png").convert_alpha(),
            pygame.image.load("images/enemy3_down2.png").convert_alpha(),
            pygame.image.load("images/enemy3_down3.png").convert_alpha(),
            pygame.image.load("images/enemy3_down4.png").convert_alpha(),
            pygame.image.load("images/enemy3_down5.png").convert_alpha(),
            pygame.image.load("images/enemy3_down6.png").convert_alpha()
        ])
        self.active = True
        self.rect = self.image1.get_rect()
        self.width,self.height = bg_size[0],bg_size[1]
        self.speed = 1
        self.rect.left ,self.rect.top =\
            random.randint(0,self.width-self.rect.width),\
            random.randint(-15 * self.height , -5 * self.height)
        self.mask = pygame.mask.from_surface(self.image1)
        self.energy = BigEnemy.energy
    def move(self):
         if self.rect.top > self.height:
             self.reset()
         else:
             self.rect.bottom += self.speed
    def reset(self):
        self.active = True
        self.energy = BigEnemy.energy
        self.rect.left, self.rect.top = \
            random.randint(0, self.width - self.rect.width), \
            random.randint(-10 * self.height , -self.height)