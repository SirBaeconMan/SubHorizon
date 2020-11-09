##IMPORTS##
import pygame
import sys
##CONSTANTS##
WIDTH = 640
HEIGHT = 640
##CODE##
pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))#remember to add pygame.FULLSCREEN later
clock = pygame.time.Clock()
class Player:
    #on initialisation (when game launches), contains most player settings
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 32, 32)
        self.x = int(x)
        self.y = int(y)
        self.color = (250,0,0)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 4
   #draw the player
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
    #on every frame update
    def update(self, selftest=None):
        if selftest == None:
            if self.left_pressed and not self.right_pressed:
                self.velX = -self.speed
           
            elif self.right_pressed and not self.left_pressed:
                self.velX = self.speed
            
            elif self.up_pressed and not self.down_pressed:
                self.velY = -self.speed
            
            elif self.down_pressed and not self.up_pressed:
                self.velY = self.speed
            
        self.x += self.velX
        self.y += self.velY
#initialising the player

player = Player(WIDTH / 8, HEIGHT / 8)

display.fill((12, 24, 36))
player.draw(display)

player.update()
pygame.display.flip()
clock.tick(120)
