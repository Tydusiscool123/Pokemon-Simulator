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
pokecenterBG = pygame.image.load('Pokecenter3.png')
pokemartBG = pygame.image.load('Pokemart2.png')
battleBG = pygame.image.load('Battle background2.png')
textPointer = pygame.image.load('textPointer.png')
selectMenuYN = pygame.image.load('optionSelectMenu.png')
textBox = pygame.image.load('Text box normal.png')
walkLeft = [pygame.image.load('Character sprite LeftWalk#1.png'), pygame.image.load('Character sprite LeftWalk#2.png'), pygame.image.load('Character sprite LeftWalk#3.png')]
walkRight = [pygame.image.load('Character sprite RightWalk#1.png'), pygame.image.load('Character sprite RightWalk#2.png'), pygame.image.load('Character sprite RightWalk#3.png')]
walkUp = [pygame.image.load('Character sprite UpWalk#1.png'), pygame.image.load('Character sprite UpWalk#2.png')]
walkDown = [pygame.image.load('Character sprite DownWalk#1.png'), pygame.image.load('Character sprite DownWalk#2.png')]
char = pygame.image.load('Character sprite DownWalk#1.png')
Pointer2 = pygame.image.load('Pointer2.png')
battleMenu = pygame.image.load('Battle menu.png')
movesMenu = pygame.image.load('Pokemon moves.png')

#Music / sound effects
selectButtonSFX = pygame.mixer.Sound('selectButtonSFX.wav')
backgroundMusic = pygame.mixer.music.load('Pokemon route 1 music.mp3')
pygame.mixer.music.play(-1)

#----------------VARIABLES----------------
charPosX = 379
charPosY = 95
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

wildPokemonList = ["Pikachu", "Bulbasaur", "Charmander", "Squirtle"]
inPokecenter = False
firstRun = False
inPokemart = False
canMove = False
keySelectD = False
menuSelectD = False
talk = False
textCount = 0
pokemon = "Charizard"
pokecenterTextList = ["Welcome to our POKEMON CENTER!", "Would you like to heal your \nPOKEMON?", "I'll take your POKEMON \nfor a few seconds...", "Weve restored your POKEMON \nto full health", "Thank you for coming!", "" ]
pokemartTextList = ["Welcome to the PokeMart!", "would you like to buy something?", "Thank you for coming!", ""]
battletextList = ["Jeff used poop!", "Your mum is cool"]
fontSize = 10
textPosX = 29
textPosY = 326
font = pygame.font.Font('Pokemon fire red font.ttf', fontSize)
keyHoldCount = 0
selectMenuPosX = 318
selectMenuPosY = 222
selectUp = True
selectDown = False
pointerOffsetY = 20
pointerOffsetX = 15
selectYes = False
firstScreen = False
fightScreen = False
selectLeft = False
selectRight = False
keyCount = 0
keyCount2 = 0
inBattle = False

#----------------CLASSES----------------


#----------------FUNCTIONS----------------

def startUp():
  print("Welcome to the world of Pokemon!")
  print("Which pokemon would you like?")

#KEYSINPUT
def keysInputMenu():
  global menuSelectD 
  global keyCount
  global keyCount2
  global selectUp
  global selectDown
  global selectRight
  global selectLeft
  global menuSelectS

  keys = pygame.key.get_pressed()

  #PRESSING D (SELECT / A)
  if keys[pygame.K_d]:
    #No holding check
    if keyCount < 1:
      selectButtonSFX.play()
      menuSelectD = True
    if keyCount > 0:
      menuSelectD = False
    keyCount +=1

  else: 
    keyCount = 0
    menuSelectD = False
    #keyHoldCount = 0
  
  #USING ARROW KEYS
  if keys[pygame.K_UP]:
    selectUp = True
    selectDown = False
  if keys[pygame.K_DOWN]:
    selectUp = False
    selectDown = True
  if keys[pygame.K_LEFT]:
    selectLeft = True
    selectRight = False
  if keys[pygame.K_RIGHT]:
    selectLeft = False
    selectRight = True

  #PRESSING S (BACK / B)
  if keys[pygame.K_s]:
    #No holding check
    if keyCount2 < 1:
      selectButtonSFX.play()
      menuSelectS = True
    if keyCount2 > 0:
      menuSelectS = False
    keyCount2 +=1
    
  else:
    keyCount2 = 0
    menuSelectS = False

