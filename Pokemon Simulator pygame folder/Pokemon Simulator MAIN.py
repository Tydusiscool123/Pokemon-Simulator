import pygame
import random
import math
import copy
import subprocess
#initialise pygame
pygame.init()
from pygame.constants import WINDOWCLOSE
from pygame.locals import QUIT

win = pygame.display.set_mode((450, 400))
pygame.display.set_caption('Pokemon Simulator')

#Images
openingScreen = pygame.image.load('openingScreen.png')
bg = pygame.image.load('Pokemon game background.png')
pokecenterBG = pygame.image.load('Pokecenter4.png')
pokemartBG = pygame.image.load('Pokemart3.png')
pokemartMenu = pygame.image.load('pokemartMenu2.png')
martSubMenu = pygame.image.load('martSubMenu.png')
battleBG = pygame.image.load('Battle background4.png')
bagBG = pygame.image.load('bagBG2.png')
pokemonMenu = pygame.image.load('pokemonMenu.png')
textPointer = pygame.image.load('textPointer.png')
selectMenuYN = pygame.image.load('optionSelectMenu.png')
pokeSubMenu2 = pygame.image.load('pokeSubMenu2.png')
pokeSubMenu1 = pygame.image.load('pokeSubMenu1.png')
textBox = pygame.image.load('Text box normal.png')
walkLeft = [pygame.image.load('Character sprite LeftWalk#1.png'), pygame.image.load('Character sprite LeftWalk#2.png'), pygame.image.load('Character sprite LeftWalk#3.png')]
walkRight = [pygame.image.load('Character sprite RightWalk#1.png'), pygame.image.load('Character sprite RightWalk#2.png'), pygame.image.load('Character sprite RightWalk#3.png')]
walkUp = [pygame.image.load('Character sprite UpWalk#1.png'), pygame.image.load('Character sprite UpWalk#2.png')]
walkDown = [pygame.image.load('Character sprite DownWalk#1.png'), pygame.image.load('Character sprite DownWalk#2.png')]
char = pygame.image.load('Character sprite DownWalk#1.png')
Pointer2 = pygame.image.load('Pointer2.png')
battleMenu = pygame.image.load('Battle menu.png')
movesMenu = pygame.image.load('Pokemon moves.png')
controlsMenu = pygame.image.load('controls.png')
rulesMenu = pygame.image.load('rules.png')
tipsMenu = pygame.image.load('Tips.png')
pokedexGraphic = pygame.image.load('Pokedex completed2.png')


#STARTER SPRITES
bulbasaurSprite1 = pygame.image.load('bulbasaur1.png')
bulbasaurSprite2 = pygame.image.load('bulbasaur2.png')
charmanderSprite1 = pygame.image.load('charmander1.png')
charmanderSprite2 = pygame.image.load('charmander2.png')
squirtleSprite1 = pygame.image.load('squirtle1.png')
squirtleSprite2 = pygame.image.load('squirtle2.png')
pikachuSprite1 = pygame.image.load('pikachu1.png')
pikachuSprite2 = pygame.image.load('pikachu2.png')

#SPRITE LISTS
spriteList1 = [bulbasaurSprite1, bulbasaurSprite2]
spriteList4 = [charmanderSprite1, charmanderSprite2]
spriteList7 = [squirtleSprite1, squirtleSprite2]
spriteList25 = [pikachuSprite1, pikachuSprite2]


#Music / sound effects
selectButtonSFX = pygame.mixer.Sound('selectButtonSFX.wav')
runawaySFX = pygame.mixer.Sound('runaway2.wav')
healingSFX = pygame.mixer.Sound('SFX_HEAL_UP.wav')
levelUpSFX = pygame.mixer.Sound('levelUp.wav')

#----------------VARIABLES----------------
charPosX = 40
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


inPokecenter = False
firstRun = False
inPokemart = False
canMove = False
keySelectD = False
keySelectW = False
menuSelectD = False
menuSelectS = False
talk = False
textCount = 0

fontSize = 10
textPosX = 29
textPosY = 326

font = pygame.font.Font('Pokemon fire red font.ttf', fontSize)
fontSize2 = 8
font2 = pygame.font.Font('Pokemon fire red font.ttf', fontSize2)
fontSize3 = 7
font3 = pygame.font.Font('Pokemon fire red font.ttf', fontSize3)

keyHoldCount = 0
selectMenuPosX = 318
selectMenuPosY = 222
selectUp = True
selectDown = False
pointerOffsetY = 20
pointerOffsetX = 15
selectYes = False
firstScreen = False
pokeScreen = False
moveScreen = False
selectLeft = False
selectRight = False
keyCount = 0
keyCount2 = 0
inBattle = False
bagScreen = False
battlePartyScreen = False
firstCount = 0

P_offsetX1 = 13
P_offsetX2 = 117
P_offsetY1 = 23
P_offsetY2 = 51

selectedMove = False
NVEffective = False
SEffective = False
effective = False

damageRatio = 0
lastBarLength = 0
enemyLastBarLength = 0
HPAnimation = False

maxMovePP = 0
movePP = 0
moveIndex = 0

specialMove = False
attackDown = False
paralysis = False
userSleep = False
enemySleep = False
attackStatStage = False

ballType = "Poke Ball"
pokeNum = 1

boxList = []
ballIndex = 0
index = 0
ballList = ["Poke Ball"]
ballAmountList = [5]
martList = ["Poke Ball", "Great Ball", "Ultra Ball", "Master Ball", "Lucky Egg", "Amulet Coin"]
martPriceList = [200, 600, 1200, 69420, 5000, 5000]

levelAdd = 1

money = 1000

battleTextX = 24
battleTextY = 274
battleTextY2 = 304

ruleScreen = False
pokedexList = []
completedPokedex = False
rulesCount = 0
continueTurn = False
coinMultiplier = 1

struggle = False


