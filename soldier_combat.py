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
        self.walkCount = 0
        self.standing = True
        
    def draw(self, win): 
        if self.walkCount +1  >= 24:
            self.walkCount = 0

        if not(self.standing):  
            if self.left:
                win.blit(combLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(combRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(combR, (self.x-100, self.y))
            elif self.left:
                win.blit(combL, (self.x, self.y))
            else:
                win.blit(char, (self.x, self.y))

# PROJECTILES
class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 30 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)
   

def redrawGameWindow():
    win.blit(bg, (0,0)) # This will draw our background image at (0,0)
    soldier.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

# MAIN LOOP
soldier = player (453, 210, 358, 491)
bullets = []
run = True
while run:
    clock.tick(24)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < screenWidth and bullet.x > 0:
            bullet.x += bullet.vel 
        else:
            bullets.pop(bullets.index(bullet)) #REMOVE BULLETS AT THE END OF SCREEN
    

    keys = pygame.key.get_pressed()
    
   
    # NORMAL WALKING 
    if keys[pygame.K_LEFT] and soldier.x > soldier.vel:
        soldier.x -= soldier.vel
        soldier.left = True
        soldier.right = False
        soldier.standing = False                
    elif keys[pygame.K_RIGHT] and soldier.x < screenWidth - soldier.width - soldier.vel:
        soldier.x += soldier.vel
        soldier.right = True
        soldier.left = False
        soldier.standing = False                   
    else:
        soldier.standing = True                  
        soldier.walkCount = 0
        
        # BULLET FIRING 
        if keys[pygame.K_SPACE]:
            if soldier.left:
                facing = -1
                if len(bullets) < 10:
                    bullets.append(projectile(round(soldier.x + soldier.width//2 -190), round(soldier.y + soldier.height//2 +55), 6, (255,255,255), facing)) 
            else:
                facing = 1
                if len(bullets) < 10:
                    bullets.append(projectile(round(soldier.x + soldier.width//2 +290), round(soldier.y + soldier.height//2 +50), 6, (255,255,255), facing)) 
   

    if not (soldier.isJump):
        if keys[pygame.K_UP]:
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
        
