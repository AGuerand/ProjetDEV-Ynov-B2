from turtle import right
import pygame
import pygame as pg
from image.idle import *
#from main import windw

#Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        pos = pygame.mouse.get_pos()
        self.images_idle = []
        self.images_idle.append(pygame.image.load("./image/idle/survivor-idle_shotgun_0.png"))
        self.images_idle.append(pygame.image.load("./image/idle/survivor-idle_shotgun_1.png"))
        self.images_idle.append(pygame.image.load("./image/idle/survivor-idle_shotgun_2.png"))
        self.images_idle.append(pygame.image.load("./image/idle/survivor-idle_shotgun_3.png"))
        self.images_idle.append(pygame.image.load("./image/idle/survivor-idle_shotgun_4.png"))
        self.images_idle.append(pygame.image.load("./image/idle/survivor-idle_shotgun_5.png"))
        self.images_idle.append(pygame.image.load("./image/idle/survivor-idle_shotgun_6.png"))
        self.images_idle.append(pygame.image.load("./image/idle/survivor-idle_shotgun_7.png"))
        self.images_idle.append(pygame.image.load("./image/idle/survivor-idle_shotgun_8.png"))
        self.images_idle.append(pygame.image.load("./image/idle/survivor-idle_shotgun_9.png"))
        self.images_idle.append(pygame.image.load("./image/idle/survivor-idle_shotgun_10.png"))
        self.images_idle.append(pygame.image.load("./image/idle/survivor-idle_shotgun_11.png"))
        self.images_idle.append(pygame.image.load("./image/idle/survivor-idle_shotgun_12.png"))
        self.images_idle.append(pygame.image.load("./image/idle/survivor-idle_shotgun_13.png"))
        self.images_idle.append(pygame.image.load("./image/idle/survivor-idle_shotgun_14.png"))
        self.images_idle.append(pygame.image.load("./image/idle/survivor-idle_shotgun_15.png"))
        self.images_idle.append(pygame.image.load("./image/idle/survivor-idle_shotgun_16.png"))
        self.images_idle.append(pygame.image.load("./image/idle/survivor-idle_shotgun_17.png"))
        self.images_idle.append(pygame.image.load("./image/idle/survivor-idle_shotgun_18.png"))
        self.images_idle.append(pygame.image.load("./image/idle/survivor-idle_shotgun_19.png"))
        self.images_move = []
        self.images_move.append(pygame.image.load("./image/move/survivor-move_shotgun_0.png"))
        self.images_move.append(pygame.image.load("./image/move/survivor-move_shotgun_1.png"))
        self.images_move.append(pygame.image.load("./image/move/survivor-move_shotgun_2.png"))
        self.images_move.append(pygame.image.load("./image/move/survivor-move_shotgun_3.png"))
        self.images_move.append(pygame.image.load("./image/move/survivor-move_shotgun_4.png"))
        self.images_move.append(pygame.image.load("./image/move/survivor-move_shotgun_5.png"))
        self.images_move.append(pygame.image.load("./image/move/survivor-move_shotgun_6.png"))
        self.images_move.append(pygame.image.load("./image/move/survivor-move_shotgun_7.png"))
        self.images_move.append(pygame.image.load("./image/move/survivor-move_shotgun_8.png"))
        self.images_move.append(pygame.image.load("./image/move/survivor-move_shotgun_9.png"))
        self.images_move.append(pygame.image.load("./image/move/survivor-move_shotgun_10.png"))
        self.images_move.append(pygame.image.load("./image/move/survivor-move_shotgun_11.png"))
        self.images_move.append(pygame.image.load("./image/move/survivor-move_shotgun_12.png"))
        self.images_move.append(pygame.image.load("./image/move/survivor-move_shotgun_13.png"))
        self.images_move.append(pygame.image.load("./image/move/survivor-move_shotgun_14.png"))
        self.images_move.append(pygame.image.load("./image/move/survivor-move_shotgun_15.png"))
        self.images_move.append(pygame.image.load("./image/move/survivor-move_shotgun_16.png"))
        self.images_move.append(pygame.image.load("./image/move/survivor-move_shotgun_17.png"))
        self.images_move.append(pygame.image.load("./image/move/survivor-move_shotgun_18.png"))
        self.images_move.append(pygame.image.load("./image/move/survivor-move_shotgun_19.png"))
        self.index = 0
        self.image = self.images_idle[self.index]
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        self.color = (250, 120, 60)
        #     POSITION
        self.velX = 0
        self.velY = 0
        self.speed = 4
        self.orientation = "right"
        self.image = pygame.transform.rotate(self.image, 90)
        self.hitbox = (self.x - 10, self.y - 10, 50, 50)
        #    LIFE
        self.maxLife = 100
        self.currentLife = 100
        self.life_barlength = 300
        self.life_ratio = self.maxLife / self.life_barlength

        #DAMAGE
        self.damage=10
        # SPRITE 
        self.leftright = 0
        self.updown = 0
        self.check = 0.0
        # self.image=pygame.Surface((60,60))
        # self.image.fill(self.color)
        # self.image=pygame.image.load(os.path.join(stn.img_folder,img)).convert()
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        # self.x=self.rect.x
    
    # def draw(self, win):
    #     pygame.draw.rect(win, self.color, self.rect)
    #     pygame.draw.rect(win, (255,0,0), self.hitbox,2)
    
    def update(self):
        def rotation(orientation):
            angle = 0
            if orientation == "right":
                angle = 0
            elif orientation == "up":
                angle = 90
            elif orientation == "left":
                angle = 180
            elif orientation == "down":
                angle = 260
            self.image = pygame.transform.rotate(self.image, angle)
        self.velX = 0
        self.velY = 0
        self.check += 1

        if self.leftright == 1:
            if self.check == 2:
                self.index += 1
                if self.index >= len(self.images_move):
                    self.index = 0
                self.image = self.images_move[self.index]
                rotation(self.orientation)
                self.check = 0
            self.velX = -self.speed

        if self.leftright < 0 and self.leftright != 0:
            if self.check == 2:
                self.index += 1
                if self.index >= len(self.images_move):
                    self.index = 0
                self.image = self.images_move[self.index]
                rotation(self.orientation)
                self.check = 0
            self.velX = self.speed

        if self.updown < 0 and self.updown != 0:
            if self.check == 2:
                self.index += 1
                if self.index >= len(self.images_move):
                    self.index = 0
                self.image = self.images_move[self.index]
                rotation(self.orientation)
                self.check = 0
            self.velY = -self.speed

        if self.updown == 1:
            if self.check == 2:
                self.index += 1
                if self.index >= len(self.images_move):
                    self.index = 0
                self.image = self.images_move[self.index]
                rotation(self.orientation)
                self.check = 0
            self.velY = self.speed
        
        if self.check == 2:
            self.index += 1
            if self.index >= len(self.images_idle):
                self.index = 0
            self.image = self.images_idle[self.index]
            rotation(self.orientation)
            self.check = 0
        
        self.x += self.velX
        self.y += self.velY
        self.rect.x=self.x
        self.rect.y=self.y

        self.rect = pygame.Rect(int(self.x), int(self.y), 32, 32)
        self.hitbox = (self.y, self.y, 50, 50)

    def get_damage(self, amount):
        if self.currentLife > 0:
            self.currentLife -= amount
        if self.currentLife <= 0:
            self.currentLife = 0

    def showLife(self, screen, x, y):
        pygame.draw.rect(screen, (255, 0, 0), (x, y, self.life_barlength,  25))