#------------------------------------------------CLASSES------------------------------------------------
class pokemon(object):
  def __init__(self, name, type, type2, moves, movePowerList, movePPList, movePPListMAX, attack, defense, health, speed, level, speciesRate):
    self.name = name
    self.type = type
    self.type2 = type2
    self.moves = moves
    self.movePowerList = movePowerList
    self.attack = attack
    self.defense = defense
    self.health = health
    self.level = level
    self.speed = speed
    self.speciesRate = speciesRate

    #self.moveType = moveType
    self.HPIV = random.randint(0, 31)
    self.attackIV = random.randint(0, 31)
    self.defenseIV = random.randint(0, 31)
    self.speedIV = random.randint(0, 31)
    
    
    print(self.name)
    print("self.HPIV: " + str(self.HPIV))
    print("self.attackIV: " + str(self.attackIV))
    print("self.defenseIV: " + str(self.defenseIV))
    print("self.speedIV: " + str(self.speedIV))

    self.HPEV = 0
    self.attackEV = 0
    self.defenseEV = 0
    self.speedEV = 0

    #STATS
    #Max stats
    self.maxHP = math.floor(0.01 * (2 * health + self.HPIV + math.floor(0.25 * self.HPEV)) * level) + level + 10
    self.maxAttackStats = (math.floor(0.01 * (2 * attack + self.attackIV + math.floor(0.25 * self.attackEV)) * level) + 5)
    self.maxDefenseStats = (math.floor(0.01 * (2 * defense + self.defenseIV + math.floor(0.25 * self.defenseEV)) * level) + 5)
    self.maxSpeedStats = (math.floor(0.01 * (2 * speed + self.speedIV + math.floor(0.25 * self.speedEV)) * level) + 5)

    #Actual stats
    self.HP = math.floor(0.01 * (2 * health + self.HPIV + math.floor(0.25 * self.HPEV)) * level) + level + 10
    self.attackStats = (math.floor(0.01 * (2 * attack + self.attackIV + math.floor(0.25 * self.attackEV)) * level) + 5)
    self.defenseStats = (math.floor(0.01 * (2 * defense + self.defenseIV + math.floor(0.25 * self.defenseEV)) * level) + 5)
    self.speedStats = (math.floor(0.01 * (2 * speed + self.speedIV + math.floor(0.25 * self.speedEV)) * level) + 5)
    
    self.maxPPList = movePPListMAX
    self.movePPList = movePPList

    pokeNameList = ["Bulbasaur", "Charmander", "Squirtle", "Pikachu"]
    pokeSpriteList = [spriteList1, spriteList4, spriteList7, spriteList25]
    for i, k in enumerate(pokeNameList):
      if self.name == k:
        self.spriteList = pokeSpriteList[i]


  #--------------------METHODS--------------------
  #--------RECHECKING STATS--------
  def statsCheck(self):
      print(self.name)
      print("HP: " + str(self.maxHP))
      print("Atack: " + str(self.maxAttackStats))
      print("Defense: " + str(self.maxDefenseStats))
      print("Speed: " + str(self.maxSpeedStats))
      #Max stats
      self.maxHP = math.floor(0.01 * (2 * self.health + self.HPIV + math.floor(0.25 * self.HPEV)) * self.level) + self.level + 10
      self.maxAttackStats = (math.floor(0.01 * (2 * self.attack + self.attackIV + math.floor(0.25 * self.attackEV)) * self.level) + 5)
      self.maxDefenseStats = (math.floor(0.01 * (2 * self.defense + self.defenseIV + math.floor(0.25 * self.defenseEV)) * self.level) + 5)
      self.maxSpeedStats = (math.floor(0.01 * (2 * self.speed + self.speedIV + math.floor(0.25 * self.speedEV)) * self.level) + 5)

      self.attackStats = (math.floor(0.01 * (2 * self.attack + self.attackIV + math.floor(0.25 * self.attackEV)) * self.level) + 5)
      self.defenseStats = (math.floor(0.01 * (2 * self.defense + self.defenseIV + math.floor(0.25 * self.defenseEV)) * self.level) + 5)
      self.speedStats = (math.floor(0.01 * (2 * self.speed + self.speedIV + math.floor(0.25 * self.speedEV)) * self.level) + 5)
      
      print(self.name)
      print("maxHP: " + str(self.maxHP))
      print("maxAtack: " + str(self.maxAttackStats))
      print("maxDefense: " + str(self.maxDefenseStats))
      print("maxSpeed: " + str(self.maxSpeedStats))
  
  #--------REPRINT BACKGROUND--------
  def printBattleBG(self, Pokemon2):
    global moveScreen
    global maxMovePP
    global movePP
  
    #Background
    win.blit(battleBG, (0,0))

    #POKEMON SPRITES
    pokeNameList = ["Bulbasaur", "Charmander", "Squirtle", "Pikachu"]
    #trainerSpriteList = [StarterSprite1, StarterSprite3, StarterSprite5, StarterSprite7]
    trainerSpritePosList = [(63, 181), (75, 163), (54, 175), (61, 160)]
    #enemySpriteList = [StarterSprite2, StarterSprite4, StarterSprite6, StarterSprite8]
    enemySpritePosList = [(291,95), (298, 96), (280, 95), (303, 85)]

    trainerSprite = self.spriteList[0]
    enemySprite = Pokemon2.spriteList[1]
    #Choosing which sprite's which
    for i,k in enumerate(pokeNameList):
      #Trainer sprite
      if self.name == k:
        #trainerSprite = trainerSpriteList[i]
        trainerSpritePos = trainerSpritePosList[i]
      #Enemy sprite
      if Pokemon2.name == k:
        #enemySprite = enemySpriteList[i]
        enemySpritePos = enemySpritePosList[i]

  

    #Information

    #Trainer pokemon name
    trainerPokeName = ((self.name).upper())
    textTPN = font2.render(trainerPokeName, 1, (0, 0, 0))
    #Enemy pokemon name
    enemyPokeName = ((Pokemon2.name).upper())
    textEPN = font2.render(enemyPokeName, 1, (0, 0, 0))
    #Trainer pokemon level
    levelTP = ("lv" + str(self.level))
    textLevelTP = font2.render(levelTP, 1, (0, 0, 0))
    #Enemy pokemon level
    levelEP = ("lv" + str(Pokemon2.level))
    textLevelEP = font2.render(levelEP, 1, (0, 0, 0))
    #Trainer HP
    HPString = str(self.HP) + " / " + str(self.maxHP)
    HPText = font2.render(HPString, 1, (1, 1, 1))

    #Printing all the information
    win.blit(textEPN, (25, 72))
    win.blit(textLevelEP, (149, 72))
    win.blit(textTPN, (266, 197))
    win.blit(textLevelTP, (390, 197))
    win.blit(trainerSprite, trainerSpritePos)
    win.blit(enemySprite, enemySpritePos)    
    win.blit(HPText, (357, 228)) 

    screenPrint(trainerPokeName, 266, 197, (1, 1, 1), False, font2)
    screenPrint(enemyPokeName, 25, 72, (1, 1, 1), False, font2)
    screenPrint(levelTP, 390, 197, (1, 1, 1), False, font2)
    screenPrint(levelEP, 149, 72, (1, 1, 1), False, font2)
    screenPrint(HPString, 357, 228, (1, 1, 1), False, font2)
    

    #HEALTH
    self.healthCheck(329, 223, True)
    Pokemon2.healthCheck(88, 98, False)
    pygame.display.update()
    
  #--------Checking health--------
  def healthCheck(self, barPosX, barPosY, user):
    global healthRatio
    global damageRatio
    global lastBarLength
    global enemyLastBarLength
    global HPAnimation
    #HEALTH RATIO
    healthRatio = self.HP / self.maxHP

    #HEALTH COLOURS
    #Health is more than or equal to half
    if healthRatio >= 0.5:
      #Green
      healthColour = (101, 242, 157)
    #health is less than half or more than one fifth
    elif healthRatio < 0.5 and healthRatio > 0.2:
      #Yellow
      healthColour = (250, 225, 45)
    #Health is less than a fifth
    else:
      #Red
      healthColour = (246, 78, 45)
        

    #HEALTH BAR LENGTH
    barLength = round(healthRatio * 87)
    pygame.draw.rect(win, healthColour, (barPosX, barPosY, barLength, 7))
    if user == True:
      enemyLastBarLength = barLength
    else:
      lastBarLength = barLength
  
  #--------INPUT AND STUFF--------
  def screenCheck(self, Pokemon2):
    #global keyCount
    #global keyCount2
    global selectUp
    global selectDown
    global selectRight
    global selectLeft
    global menuSelectS
    global menuSelectD 
    global battleScreen
    global moveScreen
    global bagScreen
    global pokeScreen
    global inBattle
    global up
    global down
    global left
    global right
    global P_offsetX1
    global P_offsetX2
    global P_offsetY1
    global P_offsetY2 
    global selectedMove
    global pokeMove
    global movePower
    global maxMovePP
    global movePP
    global moveIndex
    global ballIndex
    global index
    global ballList
    global ballAmountList
    global run
    global FPS
    global ballType
    global ballSpriteList
    global battlingPokemon
    global inPokemart
    global struggle
    keysInputMenu()

    #BATTLE SCREEN
    if battleScreen == True:
      menuScreen = battleMenu
      menuPosX = 230
      menuPosY = 261
      P_offsetX1 = 13
      P_offsetX2 = 117
      P_offsetY1 = 23
      P_offsetY2 = 51
      P_offsetX = P_offsetX1
      P_offsetY = P_offsetY1
      textUp = ("What will ")
      textDown = (self.name + " do?")
      windowTextUp = font.render(textUp, 1, (255, 255, 255))
      windowTextDown = font.render(textDown, 1, (255, 255, 255))
      

      #SELECTING AN OPTION
      if menuSelectD == True:
        #Selecting FIGHT
        if up and left == True:
          battleScreen = False
          moveScreen = True
          menuSelectD = False
          bagScreen = False

        #Selecting RUN
        if down and right == True:
          runawaySFX.play()
          self.printBattleBG(Pokemon2)
          text = "Got away safely..."
          Pokemon2.HP = Pokemon2.maxHP
          #Print the text and delay
          screenPrint(text, battleTextX, battleTextY, (255, 255, 255), True, font)
          pygame.time.delay(400)
          battleScreen = False
          inBattle = False

        #Selecting BAG
        if up and right == True:
          bagScreen = True
          battleScreen = False
          moveScreen = False
          menuSelectD = False
          ballIndex = 0
          P_offsetY = 70
        
        #Selecting POKEMON
        if down and left:
          bagScreen = False
          battleScreen = False
          moveScreen = False
          menuSelectD = False
          pokeScreen = True
          index = 0
          #ballIndex = 0
          #P_offsetY = 70


    #-----------MOVE SCREEN-----------
    if moveScreen == True:
      menuScreen = movesMenu
      menuPosX = 0
      menuPosY = 261
      P_offsetX1 = 13
      P_offsetX2 = 150
      P_offsetY1 = 23
      P_offsetY2 = 51
      P_offsetX = P_offsetX1
      P_offsetY = P_offsetY1

      #Rendering the moves on screen
      textUp = (self.moves[0])
      textDown = (self.moves[2])
      textRD = (self.moves[3])
      textRU = (self.moves[1])
      windowTextUp = font2.render(textUp, 1, (0, 0, 0))
      windowTextDown = font2.render(textDown, 1, (0, 0, 0))
      windowTextRU = font2.render(textRU, 1, (0, 0, 0))
      windowTextRD = font2.render(textRD, 1, (0, 0, 0))

      #Move PP
      maxMovePPText = font2.render(str(maxMovePP), 1, (0, 0, 0))
      movePPText = font2.render(str(movePP), 1, (0, 0, 0))

        #Top left move
      if up and left == True:
        pokeMove = (self.moves[0])
        movePower = (self.movePowerList[0])
        maxMovePP = (self.maxPPList[0])
        movePP = (self.movePPList[0])
        moveIndex = 0
        
        #Top right move
      if up and right == True:
        pokeMove = (self.moves[1])
        movePower = (self.movePowerList[1])
        maxMovePP = (self.maxPPList[1])
        movePP = (self.movePPList[1])
        moveIndex = 1
        #Bottom left move
      if down and left == True:
        pokeMove = (self.moves[2])
        movePower = (self.movePowerList[2])
        maxMovePP = (self.maxPPList[2])
        movePP = (self.movePPList[2])
        moveIndex = 2

        #Bottom right move
      if down and right == True:
        pokeMove = (self.moves[3])
        movePower = (self.movePowerList[3])
        maxMovePP = (self.maxPPList[3])
        movePP = (self.movePPList[3])
        moveIndex = 3


      #SELECTING A MOVE
      if menuSelectD == True:
        
        # Struggle check (struggle is when Pokemon have no PP in any move)
        struggle = True
        for i,k in enumerate(self.movePPList):
          if k <= 0:
            pass
          else:
            struggle = False
        print("STRUGGLE: " + str(struggle))

        #Only use the move if there's enough PP left
        if struggle == False:
          #Only uses moves that have more than 0 PP
          if movePP <= 0:
            self.printBattleBG(Pokemon2)
            screenPrint("Not enough PP for this move...", battleTextX, battleTextY, (255, 255, 255), True, font)
            pygame.time.delay(500)
          #Actually selecting a move
          else:
            selectedMove = True 

        #if Struggle is true, then selected move is true
        else:
          selectedMove = True 
        

            
      

      #MOVETYPE
      self.moveTypeCheck(pokeMove)
      moveTypeText = ""
      #Displaying type of the move in the fight screen submenu
      for i,char in enumerate(moveType):
        moveTypeText += char
        if i == 5:
          break
      
      moveTypePrint = font2.render((moveTypeText.upper()), 1, (0, 0, 0))

      #Going back to normal menu
      if menuSelectS == True or selectedMove == True:
        textDown = ("")
        textUp = ("") 
        windowTextUp = font.render(textUp, 1, (0, 0, 0))
        windowTextDown = font.render(textDown, 1, (0, 0, 0))
        self.printBattleBG(Pokemon2)
        pygame.display.update()
        menuScreen = battleMenu
        moveScreen = False
        battleScreen = True
        menuPosX = 230
        menuPosY = 261

    #---------MOVING CURSOR--------
    #Going up
    if selectUp == True and bagScreen == False:
      P_offsetY = P_offsetY1
      up = True
      down = False
    #Going down
    if selectDown == True and bagScreen == False:
      P_offsetY = P_offsetY2
      down = True
      up = False
    #GOing right
    if selectRight == True and bagScreen == False:
      P_offsetX = P_offsetX2
      right = True
      left = False
    #Going left
    if selectLeft == True and bagScreen == False:
      P_offsetX = P_offsetX1
      left = True
      right = False

    #----------BAG SCREEN---------
    firstTime = True
    while bagScreen == True:

      clock.tick(10)
      #QUIT
      for event in pygame.event.get():
        if event.type == QUIT:
          run = False
          battleScreen = False
          bagScreen = False
          moveScreen = False
          inBattle = False
          pygame.quit()
          
      keysInputMenu()
      #Resetting variables
      menuScreen = bagBG
      menuPosX = 0
      menuPosY = 0
      P_offsetX = 167
      P_offsetY1 = 70
      P_offsetY2 = 101
      P_offsetY3 = 133
      P_offsetY4 = 163
      P_offsetY5 = 190
      P_offsetY6 = 218
      ballTextOffset = 67

      pointerOffsetList = [P_offsetY1, P_offsetY2, P_offsetY3, P_offsetY4, P_offsetY5, P_offsetY6]
  
      if firstTime == True:
        #Reprinting menu
        P_offsetY = P_offsetY1
        win.blit(menuScreen, (menuPosX, menuPosY))
        indexMax = -1
        ballList2 = ["Poke Ball", "Great Ball", "Ultra Ball", "Master Ball"]
        for i,k in enumerate(ballList):
          for a,z in enumerate(ballList2):
            if z == k:
              screenPrint("x" + str(ballAmountList[i]), 395, ballTextOffset, (0, 0, 0), False, font)
              screenPrint(k, 182, ballTextOffset, (0, 0, 0), False, font)
              ballTextOffset += 30
              indexMax += 1
        firstTime = False
      
      
      if indexMax >= 0:
        ballType = ballList[ballIndex]
      else:
        ballType = ""
      #ballSprite = ballSpriteList[ballIndex]

      #---MOVING CURSOR---
      #Moving cursor up
      if selectUp == True and P_offsetY != P_offsetY1:
        #Reprinting menu
        reprintMenuScreen(menuScreen, menuPosX, menuPosY, "bag")

        #Raising the pointer
        ballIndex -= 1
        selectUp = False        
      
      #Moving cursor down
      if selectDown == True and P_offsetY != P_offsetY6:
        #Reprinting menu
        reprintMenuScreen(menuScreen, menuPosX, menuPosY, "bag")

        #Lowering the pointer
        if ballIndex == indexMax:
          pass
        else:
          ballIndex += 1
        selectDown = False

      #Display the pointer
      P_offsetY = pointerOffsetList[ballIndex]
      win.blit(Pointer2, (menuPosX + P_offsetX, menuPosY + P_offsetY))
      pygame.display.update()

      #Selecting a pokeball
      if menuSelectD == True and inBattle == True:
        if indexMax >= 0:
          self.catch(Pokemon2)
          ballAmountList[ballIndex] -= 1
          #Removing the item if all of it is used
          if ballAmountList[ballIndex] == 0:
            ballList.remove(ballList[ballIndex])
            ballAmountList.remove(ballAmountList[ballIndex])
        
        else:
          win.blit(textBox, (0, -47))
          pygame.display.update()
          textUp = "You don't have any POKE BALLS"
          textDown = "Go to the shop and buy some"
          screenPrint(textUp, textPosX, textPosY - 47, (0, 0, 0), True, font)
          screenPrint(textDown, textPosX, textPosY + 25 - 47, (0, 0, 0), True, font)
          pygame.time.delay(450)

          #Reprinting menu
          reprintMenuScreen(menuScreen, menuPosX, menuPosY, "bag")

        #Go back to original screen
        menuScreen = battleMenu

        textDown = ("")
        textUp = ("") 
        windowTextUp = font.render(textUp, 1, (0, 0, 0))
        windowTextDown = font.render(textDown, 1, (0, 0, 0))
        self.printBattleBG(Pokemon2)
        pygame.display.update()
        menuScreen = battleMenu
        moveScreen = False
        bagScreen = False
        battleScreen = True
        bagScreen = False
        P_offsetX = 13
        P_offsetY = 23
        menuPosX = 230
        menuPosY = 261
  
      #Exiting bag and going back to normal menu
      if menuSelectS == True and inBattle == True:
        textDown = ("")
        textUp = ("") 
        windowTextUp = font.render(textUp, 1, (0, 0, 0))
        windowTextDown = font.render(textDown, 1, (0, 0, 0))
        self.printBattleBG(Pokemon2)
        pygame.display.update()
        menuScreen = battleMenu
        moveScreen = False
        battleScreen = True
        bagScreen = False
        P_offsetX = 13
        P_offsetY = 23
        menuPosX = 230
        menuPosY = 261
      
      if menuSelectS == True and inPokemart == True:
        textDown = ("")
        textUp = ("") 
        windowTextUp = font.render(textUp, 1, (0, 0, 0))
        windowTextDown = font.render(textDown, 1, (0, 0, 0))
        #menuScreen = battleMenu
        moveScreen = False
        battleScreen = False
        bagScreen = False
        pokeScreen = False
        up = True
        down = False
        left = True
        right = False
        P_offsetX = 13
        P_offsetY = 23
        menuPosX = 230
        menuPosY = 261
        redrawGameWindow(pokemartBG)
        break
    
    #-----------POKEMON MENU------------
    while pokeScreen == True:
      
      clock.tick(FPS)
      #QUIT
      for event in pygame.event.get():
        if event.type == QUIT:
          run = False
          battleScreen = False
          bagScreen = False
          moveScreen = False
          inBattle = False
          pokeScreen = False
          pygame.quit()
          
      keysInputMenu()
      #Resetting variables
      menuScreen = pokeSubMenu2
      menuPosX = 173
      menuPosY = 69
      P_offsetX = 166
      P_offsetY1 = 79
      pokeNameOffset = 67

      if firstTime == True:
        pokeScreenBGPrint(menuScreen, menuPosX, menuPosY, pokeNameOffset)
        index = 0
        selectUp = False
        selectDown = False
        firstTime = False
      #---MOVING CURSOR---
      #Moving cursor up
      if selectUp == True and index != 0:
        #Reprinting menu
        pokeScreenBGPrint(menuScreen, menuPosX, menuPosY, pokeNameOffset)
        #Raising the pointer
        index -= 1
        selectUp = False        
      
      #Moving cursor down
      if selectDown == True and index != 4:
        #Reprinting menu
        pokeScreenBGPrint(menuScreen, menuPosX, menuPosY, pokeNameOffset)
        #Raising the pointer
        index += 1
        selectDown = False    

      #Display the pointer
      P_offsetY = P_offsetY1 + (index * 45)
      win.blit(Pointer2, (P_offsetX, P_offsetY))
      pygame.display.update()
      
      #SELECTING A POKEMON
      count = 0
      for i in enumerate(trainerPartyList):
          count += 1
      if menuSelectD == True and inBattle == True and (index + 2 <= count):
        
        if (index + 1 < count) and trainerPartyList[index + 1].HP > 0:
          #Swithcing chosen pokemon to with the battling pokemon
          battlingPokemon = trainerPartyList[index + 1]
          trainerPartyList[index + 1] = self
          trainerPartyList[0] = battlingPokemon
          print("Battling pokemon: " + battlingPokemon.name)
          self = battlingPokemon
          
          #Exiting pokemon menu 
          textDown = ("")
          textUp = ("") 
          windowTextUp = font.render(textUp, 1, (0, 0, 0))
          windowTextDown = font.render(textDown, 1, (0, 0, 0))
          self.printBattleBG(Pokemon2)
          pygame.display.update()
          menuScreen = battleMenu
          moveScreen = False
          battleScreen = True
          bagScreen = False
          pokeScreen = False
          P_offsetX = 13
          P_offsetY = 23
          up = True
          down = False
          left = True
          right = False
          menuPosX = 230
          menuPosY = 261

          #Continuing turn
          self.printBattleBG(Pokemon2)
          screenPrint("You switched out to", battleTextX, battleTextY, (255, 255, 255), True, font)
          screenPrint(self.name.upper(), battleTextX, battleTextY2, (255, 255, 255), True, font)
          pygame.time.delay(450)
          self.turnContinue(Pokemon2)
        else:
          pokeScreenBGPrint(menuScreen, menuPosX, menuPosY, pokeNameOffset)
          screenPrint("You can't switch bro", battleTextX, battleTextY, (255, 255, 255), True, font)


      #EXIIING POKEMON MENU and going back to normal menu
      if menuSelectS == True and inBattle == True:
        textDown = ("")
        textUp = ("") 
        windowTextUp = font.render(textUp, 1, (0, 0, 0))
        windowTextDown = font.render(textDown, 1, (0, 0, 0))
        self.printBattleBG(Pokemon2)
        pygame.display.update()
        menuScreen = battleMenu
        moveScreen = False
        battleScreen = True
        bagScreen = False
        pokeScreen = False
        up = True
        down = False
        left = True
        right = False
        P_offsetX = 13
        P_offsetY = 23
        menuPosX = 230
        menuPosY = 261
    
      if menuSelectS == True and inBattle == False:
        textDown = ("")
        textUp = ("") 
        windowTextUp = font.render(textUp, 1, (0, 0, 0))
        windowTextDown = font.render(textDown, 1, (0, 0, 0))
        menuScreen = battleMenu
        moveScreen = False
        battleScreen = False
        bagScreen = False
        pokeScreen = False
        up = True
        down = False
        left = True
        right = False
        P_offsetX = 13
        P_offsetY = 23
        menuPosX = 230
        menuPosY = 261
        break



    #------------DISPLAYING MOVES AND MOVE INFO-------------
    
    if moveScreen == True:
      #Reprinting menu
      win.blit(menuScreen, (menuPosX, menuPosY))
      #Display Moves
      win.blit(windowTextUp, (26, 280))
      win.blit(windowTextDown, (26, 310))
      win.blit(windowTextRU, (166, 280))
      win.blit(windowTextRD, (166, 310))
      #Display PP
      win.blit(maxMovePPText, (412, 280))
      win.blit(movePPText, (370, 280))
      #Display move type
      win.blit(moveTypePrint, (360, 312))
    elif bagScreen == True or pokeScreen == True or inPokemart == True:
      pass

      
    else:
      #Reprinting menu
      win.blit(menuScreen, (menuPosX, menuPosY))
      #Display text
      win.blit(windowTextUp, (battleTextX, battleTextY))
      win.blit(windowTextDown, (battleTextX, battleTextY2))

    if (bagScreen == False or pokeScreen == False) and inPokemart == False:
      #Display the pointer
      win.blit(Pointer2, (menuPosX + P_offsetX, menuPosY + P_offsetY))
      pygame.display.update()
  
  #--------TYPE MATCHUPS--------
  def typeMatchUp(self, enemyType, moveType):
    global SEffective
    global NVEffective
    global effective

    #ENEMY TYPE IS FIRE
    if enemyType == "Fire":
      #SUPEREFFECTIVE
      if moveType == "Water":
        SEffective = True
      #NOT VERY EFFECTIVE
      elif moveType == "Grass":
        NVEffective = True
      #EFFECTIVE
      else:
        effective = True
      
    typeList = ["Fire", "Water", "Grass", "Electric", "Poison", "Flying"]
    #ENEMY TYPE IS WATER
    if enemyType == "Water":
      #SUPEREFFECTIVE
      if moveType == "Grass" or moveType == "Electric":
        SEffective = True
      #NOT VERY EFFECTIVE
      elif moveType == "Fire":
        NVEffective = True
      #EFFECTIVE
      else:
        effective = True
    
    typeList = ["Fire", "Water", "Grass", "Electric", "Poison", "Flying"]
    #ENEMY TYPE IS GRASS
    if enemyType == "Grass":
      #SUPEREFFECTIVE
      if moveType == "Fire" or moveType == "Flying" or moveType == "Poison":
        SEffective = True
      #NOT VERY EFFECTIVE
      elif moveType == "Electric" or moveType == "Water":
        NVEffective = True
      #EFFECTIVE
      else:
        effective = True
    
    typeList = ["Fire", "Water", "Grass", "Electric", "Poison", "Flying"]
    #ENEMY TYPE IS ELECTRIC
    if enemyType == "Electric":
      #SUPEREFFECTIVE
        #Nothing is super effective
      
      #NOT VERY EFFECTIVE
      if moveType == "Flying":
        NVEffective = True
      #EFFECTIVE
      else:
        effective = True
    
    typeList = ["Fire", "Water", "Grass", "Electric", "Poison", "Flying"]
    #ENEMY TYPE IS POISON
    if enemyType == "Poison":
      #SUPEREFFECTIVE
        #Nothing is super effective
      
      #NOT VERY EFFECTIVE
      if moveType == "Grass":
        NVEffective = True
      #EFFECTIVE
      else:
        effective = True
    
    #SAME TYPE
    if enemyType == moveType:
      NVEffective = True
      effective = False
      SEffective = False

  #--------CHECKING TYPE OF MOVES--------
  def moveTypeCheck(self, pokeMove):
    global moveType
    #ELECTRIC TYPE
    if pokeMove == "Thunder wave" or pokeMove == "Thundershock" or pokeMove == "Thunderbolt":
      moveType = "Electric"
    #FIRE TYPE
    elif pokeMove == "Ember":
      moveType = "Fire"
    #GRASS TYPE
    elif pokeMove == "Razor leaf" or pokeMove == "Sleep powder" or pokeMove == "Leaf storm":
      moveType = "Grass"
    #WATER TYPE
    elif pokeMove == "Bubble":
      moveType = "Water"
    #NORMAL TYPE
    else:
      moveType = "Normal"
  
  #--------CATCHING METHOD--------
  def catch(self, Pokemon2):
    global ballType
    global enemySleep
    global paralysis
    global wildPokemon
    global pokeNum
    global trainerPartyList
    global inBattle
    global boxList
    global ballList
    global ballIndex
    global moveIndex
    global moveType
    global backgroundMusic
    global pokedexList

    #calculating ball modifier
    if ballType == "Great Ball":
      ballMod = 1.5
    elif ballType == "Ultra Ball":
      ballMod = 2
    else:
      ballMod = 1

    #Calculating status modifier
    if enemySleep == True:
      statusMod = 2
    elif paralysis == True:
      statusMod = 1.5
    else:
      statusMod = 1

    catchRate = math.floor(((3*Pokemon2.maxHP - 2*Pokemon2.HP) / (3 * Pokemon2.maxHP)) * Pokemon2.speciesRate * ballMod * statusMod)
    if Pokemon2.level < 14:
      catchRate += 50
    print("CATCH RATE BEFORE: " + str(catchRate))
    #Catch rate cant be 0 or more than 255
    if catchRate <= 0:
      catchRate = 1
    if catchRate > 255:
      catchRate = 255
    
    print("CATCH RATE AFTER: " + str(catchRate))
    #Seeing if pokemon was caught
    randNum = random.randint(0, 255)
    print("RANDOM NUMBER: " + str(randNum))
    #Pokemon is caught if random number is less than or equal to the catch rate
    if randNum <= catchRate:
      pokeCaught = True
    else:
      pokeCaught = False
    
    #Pokemon is always caught using a master ball
    if ballType == "Master Ball":
      pokeCaught = True
    
    #Printing information
    print("Poke Caught: "+ str(pokeCaught))
    self.printBattleBG(Pokemon2)
    screenPrint("You threw a " + ballList[ballIndex].upper() + "!", battleTextX, battleTextY, (255, 255, 255), True, font)
    pygame.time.delay(1000) 
    
    #CATCHING POKEMON
    if pokeCaught == True:
      #play victory music
      backgroundMusic = pygame.mixer.music.load('victory2.mp3')
      pygame.mixer.music.play(-1)

      #Printing information
      self.printBattleBG(Pokemon2)
      screenPrint("You caught a " + Pokemon2.name.upper() + "!", battleTextX, battleTextY, (255, 255, 255), True, font)
      pygame.time.delay(500)
      
      self.battleVictory(Pokemon2)
      
      #POKEDEX ENTRY
      caughtAlready = False
      allPokeList = trainerPartyList + boxList
      # Checking to see if the pokemon has been caught before
      for i,k in enumerate(allPokeList):
        if wildPokemon.name == k.name:
          caughtAlready = True
      
      if caughtAlready == True:
        pass
      else:
        pokedexList += [wildPokemon.name]
      print("POKEDEX: " + str(pokedexList))

      #Adding to party if less than 6 pokemon
      if pokeNum >= 6:
        boxList += [wildPokemon]
      #Adding to boxes if party is more than 6 pokemon
      else:
        trainerPartyList += [wildPokemon]
      
      pokeNum +=1
      inBattle = False
      
      #Pinting info to terminal 
      for i,k in enumerate(trainerPartyList):
          print("POKEMON: " + k.name + " HP: " + str(k.HP))
      for i,k in enumerate(boxList):
          print("BOX: " + k.name + " HP: " + str(k.HP))
      
      
    #NOT CATCHING POKEMON and continuing battle
    else:
      #Printing information
      self.printBattleBG(Pokemon2)
      screenPrint(Pokemon2.name.upper() + " broke free!", battleTextX, battleTextY, (255, 255, 255), True, font)
      pygame.time.delay(500)
      self.printBattleBG(Pokemon2)
      self.turnContinue(Pokemon2)

  #--------CONTINUING TURN--------
  def turnContinue(self, Pokemon2):
    #Enemy turn (continuing battle)
    randomNum = random.randint(0, 3)
    print("RANDOM: "+ str(randomNum))
    enemyPokeMove = (Pokemon2.moves[randomNum])
    enemyMovePower = (Pokemon2.movePowerList[randomNum])
    moveIndex = randomNum

    #Checking type of move
    Pokemon2.moveTypeCheck(enemyPokeMove)
    enemyMoveType = moveType
    #Calculating damage
    Pokemon2.damageCalculation(self, enemyPokeMove, enemyMovePower, enemyMoveType, False)

  #--------DAMAGE CALCULATION METHOD--------
  def damageCalculation(self, Pokemon2, pokeMove, movePower, moveType, user):
    global selectedMove
    global SEffective
    global NVEffective
    global effective
    global moveIndex
    global enemyLastBarLength
    global lastBarLength
    global attackStatStage
    global userSleep
    global enemySleep
    global paralysis
    global sleep
    global struggle

    # IF THE USER HAS NO PP LEFT - STRUGGLE
    if user == True and struggle == True:
      #DAMAGE CALCULATION
      movePower = 5
      damage = math.floor(((((((2*self.level)/5)+2) * movePower * ((self.attackStats)/Pokemon2.defenseStats))/50)+2))
      print("DAMAGE: " + str(damage))

      self.printBattleBG(Pokemon2)
      screenPrint(self.name.upper() + " struggled...", battleTextX, battleTextY, (255, 255, 255), True, font)

      #Deal a little damage
      Pokemon2.HP -= damage
      #Make sure pokemon dont have negative health
      if Pokemon2.HP < 0:
        Pokemon2.HP = 0

      #HP animation for enemy
      healthRatio =  Pokemon2.HP / Pokemon2.maxHP
      HPAnimation(healthRatio, 88, 98, enemyLastBarLength)
      self.printBattleBG(Pokemon2)
      pygame.time.delay(300)

      #User's pokemon is damaged more
      movePower = 35
      damage = math.floor(((((((2*self.level)/5)+2) * movePower * ((self.attackStats)/Pokemon2.defenseStats))/50)+2))
      self.HP -= damage
      #Make sure user doesn't have negative health
      if self.HP < 0:
        self.HP = 0

      #HP animation for user
      healthRatio =  self.HP / self.maxHP
      HPAnimation(healthRatio, 329, 223, lastBarLength)  
      self.printBattleBG(Pokemon2)
      pygame.time.delay(300)

    # NORMAL BATTLE CALCULATIONS
    else:
      #PP stuff
      if self.movePPList[moveIndex] > 0:
        self.movePPList[moveIndex] -= 1
        
      else:
        print("MoveFailed")
        flail = True
        selectedMove = False
        
      #Text showing what move the trainer's pokemon used
      if user == True:
        self.printBattleBG(Pokemon2)
      else:
        Pokemon2.printBattleBG(self)
      #Print 'pokemon name' used 'pokemon move'

      upperText = ((self.name).upper()) + " used"
      if user == False:
        upperText = ("Foe " + (self.name).upper()) + " used"
      lowerText = (pokeMove.upper() + "!")
      screenPrint(upperText, battleTextX, battleTextY, (255, 255, 255), True, font)
      screenPrint(lowerText, battleTextX, battleTextY2, (255, 255, 255), True, font)
      if user == False:
        pygame.time.delay(200)
      pygame.time.delay(500)

      #Checking types
      print(pokeMove)
      
      
      if self.type == moveType:
        STAB = 1.5
      else:
        STAB = 1
      print(moveType + "   " + str(STAB))

      typeList = ["Fire", "Water", "Grass", "Electric", "Normal"]

      #First Type calculation for trainer battling wild pokemon
      self.typeMatchUp(Pokemon2.type, moveType)
      if SEffective == True:
        typeAdvtg = 2
      if NVEffective == True:
        typeAdvtg = 0.5
      if effective == True:
        typeAdvtg = 1
      
      print("SEffective: " + str(SEffective))
      print("NVEffective: " + str(NVEffective))
      print("effective: " + str(effective))
      
      #Reset for second calculation
      SEffective = False
      NVEffective = False
      effective = False

      #Second Type calculation for trainer battling wild pokemon
      self.typeMatchUp(Pokemon2.type2, moveType)
      if SEffective == True:
        typeAdvtg *= 2
      if NVEffective == True:
        typeAdvtg *= 0.5
      if effective == True:
        typeAdvtg *= 1
      
      #Effective
      if typeAdvtg == 1:
        effective == True
      #Not very effective
      if typeAdvtg < 1:
        NVEffective = True
      #Super effective
      if typeAdvtg > 1:
        SEffective = True
      
      print("typeAdvtg: " + str(typeAdvtg))

      
      #Random factor
      randomFactor = (random.randint(85, 100) / 100)

      #Critical hit claculation
      criticalThreshold = math.floor(self.speed / 2)
      criticalRandom = random.randint(0, 255)
      
      criticalHit = False
      if criticalRandom < criticalThreshold:
        critical = ((2*self.level) + 5) / (self.level + 5)
        criticalHit = True
        print("CRITICAL HIT!!!")
      else:
        critical = 1

      
      print("Power: " + str(movePower))
      #DAMAGE CALCULATION
      damage = math.floor(((((((2*self.level)/5)+2) * movePower * ((self.attackStats)/Pokemon2.defenseStats))/50)+2)*critical*randomFactor*STAB*typeAdvtg)
      print("DAMAGE: " + str(damage))

      #SPECIAL MOVES
      if pokeMove == "Growl" or pokeMove == "Thunder wave" or pokeMove == "Sleep powder":
        
        #Neutral damage / effect
        damage = 0
        NVEffective = False
        effective = True
        SEffective = False
        criticalHit = False
        text2 = ""
        #ATTACK GO DOWN
        if pokeMove == "Growl":
          #Lower attack stat
          attackStatStage += 1
          Pokemon2.attackStats = 1/(attackStatStage) * Pokemon2.maxAttackStats
          #Print the things
          text = ((Pokemon2.name).upper()) + "'s " + "attack was lowered..."
          if user == True:
            text = "Foe " + ((Pokemon2.name).upper()) + "'s "
            text2 = "attack was lowered"
        
        #PARALYZED
        if pokeMove == "Thunder wave":
          print("SPEED B4: " + str(Pokemon2.speedStats))
          Pokemon2.speedStats *= 1/2
          print("SPEED AFTER: " + str(Pokemon2.speedStats))
          #Print the things
          text = ((Pokemon2.name).upper()) + " is paralysed"
          if user == True:
            text = "Foe " + ((Pokemon2.name).upper())
            text2 = "is paralysed"
            enemyParalyze = True
          else:
            userParalyze = True
        
        #SLEEPING
        if pokeMove == "Sleep powder":
          text = ((Pokemon2.name).upper()) + " fell asleep"
          if user == True:
            text = "Foe " + ((Pokemon2.name).upper())
            text2 =  "fell asleep"
            enemySleep = True
          else:
            userSleep = True

        #reset background
        if user == True:
          self.printBattleBG(Pokemon2)
        else:
          Pokemon2.printBattleBG(self)
        #Print the text and delay
        screenPrint(text, battleTextX, battleTextY, (255, 255, 255), True, font)
        screenPrint(text2, battleTextX, battleTextY2, (255, 255, 255), True, font)
        pygame.time.delay(500)    
      
      
      #----ACCURACY----
      useMove = False
      #Parlyzed
      if paralysis == True:
        accuracy = 75
        statusTextUp = self.name.upper() + " is paralysed"
        statusTextDown = "and unable to can"
      #Sleeping
      elif (userSleep and user == True) or (enemySleep == True and user == False): 
        # 50% chance of waking up
        randNum = random.randint(1,2)
        # Still falling asleep
        if randNum == 1:
          statusTextUp = self.name.upper() + " is asleep..."
          statusTextDown = ""
          accuracy = 0
          # Waking up
        else:
          screenPrint(self.name + " woke up!", battleTextX, battleTextY, (255, 255, 255), True, font)
          accuracy = 100
      
      # No status
      else:
        accuracy = 100
        statusTextUp = ""
        statusTextDown = ""
      
      print("ACCURACY: " + str(accuracy))
      randNum = random.randint(1, 100)
      print("RandNum: " + str(randNum))
      if randNum <= accuracy:
        useMove = True
      else:
        useMove = False
      

      #----USING A MOVE----
      if useMove == True:
        #Deal damage
        Pokemon2.HP -= damage
        #Make sure pokemon dont have negative health
        if Pokemon2.HP < 0:
          Pokemon2.HP = 0
        print("ENEMY HP: " + str(Pokemon2.HP))

        
        
        #HEALTH
        healthRatio =  Pokemon2.HP / Pokemon2.maxHP
        if user == True:
          HPAnimation(healthRatio, 88, 98, lastBarLength)
        else:
          HPAnimation(healthRatio, 329, 223, enemyLastBarLength)         
        
        pygame.time.delay(300)

        if SEffective == True or NVEffective == True:
          #reset background
          if user == True:
            self.printBattleBG(Pokemon2)
          else:
            Pokemon2.printBattleBG(self)

          #Print if it was super effective
          if SEffective:
            text = "It's super effective!"
          #Print if it was not very effective
          if NVEffective:
            text = "It's not very effective..."
          
          #Print the text and delay
          screenPrint(text, battleTextX, battleTextY, (255, 255, 255), True, font)
          pygame.time.delay(500)
        
        if criticalHit:
          #reset background
          if user == True:
            self.printBattleBG(Pokemon2)
          else:
            Pokemon2.printBattleBG(self)
          text = "A CRITICAL HIT!"

          #Print the text and delay
          screenPrint(text, battleTextX, battleTextY, (255, 255, 255), True, font)
          pygame.time.delay(400)

      else:
        screenPrint(statusTextUp, battleTextX, battleTextY, (255, 255, 255), True, font)
        screenPrint(statusTextDown, battleTextX, battleTextY2, (255, 255, 255), True, font)
        pygame.time.delay(450)
      
      #Reset the type advantages
      SEffective = False
      NVEffective = False
      effective = False
      selectedMove = False
      specialMove = False
      attackDown = False
      paralysis = False
      sleep = False

      if user == True:
        self.printBattleBG(Pokemon2)
      else:
        Pokemon2.printBattleBG(self)
      pygame.time.delay(200)

  #--------BATTLE VICTORY--------
  def battleVictory(self, Pokemon2):
    global trainerPartyList
    global money
    global levelAdd
    global coinMultiplier

    partyCount = 0
    #levelling up
    for i,k in enumerate(trainerPartyList):
      #Maxed out at level 100
      if k.level < 100:
        k.level += levelAdd
      if k.level > 100:
        k.level = 100

      HPRatio = k.HP / k.maxHP
      self.printBattleBG(Pokemon2)
      k.statsCheck()
      k.HP = round(HPRatio * k.maxHP)
      partyCount += 1

    #levelUpSFX.play()
    if partyCount == 1:
      screenPrint(k.name + " levelled up to " + str(k.level), battleTextX, battleTextY, (255, 255, 255), True, font)
    else:
      screenPrint("Your team levelled up by " + str(levelAdd), battleTextX, battleTextY, (255, 255, 255), True, font)
    pygame.time.delay(450)
    
    #Gaining prize money
    randNum = random.randint(95, 115)
    randNum /= 100
    prizeMoney = round(100 * Pokemon2.level * randNum) * coinMultiplier
    self.printBattleBG(Pokemon2)
    screenPrint("You gained $" + str(prizeMoney) + "!", battleTextX, battleTextY, (255, 255, 255), True, font)
    money += prizeMoney
    pygame.time.delay(2000)

    backgroundMusic = pygame.mixer.music.load('Pokemon route 1 music2.mp3')
    pygame.mixer.music.play(-1)

    #probably have to do a click confirm

  #--------FIGHTING METHOD--------
  def fight(self, Pokemon2):
    global firstCount
    global run
    global inBattle

    global battleScreen
    global moveScreen
    global bagScreen
    global battlePartyScreen

    global up
    global down
    global left
    global right
    global pokeMove
    global moveType
    global selectedMove
    global FPS

    global NVEffective
    global SEffective
    global effective

    global movePower
    global healthRatio
    global damageRatio

    global HPAnimation
    global moveIndex

    global attackStatStage
    global specialMove
    global attackDown
    global paralysis
    global enemySleep
    global userSleep
    global attackStatStage

    global inPokecenter
    global battlingPokemon
    global money

    global menuSelectD
    global pokeScreen
    global backgroundMusic

    global continueTurn

    battlingPokemon = self

    attackStatStage = 1

    moveType = ""
    STAB = 1
    self.printBattleBG(Pokemon2)
    #Fighting mechanism
    typeList = ["Fire", "Water", "Grass", "Electric", "Poison", "Flying"]

    #TYPE MATCHUPS
    #for i,k in enumerate(typeList):
    
        #Both are same 
        #if self.moveType == k:
            #if Pokemon2.moveType == k:
                #stringAttack1 = "Its not very effective..."
                #stringAttack2 = "Its not very effective..."
                #notEffective = True
    
    #Resetting variables  
    up = True
    down = False
    left = True
    right = False
    inBattle = True
    battleScreen = True
    moveScreen = False
    firstCount = 0
    #selectedMove = False

    #ACTUAL BATTLE  
    while inBattle == True:
      self = battlingPokemon

      #POKEMON FAINTING
      if self.HP <= 0:

        #reset background
        self.printBattleBG(Pokemon2)
        text = self.name.upper() + " fainted..."
        #Print the text and delay
        screenPrint(text, battleTextX, battleTextY, (255, 255, 255), True, font)
        pygame.time.delay(200)

        #Checking party if you have more pokemon alive
        continueTurn = False
        for i,k in enumerate(trainerPartyList):
          if k.HP > 0:
            continueTurn = True
        
        if continueTurn == True:
          bagScreen = False
          battleScreen = False
          moveScreen = False
          menuSelectD = False
          pokeScreen = True
        if continueTurn == False:

          #LOSING MONEY
          #random factor
          randNum = random.randint(90, 110) / 100
          lostMoney = round(Pokemon2.level * 20 * randNum)
          #Actually losing money
          money -= lostMoney 
          #Making sure money isn't negative
          if money < 0:
            money = 0
          
          #reset background
          self.printBattleBG(Pokemon2)
          text = "You blacked out and lost $" + str(lostMoney)
          
          #Print the text and delay
          screenPrint(text, battleTextX, battleTextY, (255, 255, 255), True, font)
          pygame.time.delay(450)
          
          #Healing the party
          for i,k in enumerate(trainerPartyList):
            k.HP = k.maxHP
            k.movePPList = k.maxPPList
          
          firstScreen = False
          moveScreen = False
          inBattle = False
          inPokecenter = True
          pokecenterRun()
          
          break
      #Beating the enemy
      if Pokemon2.HP <= 0:

        #play victory music
        backgroundMusic = pygame.mixer.music.load('victory2.mp3')
        pygame.mixer.music.play(-1)

        #reset background
        self.printBattleBG(Pokemon2)
        text = Pokemon2.name.upper() + " fainted..."

        #Print the text and delay
        screenPrint(text, battleTextX, battleTextY, (255, 255, 255), True, font)
        pygame.time.delay(200)

        self.battleVictory(Pokemon2)
          

        firstScreen = False
        moveScreen = False
        inBattle = False
        
        break
    
      #Showing the graphics 
      clock.tick(10)
      #PRINT ALL THE INFO (name, moves, health)
      self.screenCheck(Pokemon2)
      #QUIT
      for event in pygame.event.get():
        if event.type == QUIT:
          run = False
          firstScreen = False
          moveScreen = False
          inBattle = False
          pass
        
        #---------------SELECTED A MOVE AKA THE ACTUAL BATTLING - damage calculation---------------
        if selectedMove == True:
          self.moveTypeCheck(pokeMove)
          userMoveType = moveType
          
          randomSpeed = 0
          #----BOTH ARE SAME SPEED----
          if self.speedStats == Pokemon2.speedStats:
            randomSpeed = random.randint(1, 2)

          #----TRAINER IS FASTER----
          if self.speedStats > Pokemon2.speedStats or randomSpeed == 1:
            
            #Trainer turn first
            self.damageCalculation(Pokemon2, pokeMove, movePower, userMoveType, True)
            #Nice pause
            pygame.time.delay(400)

            #Breaking if enemy faints
            if Pokemon2.HP <= 0:
              break
            

            #Enemy turn second (picking random move)
            randomNum = random.randint(0, 3)
            print("RANDOM: "+ str(randomNum))
            enemyPokeMove = (Pokemon2.moves[randomNum])
            enemyMovePower = (Pokemon2.movePowerList[randomNum])
            moveIndex = randomNum
            #Checking type of move
            Pokemon2.moveTypeCheck(enemyPokeMove)
            enemyMoveType = moveType
            #Enemy damage calculation
            Pokemon2.damageCalculation(self, enemyPokeMove, enemyMovePower, enemyMoveType, False)
          

          #----TRAINER IS SLOWER----
          if self.speedStats < Pokemon2.speedStats or randomSpeed == 2:
                  
            #Enemy turn first (picking random move)
            randomNum = random.randint(0, 3)
            print("RANDOM: "+ str(randomNum))
            enemyPokeMove = (Pokemon2.moves[randomNum])
            enemyMovePower = (Pokemon2.movePowerList[randomNum])
            moveIndex = randomNum

            #Checking type of move
            Pokemon2.moveTypeCheck(enemyPokeMove)
            enemyMoveType = moveType

            #Enemy damage calculation
            Pokemon2.damageCalculation(self, enemyPokeMove, enemyMovePower, enemyMoveType, False)

            #Nice pause
            pygame.time.delay(400)

            #Breaking if user faints
            if self.HP <= 0:
              break

            #Trainer turn second
            self.damageCalculation(Pokemon2, pokeMove, movePower, userMoveType, True)
            
          randomSpeed = 0
          