#Healing in pokecenter
def pokecenterHeal():

  for i in range(1, 10):
    print("yourmum")

#Pokemart menu be like
def pokemartMenu():
  for i in range(1, 10):
    print("yourmum")

#Selecting in a menu
def selectMenu(background, selectMenuType, menuPosX, menuPosY, P_offsetX, P_offsetY):
  global selectUp
  global selectDown
  global menuSelectD 
  global selectYes
  global talk
  global inPokecenter
  global inPokemart
  global run
  global pointerOffsetY
  global pointerOffsetX
  global text
  global textSentence
  global textPosY
  global textPosX

  #Running selectMenu
  selectMenuRun = True
  while selectMenuRun == True:

    #QUIT
    for event in pygame.event.get():
        if event.type == QUIT:
            talk = False
            inPokecenter = False
            inPokemart = False
            selectMenuRun == False
            run = False

      
    #Adding the menu / resetting code
    win.blit(selectMenuType, (menuPosX, menuPosY))
    win.blit(Pointer2, (menuPosX + P_offsetX, menuPosY + P_offsetY))
    if inBattle == False:
      win.blit(textBox, (0, 0))
      win.blit (textSentence, (textPosX, textPosY))
    pygame.display.update()
    keysInputMenu()

    if selectUp == True:
      P_offsetY = 20
    
    if selectDown == True:
      P_offsetY = 46
    
    if menuSelectD == True:
      if selectUp == True:
        selectYes = True
        selectMenuRun = False
        if inBattle == False:
          redrawGameWindow(background)
        else:
          win.blit(background, (0,0))

      if selectDown == True:
        selectYes = False
        selectMenuRun = False
        if inBattle == False:
          redrawGameWindow(background)
        else:
          win.blit(background, (0,0))

#TALKING TO PEOPLE
def talking(textList, maxTextCount, questionTextCount, background):
  global talk
  global menuSelectD
  global keySelectD
  global FPS
  global inPokecenter
  global inPokemart
  global run
  global textCount
  global text
  global textSentence

  menuFirstTime = True
  #TALKING
  while talk == True:
    
    if menuFirstTime == True:
      selectButtonSFX.play()
      win.blit(textBox, (0, 0))
      text = textList[textCount]
      textSentence = font.render(text, 1, (0, 0, 0))
      win.blit (textSentence, (textPosX, textPosY))
      pygame.display.update()
      menuFirstTime = False

    #QUIT
    for event in pygame.event.get():
        if event.type == QUIT:
            talk = False
            inPokecenter = False
            inPokemart = False
            run = False

    clock.tick(FPS)

    #Graphics n stuff

    keysInputMenu()

    #opening option menu
    if textCount == questionTextCount:
      selectMenu(background, selectMenuYN, selectMenuPosX, selectMenuPosY, pointerOffsetX, pointerOffsetY)
      win.blit(textBox, (0, 0))
      text = textList[textCount]
      textSentence = font.render(text, 1, (0, 0, 0))
      win.blit (textSentence, (textPosX, textPosY))
      pygame.display.update()

      if selectYes == False:
        win.blit(textBox, (0, 0))
        text = textList[maxTextCount - 1]
        textSentence = font.render(text, 1, (0, 0, 0))
        win.blit (textSentence, (textPosX, textPosY))
        pygame.display.update()
        pygame.time.delay(500)
        talk = False

      if selectYes == True and inPokecenter == True:
        pokecenterHeal()
      if selectYes == True and inPokemart == True:
        pokemartMenu()
        

    #continuing text
    if menuSelectD == True:
      textCount += 1    
      win.blit(textBox, (0, 0))
      text = textList[textCount]
      textSentence = font.render(text, 1, (0, 0, 0))
      win.blit (textSentence, (textPosX, textPosY))
      pygame.display.update()
  
    if textCount >= maxTextCount: 
      talk = False
      menuSelectD = False
      keySelectD = False
    
#PRINTING TEXT
def printText(textList, textCount, colourNumber1, colourNumber2, colourNumber3, textPosX, textPosY):
  global textSentence
  text = textList[textCount]
  textSentence = font.render(text, 1, (colourNumber1, colourNumber2, colourNumber3))
  win.blit (textSentence, (textPosX, textPosY))
  pygame.display.update()

