import pygame  # load pygame keywords
import sys     # let  python use your file system
import os      # help python identify your OS
pygame.display.set_mode()
pygame.init()

screenWidth = 1920
screenHeight =  768
win = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png')]
combRight = [pygame.image.load('WR01001.png'), pygame.image.load('WR01002.png'), pygame.image.load('WR01003.png'), pygame.image.load('WR01004.png'), pygame.image.load('WR01005.png'), pygame.image.load('WR01006.png'), pygame.image.load('WR01007.png'), pygame.image.load('WR01008.png')]
combLeft = [pygame.image.load('WL01001.png'), pygame.image.load('WL01002.png'), pygame.image.load('WL01003.png'), pygame.image.load('WL01004.png'), pygame.image.load('WL01005.png'), pygame.image.load('WL01006.png'), pygame.image.load('WL01007.png'), pygame.image.load('WL01008.png')]
combR = pygame.image.load('WRstanding.png')
combL = pygame.image.load('WLstanding.png')
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
clock = pygame.time.Clock()


#<<<PLAYER CLASS>>><<<PLAYER CLASS>>><<<PLAYER CLASS>>>
#<<<PLAYER CLASS>>><<<PLAYER CLASS>>><<<PLAYER CLASS>>>

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.combLeft = False
        self.combRight = False
        self.walkCount = 0
        
# WALKING 
    def draw(self, win): 
        if self.walkCount +1  >= 24:
            self.walkCount = 0
           
        if self.left:
            win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        elif self.combLeft:
            win.blit(combLeft[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1            
        elif self.combRight:
            win.blit(combRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(char, (self.x, self.y))

#<<<PLAYER CLASS>>><<<PLAYER CLASS>>><<<PLAYER CLASS>>>
#<<<PLAYER CLASS>>><<<PLAYER CLASS>>><<<PLAYER CLASS>>>

def redrawGameWindow():
    win.blit(bg, (0,0)) # This will draw our background image at (0,0)
    soldier.draw(win)
    pygame.display.update()

# MAIN LOOP
soldier = player (453, 210, 358, 491)

run = True
while run:
    clock.tick(24)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    # NORMAL WALKING 
    if keys[pygame.K_LEFT] and soldier.x > soldier.vel:
        soldier.x -= soldier.vel
        soldier.left = True
        soldier.right = False
        soldier.combLeft = False
        soldier.combRight = False
    elif keys[pygame.K_RIGHT] and soldier.x < screenWidth - soldier.width - soldier.vel:
        soldier.x += soldier.vel
        soldier.right = True
        soldier.left = False
        soldier.combLeft = False
        soldier.combRight = False
    elif keys[pygame.K_a] and soldier.x > soldier.vel:
        soldier.x -= soldier.vel
        soldier.combLeft = True
        soldier.combRight = False
        soldier.left = False
        soldier.right = False
    elif keys[pygame.K_d] and soldier.x < screenWidth - soldier.width - soldier.vel:
        soldier.x += soldier.vel
        soldier.combRight = True
        soldier.combLeft = False
        soldier.left = False
        soldier.right = False
    else:
        soldier.right = False
        soldier.left = False
        soldier.combLeft = False
        soldier.combRight = False
        soldier.walkCount = 0
   

   



    if not (soldier.isJump):
        if keys[pygame.K_SPACE]:
            soldier.isJump = True
            soldier.right = False
            soldier.left = False
            soldier.walkCount = 0
            
    else:
        if soldier.jumpCount >= -10:
            soldier.y -= (soldier.jumpCount * abs(soldier.jumpCount)) * 0.5
            soldier.jumpCount -= 1
        else: 
            soldier.jumpCount = 10
            soldier.isJump = False

    redrawGameWindow()

pygame.quit()
        