#------------------------------------------------FUNCTIONS------------------------------------------------

def reprintMenuScreen(menuScreen, menuPosX, menuPosY, menu):
  global ballList
  global ballAmountList
  ballTextOffset = 67
  itemTextOffset = 67

  if menu == "bag":
    #Reprinting Bag screen
    win.blit(menuScreen, (menuPosX, menuPosY))
    ballList2 = ["Poke Ball", "Great Ball", "Ultra Ball", "Master Ball"]
    for i,k in enumerate(ballList):
      for a,z in enumerate(ballList2):
        if z == k:
          screenPrint("x" + str(ballAmountList[i]), 395, ballTextOffset, (0, 0, 0), False, font)
          screenPrint(k, 182, ballTextOffset, (0, 0, 0), False, font)
          ballTextOffset += 30
  
  if menu == "pokemart":
    #Reprinting pokemartMenu
    win.blit(menuScreen, (menuPosX, menuPosY))
    screenPrint("$" + str(money), 68, 88, (0, 0, 0), False, font)
    for i,k in enumerate(martList):
      screenPrint(k.upper(), 182, itemTextOffset, (0, 0, 0), False, font)
      screenPrint("$" + str(martPriceList[i]), 350, itemTextOffset, (0, 0, 0), False, font)
      itemTextOffset += 29

  screenPrint("Press 'S' to exit", 10, 370, (255, 255 ,255), False, font2)
       
