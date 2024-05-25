import pygame
#initialise pygame
pygame.init()
from pygame.constants import WINDOWCLOSE
from pygame.locals import QUIT

win = pygame.display.set_mode((450, 400))
pygame.display.set_caption('Pokemon Simulator')

#Images
bg = pygame.image.load('Pokemon game background.png')
walkLeft = [pygame.image.load('Character sprite LeftWalk#1.png'), pygame.image.load('Character sprite LeftWalk#2.png'), pygame.image.load('Character sprite LeftWalk#3.png')]
walkRight = [pygame.image.load('Character sprite RightWalk#1.png'), pygame.image.load('Character sprite RightWalk#2.png'), pygame.image.load('Character sprite RightWalk#3.png')]
walkUp = [pygame.image.load('Character sprite UpWalk#1.png'), pygame.image.load('Character sprite UpWalk#2.png')]
walkDown = [pygame.image.load('Character sprite DownWalk#1.png'), pygame.image.load('Character sprite DownWalk#2.png')]
char = pygame.image.load('Character sprite DownWalk#1.png')
#----------------VARIABLES----------------
#rectangle variables
x = 225
y = 200
charWidth = 40
charHeight = 40
vel = 5
charVel = 5
isJump = False
jumpCount = 10
FPS = 9
left = False
right = False
up = False
down = False
walkCount = 0
spacePress = False
clock = pygame.time.Clock()

pokeMartHeight = 94
pokeMartOffset = 112
pokeCenterHeight = 94
pokeCenterOffset = 336
treeHeight = 139
leftTreeOffset = 58
rightTreeOffset = 393

#----------------FUNCTIONS----------------
#Reset rectangle
def redrawGameWindow(): 
  global walkCount
  win.blit(bg, (0,0))

  if walkCount + 1 > 9:
    walkCount = 0

  if left:
    win.blit(walkLeft[walkCount // 3], (x,y))
    walkCount +=1

  elif right:
    win.blit(walkRight [walkCount // 3], (x,y))
    walkCount += 1

  elif up:
    if walkCount >= 6:
      walkCount = 0

    win.blit(walkUp[walkCount // 3], (x,y))
    walkCount += 1

  elif down:
    if walkCount >= 6:
      walkCount = 0
      
    win.blit(walkDown[walkCount // 3], (x,y))
    walkCount += 1

  else:
    win.blit(char, (x,y))

  pygame.display.update()

#----------------MAIN LOOP----------------
run = True
while run:
  redrawGameWindow()
  clock.tick(FPS)
  
  #QUIT
  for event in pygame.event.get():
      if event.type == QUIT:
          run = False
  #Keys input
  keys = pygame.key.get_pressed()

  if keys[pygame.K_LEFT] and x >= vel:
    left = True
    right = False
    up = False
    down = False
    if x > pokeMartOffset or y >= pokeMartHeight - vel*4:
      if x >= leftTreeOffset or y <= treeHeight - charHeight*0.9:
        x -= charVel
  
  elif keys[pygame.K_RIGHT] and x < 450 - charWidth:
    right = True
    left = False
    up = False
    down = False
    if y >= pokeCenterHeight - vel*4 or x <= pokeCenterOffset - 28:
      if x <= rightTreeOffset - (charWidth - vel*2) or y <= treeHeight - charHeight*0.9:
        x += charVel

  elif keys[pygame.K_UP] and y >= 0:
    up = True
    left = False
    right = False
    down = False
    if y >= pokeMartHeight - vel*2 or x >= pokeMartOffset - vel*2:
      if y >= pokeCenterHeight - vel*2 or x <= pokeCenterOffset - 23:
        y -= charVel

  elif keys[pygame.K_DOWN] and y < 400 - charHeight:
    up = False
    left = False
    right = False
    down = True
    if x >= leftTreeOffset - vel*2 or y <= treeHeight - charHeight:
      if x <= rightTreeOffset - vel*2 or y <= treeHeight - charHeight:
        y += charVel

  else:
    right = False
    left = False
    up = False
    down = False
    walkCount = 0
  
  if keys[pygame.K_LSHIFT] and spacePress == False:
    spacePress = True
    charVel *= 1.75
    FPS *= 1.75
  else:
    spacePress = False
    charVel = 5
    FPS = 9

 
  
