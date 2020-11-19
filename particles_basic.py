
"""
Created on Sun Oct 18 20:53:23 2020

@author: abhishekc95
"""
import pygame
import random



pygame.init()


scr_w = 700
scr_h = 700
g = 9       # acceleration due to gravity
win = pygame.display.set_mode((scr_w,scr_h))
blue = (0,0,255)
pygame.display.set_caption("PARTICLES UNDER GRAVITY")
clock = pygame.time.Clock()
t = True

class Particle:
    def __init__(self,r):
        self.x = random.randint(340,360)
        self.y = random.randint(340,360)
        self.r = r
        self.vx = random.randint(-2,2)
        self.vy = random.randint(1,3)
       
        self.ti =  0
        
    def draw(self,win):
        pygame.draw.circle(win,blue,(int(self.x),int(self.y)),self.r)




def gravity(self):
        
    self.x += self.vx*self.ti
    h =  self.vy  - 0.5*g*self.ti**2
    self.y= self.y- h
    self.ti += 0.005
    
def collision_boundary(self):
       
      collide = False   
      if (self.x >=(scr_w-self.r) or self.x <= self.r ):
           self.vx *=-1  
      if (self.y > (scr_h-self.r)):  
            self.y = (scr_h-self.r)
            collide = True
            
      return collide
     
# main program

p = []

while t :
    clock.tick(50)
    p.append(Particle(random.randint(5,10)))    
    for i in p:
        gravity(i)
        if collision_boundary(i) == True:
            p.remove(i)
        i.draw(win)

    pygame.display.update() # rectifed updating after each particle
        
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            t = False
    
    win.fill((255,255,255))
    
pygame.quit()