#POKEMON MENU REPRINTING BACKGROUND
def pokeScreenBGPrint(menuScreen, menuPosX, menuPosY, pokeNameOffset):
  #Reprinting menu
  win.blit(pokemonMenu, (0, 0))
  for i,k in enumerate(trainerPartyList):
    if i != 0:
      win.blit(menuScreen, (menuPosX, menuPosY))
      screenPrint(k.name.upper(), 215, pokeNameOffset + 5, (255, 255, 255), False, font3)
      screenPrint(str(k.level), 264, pokeNameOffset + 25, (255, 255, 255), False, font3)       
      screenPrint(str(k.HP), 380, pokeNameOffset + 25, (255, 255, 255), False, font3)
      screenPrint(str(k.maxHP), 410, pokeNameOffset + 25, (255, 255, 255), False, font3)
      menuPosY += 45
      pokeNameOffset += 45
    else:
      win.blit(pokeSubMenu1, (3, 86))
      screenPrint(k.name.upper(), 58, 119, (255, 255, 255), False, font3)
      screenPrint(str(k.level), 92, 137, (255, 255, 255), False, font3)       
      screenPrint(str(k.HP), 99, 171, (255, 255, 255), False, font3)
      screenPrint(str(k.maxHP), 124, 171, (255, 255, 255), False, font3)
  pygame.display.update()
  pygame.time.delay(30)

