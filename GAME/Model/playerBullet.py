import pygame

bulletColor = (0, 0, 0)

class PlayerBullet(pygame.sprite.Sprite):
    def __init__(self, x, y,orientation):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((5,5))
        self.x = x
        self.y = y
        self.orientation = orientation
        #self.mouse_x = mouse_x
        #self.mouse_y = mouse_y
        self.speed = 20
        #self.angle = math.atan2(y - mouse_y, x - mouse_x)
        self.velX = self.speed
        self.velY = self.speed
        # self.rect =  (self.x, self.y)

        #  SPRITE
        self.image.fill((0,0,0))
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)

    def update(self):
        if self.orientation=="left":
            self.rect.x -= int(self.velX)
        if self.orientation=="right":
            self.rect.x += int(self.velX)
        if self.orientation=="up":
            self.rect.y -= int(self.velY)
        if self.orientation=="down":
            self.rect.y += int(self.velY)
        
    
            
        # self.y -= int(self.velY)

        # pygame.draw.circle(display, (255,0,0), (self.x, self.y), 5)