#Battling menus
def battleMenuLoad():
  global menuSelectD 
  global keyHoldCount
  global selectUp
  global selectDown
  global firstScreen
  global selectLeft
  global selectRight 
  global fightScreen
  global battlePartyScreen
  global runAway
  global bagScreen 
  global inBattle
  global menuSelectS
  global fightScreen
  global selectMenuType
  global menuPosX
  global menuPosY
  global P_offsetX
  global P_offsetY

  if firstScreen == True:
    selectMenuType = battleMenu
    menuPosX = 230
    menuPosY = 261
    P_offsetX = 13
    P_offsetY = 23

    #Moving pointer
    if selectUp == True:
      P_offsetY = 23
    if selectDown == True:
      P_offsetY = 51
    if selectLeft == True:
      P_offsetX = 13
    if selectRight == True:
      P_offsetX = 117
    
    if menuSelectD == True:
      firstScreen = False
      #Selecting FIGHT
      if P_offsetX == 13 and P_offsetY == 23:
        fightScreen = True
        battlePartyScreen = False
        bagScreen = False

      #Selecting POKEMON
      if P_offsetX == 13 and P_offsetY == 51:
        battlePartyScreen = True
        fightScreen = False
        bagScreen = False

      #Selecting BAG
      if P_offsetX == 117 and P_offsetY == 23:
        bagScreen = True
        fightScreen = False
        battlePartyScreen = False

      #Selecting RUN
      if P_offsetX == 117 and P_offsetY == 51:
        runAway = True
        fightScreen = False
        inBattle = False

  #FIGHTING
  if fightScreen == True:
    selectMenuType = movesMenu
    menuPosX = 0
    menuPosY = 261
    P_offsetX = 13
    P_offsetY = 23

    #Moving pointer
    if selectUp == True:
      P_offsetY = 23
    if selectDown == True:
      P_offsetY = 51
    if selectLeft == True:
      P_offsetX = 13
    if selectRight == True:
      P_offsetX = 150
    
    #selecting a move
    if menuSelectD == True:
      firstScreen = False
      fightScreen = False
      #fight method
    #Going back
    if menuSelectS == True:
      selectMenuType = battleMenu
      menuPosX = 230
      menuPosY = 261
      P_offsetX = 13
      P_offsetY = 23
      win.blit(battleBG, (0,0))
      pygame.display.update()
      fightScreen = False
      firstScreen = True
  
  
        
  win.blit(selectMenuType, (menuPosX, menuPosY))
  win.blit(Pointer2, (menuPosX + P_offsetX, menuPosY + P_offsetY))
  pygame.display.update()
  keysInputMenu()

#WILD BATTLE
def wildBattle():
  global inBattle 
  global talk
  global menuSelectD
  global keySelectD
  global FPS
  global inPokecenter
  global inPokemart
  global run
  global textCount
  global text
  global textSentence
  global firstScreen
  global trainerPokemon

  win.blit(battleBG, (0,0))
  pygame.display.update()

  testCount = 0
  pokemonRandNum = random.randint(0, 3)
  wildPokemon = wildPokemonList[pokemonRandNum]

  while inBattle == True:

    if testCount < 1:
      firstScreen = True
    
    testCount += 1
    #QUIT
    for event in pygame.event.get():
        if event.type == QUIT:
            talk = False
            inPokecenter = False
            inPokemart = False
            run = False
            inBattle = False
    
    #text = BattleextList[textCount]
    #textSentence = font.render(text, 1, (0, 0, 0))
    #win.blit(battleBG, (0,0))
    printText(battletextList, 0, 255,255, 255, 20, 278)
    clock.tick(FPS)
    #selectMenu(battleBG, battleMenu, 230, 261, 243, 284)
    battleMenuLoad()
  
#MAP / SPRITE REDRAW
def redrawGameWindow(background): 
  global walkCount
  global charPosX
  global charPosY
  global lastPos

  win.blit(background, (0,0))

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