#HP Animation
def HPAnimation(healthRatio, barPosX, barPosY, barLength):
  global run
  global firstScreen
  global moveScreen
  global inBattle
  global FPS
  

  #Getting the new Bar Length
  minBarLength = round(healthRatio * 87)
  

  if minBarLength > barLength:
    minBarLength = barLength

  #HEALTH BAR LENGTH deficit
  lengthDeficit = round((barLength - minBarLength) / 20)
  if lengthDeficit < 1:
    lengthDeficit = 1
  drawing = True
  while drawing == True:

    #QUIT
    for event in pygame.event.get():
      if event.type == QUIT:
        run = False
        firstScreen = False
        moveScreen = False
        inBattle = False
        drawing = False
        pass
  
    barLength -= (lengthDeficit)
    barRatio = barLength / 87
    #Breaking the loop if bar length is negative or less than the desired outcome
    if barLength <= 0 or barLength <= minBarLength:
      barLength = 0
      pygame.draw.rect(win, (72, 72, 72), (barPosX, barPosY, 87, 7))
      drawing = False
      break
    #Changing the colour
    if barRatio >= 0.5:
      #Green
      healthColour = (101, 242, 157)
    #health is less than half or more than one fifth
    elif barRatio < 0.5 and healthRatio > 0.2:
      #Yellow
      healthColour = (250, 225, 45)
    #Health is less than a fifth
    else:
      #Red
      healthColour = (246, 78, 45)
    
    pygame.draw.rect(win, (72, 72, 72), (barPosX, barPosY, 87, 7))
    pygame.draw.rect(win, healthColour, (barPosX, barPosY, barLength, 7))
    pygame.display.update()
    pygame.time.delay(10)

