import pygame
import random
import subprocess
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

#Music / sound effects
routeMusic = pygame.mixer.music.load('Pokemon route 1 music.mp3')
pygame.mixer.music.play(-1)

#----------------VARIABLES----------------
charPosX = 225
charPosY = 200
charWidth = 28
charHeight = 40
charMoving = False
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
lastPos = "down"
clock = pygame.time.Clock()

pokeMartHeight = 94
pokeMartOffset = 112
pokeCenterHeight = 94
pokeCenterOffset = 336
treeHeight = 139
leftTreeOffset = 58
rightTreeOffset = 393

#grass positions
leftGrassX = 58
grassPosY = 140
grassWidth = 72
grassHeight = 260
rightGrassX = 322
inGrass = False
testGrassWalkCount = 0
grassWalkCount = 0

encounter = False
encounterRate = 100
charStep = False

#----------------FUNCTIONS----------------
#Reset rectangle
def redrawGameWindow(): 
  global walkCount
  win.blit(bg, (0,0))

  if walkCount + 1 > 9:
    walkCount = 0

  if left:
    win.blit(walkLeft[walkCount // 3], (charPosX,charPosY))
    #if walkCount % 3 == 0:
      #print("walkCount2: " + str(walkCount // 3))
    walkCount +=1

  elif right:
    win.blit(walkRight [walkCount // 3], (charPosX,charPosY))
    #if walkCount % 3 == 0:
      #print("walkCount2: " + str(walkCount // 3))
    walkCount += 1

  elif up:
    if walkCount >= 6:
      walkCount = 0

    win.blit(walkUp[walkCount // 3], (charPosX,charPosY))
    #if walkCount % 3 == 0:
      #print("walkCount2: " + str(walkCount // 3))
    walkCount += 1

  elif down:
    if walkCount >= 6:
      walkCount = 0
      
    win.blit(walkDown[walkCount // 3], (charPosX,charPosY))
    #if walkCount % 3 == 0:
      #print("walkCount2: " + str(walkCount // 3))
    walkCount += 1


  else:
    if lastPos == "up":
      win.blit(walkUp[0], (charPosX,charPosY))
      walkCount += 3
    if lastPos == "down":
      win.blit(walkDown[0], (charPosX,charPosY))
      walkCount += 3
    if lastPos == "left":
      win.blit(walkLeft[0], (charPosX,charPosY))
      walkCount += 3
    if lastPos == "right":
      win.blit(walkRight[0], (charPosX,charPosY))
      walkCount += 3

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

  #Moving left
  if keys[pygame.K_LEFT] and charPosX >= vel:
    left = True
    right = False
    up = False
    down = False
    lastPos = "left"
    charMoving = True
    if charPosX > pokeMartOffset or charPosY >= pokeMartHeight - vel*4:
      if charPosX >= leftTreeOffset or charPosY <= treeHeight - charHeight*0.9:
        charPosX -= charVel
        charStep = True
  
  #Moving right
  elif keys[pygame.K_RIGHT] and charPosX <= 450 - 30:
    right = True
    left = False
    up = False
    down = False
    lastPos = "right"
    charMoving = True
    if charPosY >= pokeCenterHeight - vel*4 or charPosX <= pokeCenterOffset - 28:
      if charPosX <= rightTreeOffset - charWidth or charPosY <= treeHeight - charHeight*0.9:
        charPosX += charVel
        charStep = True

  #Moving up
  elif keys[pygame.K_UP] and charPosY >= 0:
    up = True
    left = False
    right = False
    down = False
    lastPos = "up"
    charMoving = True
    if charPosY >= pokeMartHeight - vel*2 or charPosX >= pokeMartOffset - vel*2:
      if charPosY >= pokeCenterHeight - vel*2 or charPosX <= pokeCenterOffset - 23:
        charPosY -= charVel
        charStep = True

  #Moving down
  elif keys[pygame.K_DOWN] and charPosY < 400 - charHeight:
    up = False
    left = False
    right = False
    down = True
    lastPos = "down"
    charMoving = True
    if charPosX >= leftTreeOffset - vel*2 or charPosY <= treeHeight - charHeight:
      if charPosX <= rightTreeOffset - vel*2 or charPosY <= treeHeight - charHeight:
        charPosY += charVel
        charStep = True
        

  elif keys [pygame.K_b]:
    routeMusic = pygame.mixer.music.load('Battle music.mp3')
    pygame.mixer.music.play(-1)
  elif keys [pygame.K_a]:
    routeMusic = pygame.mixer.music.load('Pokemon route 1 music.mp3')
    pygame.mixer.music.play(-1)
  
  #Character doing nothing
  else:
    right = False
    left = False
    up = False
    down = False
    walkCount = 0
    charMoving = False
    #getting last position so that char stays in same positon and doesn't move back
    if lastPos == "up":
      win.blit(walkUp[0], (charPosX,charPosY))
    if lastPos == "down":
      win.blit(walkDown[0], (charPosX,charPosY))
    if lastPos == "left":
      win.blit(walkLeft[0], (charPosX,charPosY))
    if lastPos == "right":
      win.blit(walkRight[0], (charPosX,charPosY))
      
  #Holding space = running
  if keys[pygame.K_SPACE] and spacePress == False:
    spacePress = True
    charVel *= 1.75
    FPS *= 1.75
  else:
    spacePress = False
    charVel = 5
    FPS = 9

  #IN GRASS OPERATIONS:
  if (charPosX >= leftGrassX - 5 and charPosX <= ((leftGrassX + grassWidth) - (charWidth/2))) and (charPosY >= grassPosY - (charHeight*0.75)):
    inGrass = True
  elif ((charPosX >= rightGrassX - (charWidth*0.75)) and charPosX <= ((rightGrassX + grassWidth) - (charWidth/2))) and (charPosY >= grassPosY - (charHeight*0.75)):
    inGrass = True
  else:
    inGrass = False
  
  if inGrass == True and charMoving == True:
      grassWalkCount +=1
      if charStep == True:
        if walkCount % 3 == 0:
          #print("walkCount3: " + str(walkCount // 3))
          encounterRate = random.randint(1, 100)
        if encounterRate < 10:
          encounter = True
        else:
          encounter = False  
  #Terminal output
  print("encounter: " + str(encounterRate)) 

  #ENCOUNTER POKEMON
  if encounter == True:
    win.fill((0, 0, 0))
    pygame.display.update()
    routeMusic = pygame.mixer.music.load('Battle music.mp3')
    pygame.mixer.music.play(-1)
    pygame.time.delay(1000)
    encounter = False
    encounterRate = 100
    routeMusic = pygame.mixer.music.load('Pokemon route 1 music.mp3')
    pygame.mixer.music.play(-1)
  #print("grassWalk: " + str(grassWalkCount))
  
  


  






 
  