#POKECENTER
def pokecenterRun():
  global walkUp
  global backgroundMusic
  global inPokecenter
  global charPosX
  global charPosY
  global run
  global left
  global right
  global up
  global down
  global charMoving
  global lastPos
  global charStep
  global walkCount
  global charVel 
  global spacePress
  global FPS
  global firstRun
  global canMove
  global vel
  global talk
  global keySelectD
  global menuSelectD
  global textCount
  win.blit(walkUp[0], (charPosX,charPosY))
  pygame.display.update()

  backgroundMusic = pygame.mixer.music.load('Pokecenter music.mp3')
  pygame.mixer.music.play(-1)
  firstRun = True

  #RUNNING POKEMON CENTER
  while inPokecenter == True:
    #Placing char in initial position
    if firstRun == True:
      charPosX = (charWidth/2) + 201
      charPosY = 301
      up = True
      left = False
      right = False
      down = False
      lastPos = "up"
      charMoving = False
      firstRun = False
    
    redrawGameWindow(pokecenterBG)
    characterWalking()
    clock.tick(FPS)

    #QUIT
    for event in pygame.event.get():
        if event.type == QUIT:
            inPokecenter = False
            run = False
    
    #Boundaries / Moving
    #MOVING LEFT
    if left == True and charMoving == True:
      #front desk
      if (charPosX >= 326 + charVel or charPosX <= 97) or charPosY >= 155:
        #Right table / cushion left
        if (charPosX >= 386 + charVel or charPosX <= 307) or (charPosY >= 281 or charPosY <= 176):
          #PC
          if (charPosX >= 360 + charVel) or charPosY >= 116:
            #left wall top
            if charPosX >= 10 + charVel or charPosY >= 114 + charVel:
              #Bottom left corner
              if charPosX >= 20 + charVel or (charPosY <= 266):
                charPosX -= charVel
    
    #MOVING RIGHT
    if right == True and charMoving == True:
      #front desk right
      if (charPosX <= 95 - charVel or charPosX >= 325) or charPosY >= 161:
        #I have no idea
        if charPosX <= 387 or charPosY <= 204:
          #Table right
          if (charPosX <= 307 - charVel or charPosX >= 386) or (charPosY >= 281 or charPosY <= 176):
            #right wall
            if charPosX <= 397 - charVel or charPosY >= 115:
              charPosX += charVel
    
    #MOVING UP
    if up == True and charMoving == True and (charPosY >= 100 + charVel):
      #Front desk up
      if (charPosX <= 97 or charPosX >= 325) or charPosY >= 161 + charVel:
        #Table up
        if (charPosX <= 307 or charPosX >= 386) or (charPosY >= 281 + charVel or charPosY <= 176):
          #PC
          if (charPosX <= 325 or charPosX >= 360) or charPosY >= 116 + charVel:
            #left side of the wall
            if charPosX >= 97 or charPosY >= 114 + charVel:
              #right side of wall
              if charPosX <= 397 or charPosY >= 115 + charVel:
                charPosY -= charVel
    
    #MOVING DOWN
    if down == True and charMoving == True:
      #Barrier at bottom
      if charPosY <= 290 - charVel or (charPosX >= 199 and charPosX <= 221) :
        #far right cushion
        if charPosX <=392 or charPosY <= 202 - charVel:
          #table / cushion down
          if (charPosX >= 386 or charPosX <= 307) or charPosY <= 176 - charVel:
            #Bottom left corner
            if charPosX >= 20 or (charPosY <= 266 - charVel):
              charPosY += charVel
    
    #print("charPosX: " + str(charPosX))
    #print("charPosY: " + str(charPosY))
              
    #Resetting talking
    if (textCount > 0):
      keySelectD = False
      menuSelectD = False
      textCount = 0

    #talking to Nurse joy 
    if keySelectD == True and (charPosX >= 203 and charPosX <= 220 and charPosY <= 161):
      talk = True
      talking(pokecenterTextList, 5, 1, pokecenterBG)
      keySelectD = False

    #walking out of pokecenter
    if (charPosX >= 199 and charPosX <= 221) and charPosY >= 302:
      inPokecenter = False
      backgroundMusic = pygame.mixer.music.load('Pokemon route 1 music.mp3')
      pygame.mixer.music.play(-1)
      charPosY = 77
      charPosX = 379
      up = False
      left = False
      right = False
      down = True
      lastPos = "down"
      charMoving = False