#PRINTING TEXT ON SCREEN
def screenPrint(text, x, y, colour, delay, fontType):
  if fontType == font3:
    shadowLength = 1
  if fontType == font2:
    shadowLength = 1
  if fontType == font:
    shadowLength = 2

  if colour == (255, 255, 255):
    shadowColour = (115, 115, 116)
  elif colour == (0, 0, 0):
    colour = (96, 97, 96)
    shadowColour = (208, 208, 200)
  else:
    shadowColour = (208, 208, 200)

  if delay == True:
    delayedText = ""
    for char in text:
      delayedText += char
      printText = fontType.render(delayedText, 1, colour)
      printShadow = fontType.render(delayedText, 1, shadowColour)
      win.blit(printShadow, (x + shadowLength, y + shadowLength))
      win.blit(printText, (x, y))
      pygame.display.update()
      pygame.time.delay(30)
  
  else:
    printText = fontType.render(text, 1, colour)
    printShadow = fontType.render(text, 1, shadowColour)
    win.blit(printShadow, (x + shadowLength, y + shadowLength))
    if shadowLength == 1:
      win.blit(printShadow, (x + 2, y + 2))
    win.blit(printText, (x, y))
    #pygame.display.update()

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
  global menuSelectP
  global ruleScreen

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

  #PRESSING P (Getting a Pikachu) - secret code
  if keys[pygame.K_p]:
    #No holding check
    if keyCount < 1:
      selectButtonSFX.play()
      menuSelectP = True
    if keyCount > 0:
      menuSelectP = False
    keyCount +=1

  else: 
    keyCount = 0
    menuSelectP = False

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
  global FPS

  #Running selectMenu
  selectMenuRun = True
  while selectMenuRun == True:
    clock.tick(FPS)
    #QUIT
    for event in pygame.event.get():
      if event.type == QUIT:
        talk = False
        inPokecenter = False
        inPokemart = False
        selectMenuRun == False
        run = False
        pygame.quit()

      
    #Adding the menu / resetting code
    win.blit(selectMenuType, (menuPosX, menuPosY))
    win.blit(Pointer2, (menuPosX + P_offsetX, menuPosY + P_offsetY))
    #if inBattle == False:
      #win.blit(textBox, (0, 0))
      #win.blit (textSentence, (textPosX, textPosY))
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
          pass
          #redrawGameWindow(background)
        else:
          win.blit(background, (0,0))

      if selectDown == True:
        selectYes = False
        selectMenuRun = False
        if inBattle == False:
          pass
          #redrawGameWindow(background)
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

      #Selecting no
      if selectYes == False:
        win.blit(textBox, (0, 0))
        text = textList[maxTextCount - 1]
        textSentence = font.render(text, 1, (0, 0, 0))
        win.blit (textSentence, (textPosX, textPosY))
        pygame.display.update()
        #pygame.time.delay(500)
        talk = False
        

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

#MAP / SPRITE REDRAW
def redrawGameWindow(background): 
  global walkCount
  global charPosX
  global charPosY
  global lastPos
  global inPokecenter
  global inPokemart

  win.blit(background, (0,0))

  if walkCount + 1 > 9:
    walkCount = 0

  if left:
    win.blit(walkLeft[walkCount // 3], (charPosX,charPosY))
    walkCount +=1

  elif right:
    win.blit(walkRight [walkCount // 3], (charPosX,charPosY))
    walkCount += 1

  elif up:
    if walkCount >= 6:
      walkCount = 0

    win.blit(walkUp[walkCount // 3], (charPosX,charPosY))
    walkCount += 1

  elif down:
    if walkCount >= 6:
      walkCount = 0
      
    win.blit(walkDown[walkCount // 3], (charPosX,charPosY))
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
  
  #displaying message for rules
  if rulesCount == 0:
    if inPokecenter == False and inPokemart == False:
      screenPrint("Press 'R' for RULES", 5, 365, (255, 255, 255), False, font2)
    elif inPokemart == True:
      pass
    else:
      screenPrint("Press 'R' for RULES", 7, 27, (255, 255, 255), False, font2)

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
  global selectYes

  win.blit(walkUp[0], (charPosX,charPosY))
  pygame.display.update()

  backgroundMusic = pygame.mixer.music.load('Pokecenter music2.mp3')
  pygame.mixer.music.play(-1)
  firstRun = True
  talkCount = 0
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
              
    #Resetting talking
    if (talkCount > 0):
      keySelectD = False
      menuSelectD = False
      talkCount = 0
    
    #talking to Nurse joy
    if keySelectD == True and (charPosX >= 203 and charPosX <= 220 and charPosY <= 161):
      #Displaying the first message
      selectButtonSFX.play()
      textUp = "WELCOME to the POKEMON CENTER!"
      textDown = ""
      win.blit(textBox, (0, 0))
      pygame.display.update()

      screenPrint(textUp, textPosX, textPosY, (0, 0, 0), True, font)
      screenPrint(textDown, textPosX, textPosY + 25, (0, 0, 0), True, font)

      talk = True
      talkCount = 0
      menuSelectD = False
      offset = 0
      offsetNum = 1

      while talk == True:
        clock.tick(FPS)
        keysInputMenu()

        pygame.draw.rect(win, (255, 255, 255), (textPosX + 380, textPosY - 5, 22, 55))
        win.blit(textPointer, (textPosX + 380, textPosY + 5 + offset))
        pygame.display.update()
        offset += offsetNum
        if offset == 5:
          offsetNum = -1
        if offset == -5:
          offsetNum = 1

        #QUIT
        for event in pygame.event.get():
            if event.type == QUIT:
                inPokecenter = False
                run = False
                talk = False

        if menuSelectD == True:
          talkCount += 1
          menuSelectD = False

        if talkCount == 1:
          win.blit(textBox, (0, 0))
          pygame.display.update()
          textUp = "Would you like to heal your"
          textDown = "POKEMON?"
          screenPrint(textUp, textPosX, textPosY, (0, 0, 0), True, font)
          screenPrint(textDown, textPosX, textPosY + 25, (0, 0, 0), True, font)

          selectMenu(pokecenterBG, selectMenuYN, selectMenuPosX, selectMenuPosY, pointerOffsetX, pointerOffsetY)
        
          if selectYes == True:
            #Nurse joy dialogue if trainer wishes to heal pokemon
            redrawGameWindow(pokecenterBG)
            win.blit(textBox, (0, 0))
            pygame.display.update()
            textUp = "Okay, I'll just take your POKEMON"
            textDown = "for a few seconds..."
            screenPrint(textUp, textPosX, textPosY, (0, 0, 0), True, font)
            screenPrint(textDown, textPosX, textPosY + 25, (0, 0, 0), True, font)
            #Healing animation / SFX
            healingSFX.play()
            pygame.time.delay(500)

            #Actual healing
            for i,k in enumerate(trainerPartyList):
              k.HP = k.maxHP
              k.movePPList = k.maxPPList
              print(k.name + " HP: " + str(k.HP))

            #Finsihed healing - Nurse Joy dialogue 2
            win.blit(textBox, (0, 0))
            pygame.display.update()
            textUp = "We've restored your POKEMON"
            textDown = "to full health!"
            screenPrint(textUp, textPosX, textPosY, (0, 0, 0), True, font)
            screenPrint(textDown, textPosX, textPosY + 25, (0, 0, 0), True, font)
            pygame.time.delay(500)

          #Nurse joy dialogue 3
          win.blit(textBox, (0, 0))
          pygame.display.update()
          textUp = "Thanks for coming!"
          screenPrint(textUp, textPosX, textPosY, (0, 0, 0), True, font)
          pygame.time.delay(350)
          talk = False
          keySelectD = False
          menuSelectD = False             
          
       
        

    #walking out of pokecenter
    if (charPosX >= 199 and charPosX <= 221) and charPosY >= 302:
      inPokecenter = False
      backgroundMusic = pygame.mixer.music.load('Pokemon route 1 music2.mp3')
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
  global menuSelectS
  global selectYes
  global keySelectD
  global selectUp
  global selectDown
  global textCount
  global ballAmountList
  global ballList
  global money

  global bagScreen
  global battleScreen

  global coinMultiplier
  global levelAdd
  
  win.blit(walkUp[0], (charPosX,charPosY))
  pygame.display.update()

  backgroundMusic = pygame.mixer.music.load('Pokecenter music2.mp3')
  pygame.mixer.music.play(-1)
  firstRun = True
  talkCount = 0

  
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
    if (talkCount > 0):
      keySelectD = False
      menuSelectD = False
      talkCount = 0
    
    #--------------------TALKING TO THE POKEMART NPC--------------------
    if keySelectD == True and (charPosX <= 180 and (charPosY >= 148 and charPosY <= 175)) and lastPos == "left":

      #Displaying the first message
      selectButtonSFX.play()
      textUp = "WELCOME to the POKEMART!"
      textDown = ""
      win.blit(textBox, (0, 0))
      pygame.display.update()

      screenPrint(textUp, textPosX, textPosY, (0, 0, 0), True, font)
      screenPrint(textDown, textPosX, textPosY + 25, (0, 0, 0), True, font)

      talk = True
      talkCount = 0
      menuSelectD = False
      offset = 0
      offsetNum = 1

      while talk == True:
        clock.tick(FPS)
        keysInputMenu()

        #Displaying moving pointer
        pygame.draw.rect(win, (255, 255, 255), (textPosX + 380, textPosY - 5, 22, 55))
        win.blit(textPointer, (textPosX + 380, textPosY + 5 + offset))
        pygame.display.update()
        #Animating the pointer
        offset += offsetNum
        if offset == 5:
          offsetNum = -1
        if offset == -5:
          offsetNum = 1
          
        #QUIT
        for event in pygame.event.get():
          if event.type == QUIT:
            inPokemart = False
            run = False
            talk = False

        if menuSelectD == True:
          win.blit(textBox, (0, 0))
          pygame.display.update()
          textUp = "Would you like to buy?"
          textDown = ""
          screenPrint(textUp, textPosX, textPosY, (0, 0, 0), True, font)
          screenPrint(textDown, textPosX, textPosY + 25, (0, 0, 0), True, font)
          selectUp = True
          selectMenu(pokemartBG, selectMenuYN, selectMenuPosX, selectMenuPosY, pointerOffsetX, pointerOffsetY)
          menuSelectD = False
          
          #----------POKEMART MENU----------
          if selectYes == True:
            # Resetting variables
            shopScreen = True
            firstTime = True
            itemIndex = 0
            selectingItem = False
            menuSelectD = False
            DCount = 0
            itemAmount = 1
            boughtItem = False
            menuSelectD = False
            # Actual loop
            while shopScreen == True:
              clock.tick(FPS)
              #QUIT
              for event in pygame.event.get():
                if event.type == QUIT:
                  run = False
                  battleScreen = False
                  shopScreen = False
                  moveScreen = False
                  inBattle = False
                  pygame.quit()
                  
              keysInputMenu()
              #Resetting variables
              menuScreen = pokemartMenu
              menuPosX = 0
              menuPosY = 0
              amountX = 246
              amountY = 214
              priceX = amountX + 87
              priceY = amountY
              P_offsetX = 167
              P_offsetY1 = 70
              P_offsetY2 = 101
              P_offsetY3 = 133
              P_offsetY4 = 163
              P_offsetY5 = 190
              P_offsetY6 = 218
              itemTextOffset = 67

              pointerOffsetList = [P_offsetY1, P_offsetY2, P_offsetY3, P_offsetY4, P_offsetY5, P_offsetY6]
              
              #First time reset
              if firstTime == True:
                #Reprinting menu
                P_offsetY = P_offsetY1
                redrawGameWindow(pokemartBG)
                win.blit(menuScreen, (menuPosX, menuPosY))
                screenPrint("$" + str(money), 68, 88, (0, 0, 0), False, font)
                for i,k in enumerate(martList):
                  screenPrint(k.upper(), 182, itemTextOffset, (0, 0, 0), False, font)
                  screenPrint("$" + str(martPriceList[i]), 350, itemTextOffset, (0, 0, 0), False, font)
                  itemTextOffset += 29
                
                firstTime = False
                
              itemType = martList[itemIndex]

              #---MOVING CURSOR---
              #Moving cursor up
              if selectUp == True and P_offsetY != P_offsetY1 and selectingItem == False:
                #Reprinting menu
                reprintMenuScreen(menuScreen, menuPosX, menuPosY, "pokemart")
                #Raising the pointer
                itemIndex -= 1
                selectUp = False   
              
              #Moving cursor down
              if selectDown == True and P_offsetY != P_offsetY6 and selectingItem == False:
                #Reprinting menu
                reprintMenuScreen(menuScreen, menuPosX, menuPosY, "pokemart")

                #Lowering the pointer
                itemIndex += 1
                selectDown = False

              #Display the pointer
              if selectingItem == False:
                P_offsetY = pointerOffsetList[itemIndex]
                win.blit(Pointer2, (menuPosX + P_offsetX, menuPosY + P_offsetY))
                pygame.display.update()
              
              #Selecting how many items wanted
              #Going up
              if selectUp == True and selectingItem == True and ((itemAmount < 100) and (money >= (itemAmount + 1) * martPriceList[itemIndex])):
                itemAmount += 1
                win.blit(martSubMenu, (225, 171))
                screenPrint("x" + str(itemAmount), amountX, amountY, (0, 0, 0), False, font)
                screenPrint("$" + str(itemAmount * martPriceList[itemIndex]), priceX, priceY, (0, 0, 0), False, font)
                pygame.display.update()
                selectUp = False  

              #Going down
              if selectDown == True and selectingItem == True and itemAmount > 1:
                itemAmount -= 1
                win.blit(martSubMenu, (225, 171))
                screenPrint("x" + str(itemAmount), amountX, amountY, (0, 0, 0), False, font)
                screenPrint("$" + str(itemAmount * martPriceList[itemIndex]), priceX, priceY, (0, 0, 0), False, font)
                pygame.display.update()
                selectDown = False                

              #SELECTING AN ITEM
              if menuSelectD == True:
                #Buying items
                if selectingItem == True:
                  #Adding item to bag if not there already
                  alreadyHad = False
                  for i,k in enumerate(ballList):
                    if itemType == k:
                      ballAmountList[i] += itemAmount
                      alreadyHad = True
                  #Just adding amount if already have the item
                  if alreadyHad == False:
                    ballList += [itemType]
                    ballAmountList += [itemAmount]
                  
                  for i,k in enumerate(ballList):
                    print(k + " x" + str(ballAmountList[i]))
                  money -= itemAmount * martPriceList[itemIndex]
                  win.blit(textBox, (0, -47))
                  pygame.display.update()
                  textUp = "You bought " + str(itemAmount) + " " + itemType.upper() + "s!"
                  screenPrint(textUp, textPosX, textPosY - 47, (0, 0, 0), True, font)
                  pygame.time.delay(450)

                  #Buying LUCKY EGG
                  if itemType == "Lucky Egg":
                    levelAdd += 1
                  
                  #Buying Amulet coin
                  if itemType == "Amulet Coin":
                    coinMultiplier += 1
                    

                  #Reprinting menu
                  reprintMenuScreen(menuScreen, menuPosX, menuPosY, "pokemart")
                  pygame.display.update()
                  menuSelectD = False
                  selectingItem = False
                  boughtItem = True
                  

                if DCount == 0:
                  #Selecting an item
                  if money >= martPriceList[itemIndex]:
                    selectingItem = True
                    win.blit(martSubMenu, (225, 171))
                    screenPrint("x" + str(itemAmount), amountX, amountY, (0, 0, 0), False, font)
                    screenPrint("$" + str(itemAmount * martPriceList[itemIndex]), priceX, priceY, (0, 0, 0), False, font)
                    pygame.display.update()
                    DCount +=1
                    menuSelectD = False

                  #If the user has not enough money
                  else:
                    win.blit(textBox, (0, -47))
                    pygame.display.update()
                    textUp = "You don't have enough money to"
                    textDown = "buy this item..."
                    screenPrint(textUp, textPosX, textPosY - 47, (0, 0, 0), True, font)
                    screenPrint(textDown, textPosX, textPosY + 25 - 47, (0, 0, 0), True, font)
                    pygame.time.delay(450)

                    #Reprinting menu
                    reprintMenuScreen(menuScreen, menuPosX, menuPosY, "pokemart")
                    pygame.display.update()
                    menuSelectD = False
                                    
                if DCount == 2:
                  selectingItem = False

                #Resetting if item is bought
                if boughtItem == True:
                  DCount = 0
                  boughtItem = False

              #Going back
              if menuSelectS == True:
                if selectingItem == False:
                  redrawGameWindow(pokemartBG)
                  shopScreen = False
                  menuSelectS = False
                  menuSelectD = False
                else:
                  #Reprinting menu
                  reprintMenuScreen(menuScreen, menuPosX, menuPosY, "pokemart")

                  selectingItem = False
                  menuSelectS = False
                  DCount = 0
                  menuSelectD = False
                  itemAmount = 1
                  selectUp = False
                  selectDown = False
              

            talkCount = 3
                 
          else:
            talkCount = 3
                
        if talkCount == 3:
          #Pokemart guy dialogue 3
          win.blit(textBox, (0, 0))
          pygame.display.update()
          textUp = "Thanks for coming!"
          screenPrint(textUp, textPosX, textPosY, (0, 0, 0), True, font)
          pygame.time.delay(350)
          talk = False
          keySelectD = False
          menuSelectD = False

    #EXITING POKEMART
    if (charPosX >= 165 and charPosX <= 192) and charPosY >= 306:
      inPokemart = False
      backgroundMusic = pygame.mixer.music.load('Pokemon route 1 music2.mp3')
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
  global keySelectW
  global battleScreen 
  global pokeScreen
  global rulesCount
  charStep = False

  if keys[pygame.K_d]:
    keySelectD = True
  else:
    keySelectD = False
    menuSelectD = False
  
  if keys[pygame.K_w]:
    keySelectW = True
    pokeScreen = True
    battleScreen = False
    battlingPokemon.screenCheck(Pikachu)
  else:
    keySelectW = False
  
  if keys[pygame.K_r]:
    selectButtonSFX.play()
    rulesCount += 1
    rules()
  
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

#RULES
def rules():
  global run
  global startUp
  global menuSelectD
  global menuSelectS
  global selectUp
  global selectDown
  global selectRight
  global selectLeft
  global ruleScreen

  menuScreen = rulesMenu
  ruleScreen = True
  count = 0
  while ruleScreen == True:
    clock.tick(10)
    
    #QUIT
    for event in pygame.event.get():
        if event.type == QUIT:
            startUp = False
            run = False
            ruleScreen = False
            pygame.quit()

    # Displaying screen
    win.blit(menuScreen, (0,0))
    pygame.display.update()

    # INPUT
    keysInputMenu()
    menuScreenList = [rulesMenu, controlsMenu, tipsMenu]
    # Going to controls menu or back to rules menu
    if selectRight == True:
      if count < 2:
        count += 1
      menuScreen = menuScreenList[count]
      selectRight = False

    print(count)
    if selectLeft == True:
      if count > 0:
        count -= 1
      menuScreen = menuScreenList[count]
      selectLeft = False

    #Going back
    if menuSelectS == True:
      ruleScreen = False

#COMPLETING POKEDEX
def completedPokedexScreen():
  music = pygame.mixer.music.load('pokedexDone.mp3')
  pygame.mixer.music.play(-1)

  win.blit(pokedexGraphic, (0,0))
  pygame.display.update()
  pokedexScreen = True

  while pokedexScreen == True:
    clock.tick(FPS)

    #QUIT
    for event in pygame.event.get():
        if event.type == QUIT:
            pokedexScreen = False
            pygame.quit()
    # Pressing D to exit
    keysInputMenu()
    if menuSelectS == True:
      pokedexScreen == False
      redrawGameWindow(bg)
      music = pygame.mixer.music.load('Pokemon route 1 music2.mp3')
      pygame.mixer.music.play(-1)
      break



#-----------------POKEMON-----------------
wildLevel = 5
Pikachu = pokemon("Pikachu", "Electric", "", ["quick attack", "Thunderbolt", "Thundershock", "Tackle"], [40, 65, 40, 50], [30, 10, 30, 35], [30, 10, 30, 35], 55, 30, 35, 90, wildLevel, 190)
Charmander = pokemon("Charmander", "Fire", "", ["Tackle", "Ember", "Scratch", "Growl"], [50, 40, 40, 0], [35, 25, 35, 40], [35, 25, 35, 40], 55, 30, 35, 65, wildLevel, 190)
Charmeleon = pokemon("Charmeleon", "Fire", "", ["Flamethrower", "Ember", "Scratch", "Tackle"], [90, 40, 40, 50], [35, 25, 35, 40], [35, 25, 35, 40], 55, 30, 35, 65, wildLevel, 190)
Bulbasaur = pokemon("Bulbasaur", "Grass", "Poison", ["Tackle", "Razor leaf", "Leaf storm", "Growl"], [50, 55, 75, 0], [35, 25, 5, 40], [35, 25, 5, 40], 55, 30, 35, 45, wildLevel, 190)
Squirtle = pokemon("Squirtle", "Water", "", ["Tackle", "Bubble", "Scratch", "Growl"], [50, 40, 40, 0], [35, 30, 35, 40], [35, 30, 35, 40], 48, 65, 44, 43, wildLevel, 190)

wildPokemonList = [Pikachu, Charmander, Bulbasaur, Squirtle]
trainerPokemon = Bulbasaur
#--------------------STARTUP--------------------
run = True
startUp = True
pointerX = 74
pointerY = 170
selectIndex = 1
pointerXList = [74, 195, 330]
count = 0
offset = 0
offsetNum = 1
backgroundMusic = pygame.mixer.music.load('opening2.mp3')
pygame.mixer.music.play(-1)

while startUp:
  clock.tick(FPS)
    
  #QUIT
  for event in pygame.event.get():
      if event.type == QUIT:
          startUp = False
          run = False
          pygame.quit()

  win.blit(openingScreen, (0,0))
  win.blit(textPointer, (pointerX, pointerY + offset))
  pygame.display.update()

  #Pointer Animation
  offset += offsetNum
  if offset == 5:
    offsetNum = -1
  if offset == -5:
    offsetNum = 1

  
  # INPUT
  keysInputMenu()
  
  # Going right
  if selectRight == True and selectIndex < 3:
    selectIndex += 1
    pointerX = pointerXList[selectIndex - 1]
    selectRight = False
  # Going left
  if selectLeft == True and selectIndex > 1:
    selectIndex -= 1
    pointerX = pointerXList[selectIndex - 1]
    selectLeft = False

  # SELECTING A POKEMON
  if menuSelectD == True:
    startUp = False
    menuSelectD = False
    #Actually giving the user the pokemon they choose
    if selectIndex == 1:
      trainerPokemon = pokemon("Bulbasaur", "Grass", "Poison", ["Tackle", "Razor leaf", "Leaf storm", "Growl"], [50, 55, 75, 0], [35, 25, 5, 40], [35, 25, 5, 40], 55, 30, 35, 45, wildLevel, 190)

    if selectIndex == 2:
      trainerPokemon = pokemon("Charmander", "Fire", "", ["Tackle", "Ember", "Scratch", "Growl"], [50, 40, 40, 0], [35, 25, 35, 40], [35, 25, 35, 40], 55, 30, 35, 65, wildLevel, 190)

    if selectIndex == 3:
      trainerPokemon = pokemon("Squirtle", "Water", "", ["Tackle", "Bubble", "Scratch", "Growl"], [50, 40, 40, 0], [35, 30, 35, 40], [35, 30, 35, 40], 48, 65, 44, 43, wildLevel, 190)

  if menuSelectP == True:
    trainerPokemon = pokemon("Pikachu", "Electric", "", ["quick attack", "Thunderbolt", "Thundershock", "Tackle"], [40, 65, 40, 50], [30, 10, 30, 35], [30, 10, 30, 35], 55, 30, 35, 90, wildLevel, 190)
    menuSelectP = False
    startUp = False

trainerPartyList = [trainerPokemon]
battlingPokemon = trainerPokemon

win.blit(textBox, (0,0))
pygame.display.update()
screenPrint("You chose " + trainerPokemon.name + "!", textPosX, textPosY, (0, 0, 0), True, font)
pygame.time.delay(1000)

rules()
backgroundMusic = pygame.mixer.music.load('Pokemon route 1 music2.mp3')
pygame.mixer.music.play(-1)
#Adding pokemon to the pokedex
pokedexList += [trainerPokemon.name]

#------------------------------------------------MAIN LOOP------------------------------------------------
while run:
  global wildPokemon
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
    backgroundMusic = pygame.mixer.music.load('Battle music2.mp3')
    pygame.mixer.music.play(-1)
    pygame.time.delay(1000)

    #Random pokemon generator
    pokeList = [Bulbasaur, Charmander, Squirtle, Pikachu]
    pokeRandNum = random.randint(0, 3)
    wildPokemon = pokeList[pokeRandNum]

    wildLevel = random.randint(trainerPokemon.level - 3, trainerPokemon.level)
    if trainerPokemon.level > 7:
      wildLevel = random.randint(trainerPokemon.level - 5, trainerPokemon.level)

    #Might just need to make a function to create a new pokemon
    if wildPokemon.name == "Pikachu":
      wildPokemon = pokemon("Pikachu", "Electric", "", ["quick attack", "Thunderbolt", "Thundershock", "Tackle"], [40, 65, 40, 50], [30, 10, 30, 35], [30, 10, 30, 35], 55, 30, 35, 90, wildLevel, 190)
    if wildPokemon.name == "Bulbasaur":
      wildPokemon = pokemon("Bulbasaur", "Grass", "Poison", ["Tackle", "Razor leaf", "Leaf storm", "Growl"], [50, 55, 75, 0], [35, 25, 5, 40], [35, 25, 5, 40], 55, 30, 35, 45, wildLevel, 190)
    if wildPokemon.name == "Charmander":
      wildPokemon = pokemon("Charmander", "Fire", "", ["Tackle", "Ember", "Scratch", "Growl"], [50, 40, 40, 0], [35, 25, 35, 40], [35, 25, 35, 40], 55, 30, 35, 65, wildLevel, 190)
    if wildPokemon.name == "Squirtle":
      wildPokemon = pokemon("Squirtle", "Water", "", ["Tackle", "Bubble", "Scratch", "Growl"], [50, 40, 40, 0], [35, 30, 35, 40], [35, 30, 35, 40], 48, 65, 44, 43, wildLevel, 190)

    battlingPokemon.fight(wildPokemon)
    encounter = False
    encounterRate = 100
    backgroundMusic = pygame.mixer.music.load('Pokemon route 1 music2.mp3')
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
  
  #COMPLETING THE POKEDEX
  if completedPokedex == False:
    for i,k in enumerate(pokedexList):
      if i == 3:
        completedPokedex = True
        completedPokedexScreen()

pygame.quit()