#POKEMART
def pokemartRun():
  global walkUp
  global backgroundMusic
  global inPokemart
  global charPosX
  global charPosY
  global run
  global left
  global right
  global up
  global down
  global charMoving
  global lastPos
  global charStep
  global walkCount
  global charVel 
  global spacePress
  global FPS
  global firstRun
  global talk
  global menuSelectD
  global keySelectD
  global textCount
  win.blit(walkUp[0], (charPosX,charPosY))
  pygame.display.update()

  backgroundMusic = pygame.mixer.music.load('Pokecenter music.mp3')
  pygame.mixer.music.play(-1)
  firstRun = True

  #RUNNING POKEMART
  while inPokemart == True:
    #Placing char in initial position
    if firstRun == True:
      charPosX = 178
      charPosY = 304
      up = True
      left = False
      right = False
      down = False
      lastPos = "up"
      charMoving = False
      firstRun = False
    
    redrawGameWindow(pokemartBG)
    characterWalking()
    clock.tick(FPS)

    #QUIT
    for event in pygame.event.get():
        if event.type == QUIT:
            inPokemart = False
            run = False

    #MOVING LEFT
    if left == True and charMoving == True and charPosX >= 46 + charVel:
      #Bottom left cabinet
      if (charPosX <= 53 or charPosX >= 141 + charVel) or (charPosY >= 277 or charPosY <= 227):
        #Front desk
        if charPosX >= 174 + charVel or (charPosY >= 214):
          #Bottom left stall
          if (charPosX <= 250 or charPosX >= 338 + charVel) or (charPosY <= 158 or charPosY >= 278):
            #Bottom left corner
            if charPosX >= 71 + charVel or charPosY <= 285:
              charPosX -= charVel
    
    #MOVING RIGHT
    if right == True and charMoving == True and charPosX <= 376 - charVel:
      #Bottom left cabinet
      if (charPosX <= 53 - charVel or charPosX >= 141) or (charPosY >= 277 or charPosY <= 227):
        #Top right stall
        if charPosX <= 249 - charVel or charPosY >= 132:
          #Bottom left stall
          if (charPosX <= 250 - charVel or charPosX >= 338) or (charPosY <= 158 or charPosY >= 278):
            #Bottom right stall
            if charPosX <= 350 - charVel or (charPosY <= 154):
              charPosX += charVel
    
    #MOVING UP
    if up == True and charMoving == True and charPosY >= 114 + charVel:
      #Bottom left cabinet
      if (charPosX <= 53 or charPosX >= 141) or (charPosY >= 277 + charVel or charPosY <= 227):
        #front Desk
        if charPosX >= 174 or charPosY >= 214 + charVel:
          #Top right stall
          if charPosX <= 249 or charPosY >= 132 + charVel:
            #Bottom left stall
            if (charPosX <= 250 or charPosX >= 338) or (charPosY >= 278 + charVel or charPosY <= 158):
              #Bottom right stall
              if charPosX <= 350 or (charPosY >= 278 + charVel or charPosY <= 154):
                charPosY -= charVel
    
    #MOVING DOWN
    if down == True and charMoving == True and ((charPosX >= 165 and charPosX <= 192) or charPosY <= 298 - charVel):
      #Bottom left cabinet
      if (charPosX <= 53 or charPosX >= 141) or (charPosY >= 277 or charPosY <= 227 - charVel):
        #Bottom left stall
        if (charPosX <= 250 or charPosX >= 338) or (charPosY >= 278 or charPosY <= 158 - charVel):
          #Bottom right stall
          if charPosX <= 350 or (charPosY >= 278 or charPosY <= 154 - charVel):
            #Bottom left corner
            if charPosX >= 71 or charPosY <= 280:
              charPosY += charVel
    
    
    print("charPosX: " + str(charPosX))
    print("charPosY: " + str(charPosY))
    
    #Resetting talking
    if (textCount > 0):
      keySelectD = False
      menuSelectD = False
      textCount = 0

    #talking to pokemart guy
    if keySelectD == True and (charPosX <= 180 and (charPosY >= 148 and charPosY <= 175)):
      talk = True
      talking(pokemartTextList, 3, 1, pokemartBG)
      keySelectD = False
    
    #EXITING POKEMART
    if (charPosX >= 165 and charPosX <= 192) and charPosY >= 306:
      inPokemart = False
      backgroundMusic = pygame.mixer.music.load('Pokemon route 1 music.mp3')
      pygame.mixer.music.play(-1)
      charPosY = 77
      charPosX = 62
      up = False
      left = False
      right = False
      down = True
      lastPos = "down"
      charMoving = False

#WALKING MECHANISM
def characterWalking():
  #Keys input
  keys = pygame.key.get_pressed()
  global left
  global right
  global up
  global down
  global charMoving
  global lastPos
  global charStep
  global charPosX
  global charPosY
  global walkCount
  global charVel 
  global spacePress
  global FPS
  global inPokecenter
  global keySelectD
  global menuSelectD
  charStep = False

  if keys[pygame.K_d]:
    keySelectD = True
  else:
    keySelectD = False
    menuSelectD = False
  
  #MOVING KEYS
  #Moving left
  if keys[pygame.K_LEFT]:
    left = True
    right = False
    up = False
    down = False
    lastPos = "left"
    charMoving = False
    if charPosX >= charVel:
      charMoving = True
  
  #Moving right
  elif keys[pygame.K_RIGHT]:
    right = True
    left = False
    up = False
    down = False
    lastPos = "right"
    charMoving = False
    if charPosX <= 422 - charVel:
      charMoving = True

  #Moving up
  elif keys[pygame.K_UP]:
    up = True
    left = False
    right = False
    down = False
    lastPos = "up"
    charMoving = False
    if charPosY >= 0:
      charMoving = True

  #Moving down
  elif keys[pygame.K_DOWN]:
    down = True 
    lastPos = "down"
    up = False
    left = False
    right = False
    charMoving = False
    if charPosY < 400 - charHeight:
      charMoving = True
    
  
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
    charVel *= 2
    FPS *= 2
  else:
    spacePress = False
    charVel = 5
    FPS = 9
  #print (spacePress)


#------------------------------------------------MAIN LOOP------------------------------------------------
run = True
while run:
  redrawGameWindow(bg)
  characterWalking()
  clock.tick(FPS)

  #QUIT
  for event in pygame.event.get():
      if event.type == QUIT:
          run = False
  
  #Moving left
  if left == True and charMoving == True:
    if charPosX > pokeMartOffset or charPosY >= pokeMartHeight - vel*4:
      if charPosX >= leftTreeOffset or charPosY <= treeHeight - charHeight*0.9:
        charPosX -= charVel
        charStep = True
  #Moving right
  if right == True and charMoving == True:
    if charPosY >= pokeCenterHeight - vel*4 or charPosX <= pokeCenterOffset - 28:
      if charPosX <= rightTreeOffset - charWidth or charPosY <= treeHeight - charHeight*0.9:
        charPosX += charVel
        charStep = True
  #Moving up
  if up == True and charMoving == True:
    if charPosY >= pokeMartHeight - vel*2 or charPosX >= pokeMartOffset - vel*2:
      if charPosY >= pokeCenterHeight - vel*2 or charPosX <= pokeCenterOffset - 23:
        charPosY -= charVel
        charStep = True
  #Moving down
  if down == True and charMoving == True:
    if charPosX >= leftTreeOffset - vel*2 or charPosY <= treeHeight - charHeight:
      if charPosX <= rightTreeOffset - vel*2 or charPosY <= treeHeight - charHeight:
        charPosY += charVel
        charStep = True

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
          print(str(encounterRate))
        if encounterRate < 12:
          encounter = True
        else:
          encounter = False  

  #ENCOUNTER POKEMON
  if encounter == True:
    win.fill((0, 0, 0))
    pygame.display.update()
    backgroundMusic = pygame.mixer.music.load('Battle music.mp3')
    pygame.mixer.music.play(-1)
    pygame.time.delay(1000)
    inBattle = True
    wildBattle()
    encounter = False
    encounterRate = 100
    backgroundMusic = pygame.mixer.music.load('Pokemon route 1 music.mp3')
    pygame.mixer.music.play(-1)
  
  #ENTERING POKEMART
  if (charPosY >= 74 and charPosY <= 84) and (charPosX >= 60 and charPosX <= 66):
    if (up == True and charStep == False and lastPos == "up"):
      inPokemart = True
      pokemartRun()
  
  #ENTERING POKECENTER
  if (charPosY <= 84 and charPosY >= 74) and (charPosX >= 375 and charPosX <= 380):
    if (up == True and charStep == False and lastPos == "up"):
      inPokecenter = True
      print( str(inPokecenter))
      pokecenterRun()

  #Show Char position
  #print("CharPosY:" + str(charPosY))
  #print("CharPosX:" + str(charPosX))
  #print

pygame.quit()