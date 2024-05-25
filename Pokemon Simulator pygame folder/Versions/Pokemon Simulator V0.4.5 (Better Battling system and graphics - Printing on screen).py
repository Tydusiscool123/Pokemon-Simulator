import pygame
import random
import math
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
battleBG = pygame.image.load('Battle background3.png')
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

#STARTER SPRITES
StarterSprite1 = pygame.image.load('Starters sprites-01.png')
StarterSprite2 = pygame.image.load('Starters sprites-02.png')
StarterSprite3 = pygame.image.load('Starters sprites-03.png')
StarterSprite4 = pygame.image.load('Starters sprites-04.png')
StarterSprite5 = pygame.image.load('Starters sprites-05.png')
StarterSprite6 = pygame.image.load('Starters sprites-06.png')
StarterSprite7 = pygame.image.load('Starters sprites-07.png')
StarterSprite8 = pygame.image.load('Starters sprites-08.png')

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


inPokecenter = False
firstRun = False
inPokemart = False
canMove = False
keySelectD = False
menuSelectD = False
menuSelectS = False
talk = False
textCount = 0
pokemon = "Charizard"
pokecenterTextList = ["Welcome to our POKEMON CENTER!", "Would you like to heal your \nPOKEMON?", "I'll take your POKEMON \nfor a few seconds...", "Weve restored your POKEMON \nto full health", "Thank you for coming!", "" ]
pokemartTextList = ["Welcome to the PokeMart!", "would you like to buy something?", "Thank you for coming!", ""]
battletextList = ["Go! Jeff", "What will \nJeff do?"]
fontSize = 10
textPosX = 29
textPosY = 326
font = pygame.font.Font('Pokemon fire red font.ttf', fontSize)
fontSize2 = 8
battleNameFont = pygame.font.Font('Pokemon fire red font.ttf', fontSize2)
keyHoldCount = 0
selectMenuPosX = 318
selectMenuPosY = 222
selectUp = True
selectDown = False
pointerOffsetY = 20
pointerOffsetX = 15
selectYes = False
firstScreen = False
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
HPAnimation = False

movePP = 0

#----------------CLASSES----------------
class pokemon(object):
    def __init__(self, name, type, type2, moves, movePowerList, movePPList, attack, defense, health, speed, level):
      self.name = name
      self.type = type
      self.type2 = type2
      self.moves = moves
      self.movePowerList = movePowerList
      self.movePPList = movePPList
      self.attack = attack
      self.defense = defense
      self.health = health
      self.level = level
      self.speed = speed

      #self.moveType = moveType
      IV = 0
      EV = 0

      #STATS
      #Max stats
      self.maxHealthPoints = math.floor(0.01 * (2 * health + IV + math.floor(0.25 * EV)) * level) + level + 10
      self.maxAttackStats = (math.floor(0.01 * (2 * attack + IV + math.floor(0.25 * EV)) * level) + 5)
      self.maxDefenseStats = (math.floor(0.01 * (2 * defense + IV + math.floor(0.25 * EV)) * level) + 5)
      self.maxSpeedStats = (math.floor(0.01 * (2 * speed + IV + math.floor(0.25 * EV)) * level) + 5)

      #Actual stats
      self.healthPoints = math.floor(0.01 * (2 * health + IV + math.floor(0.25 * EV)) * level) + level + 10
      self.attackStats = (math.floor(0.01 * (2 * attack + IV + math.floor(0.25 * EV)) * level) + 5)
      self.defenseStats = (math.floor(0.01 * (2 * defense + IV + math.floor(0.25 * EV)) * level) + 5)
      self.speedStats = (math.floor(0.01 * (2 * speed + IV + math.floor(0.25 * EV)) * level) + 5)

    #--------METHODS--------

    #REPRINT BACKGROUND
    def printBattleBG(self, Pokemon2):
      global moveScreen
      global movePP
      global lastBarLength
      #Background
      win.blit(battleBG, (0,0))

      #POKEMON SPRITES
      pokeNameList = ["Bulbasaur", "Charmander", "Squirtle", "Pikachu"]
      trainerSpriteList = [StarterSprite1, StarterSprite3, StarterSprite5, StarterSprite7]
      trainerSpritePosList = [(63, 181), (75, 163), (54, 175), (61, 160)]
      enemySpriteList = [StarterSprite2, StarterSprite4, StarterSprite6, StarterSprite8]
      enemySpritePosList = [(291,95), (298, 96), (280, 95), (303, 85)]

      #Choosing which sprite's which
      for i,k in enumerate(pokeNameList):
        #Trainer sprite
        if self.name == k:
          trainerSprite = trainerSpriteList[i]
          trainerSpritePos = trainerSpritePosList[i]
        #Enemy sprite
        if Pokemon2.name == k:
          enemySprite = enemySpriteList[i]
          enemySpritePos = enemySpritePosList[i]

    

      #Information

      #Trainer pokemon name
      trainerPokeName = ((self.name).upper())
      textTPN = battleNameFont.render(trainerPokeName, 1, (0, 0, 0))
      #Enemy pokemon name
      enemyPokeName = ((Pokemon2.name).upper())
      textEPN = battleNameFont.render(enemyPokeName, 1, (0, 0, 0))
      #Trainer pokemon level
      levelTP = ("lv" + str(self.level))
      textLevelTP = battleNameFont.render(levelTP, 1, (0, 0, 0))
      #Enemy pokemon level
      levelEP = ("lv" + str(Pokemon2.level))
      textLevelEP = battleNameFont.render(levelEP, 1, (0, 0, 0))

      #Printing all the information
      win.blit(textEPN, (25, 72))
      win.blit(textLevelEP, (149, 72))
      win.blit(textTPN, (266, 197))
      win.blit(textLevelTP, (390, 197))
      win.blit(trainerSprite, trainerSpritePos)
      win.blit(enemySprite, enemySpritePos)     

      #HEALTH
      self.healthCheck(329, 223)
      Pokemon2.healthCheck(88, 98)
      pygame.display.update()
      

    def healthCheck(self, barPosX, barPosY):
      global healthRatio
      global damageRatio
      global lastBarLength
      global HPAnimation
      #HEALTH RATIO
      healthRatio = self.healthPoints / self.maxHealthPoints

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
      lastBarLength = barLength

    #INPUT AND STUFF
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
      global movePP
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

          #Selecting RUN
          if down and right == True:
            battleScreen = False
            inBattle = False
      
      #MOVE SCREEN
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
        windowTextUp = battleNameFont.render(textUp, 1, (0, 0, 0))
        windowTextDown = battleNameFont.render(textDown, 1, (0, 0, 0))
        windowTextRU = battleNameFont.render(textRU, 1, (0, 0, 0))
        windowTextRD = battleNameFont.render(textRD, 1, (0, 0, 0))

        #Move PP
        movePPText = battleNameFont.render(str(movePP), 1, (0, 0, 0))
        
        #SELECTING A MOVE
        if menuSelectD == True:
          selectedMove = True 
          #Top left move
        if up and left == True:
          pokeMove = (self.moves[0])
          movePower = (self.movePowerList[0])
          movePP = (self.movePPList[0])
          #Top right move
        if up and right == True:
          pokeMove = (self.moves[1])
          movePower = (self.movePowerList[1])
          movePP = (self.movePPList[1])
          #Bottom left move
        if down and left == True:
          pokeMove = (self.moves[2])
          movePower = (self.movePowerList[2])
          movePP = (self.movePPList[2])
          #Bottom right move
        if down and right == True:
          pokeMove = (self.moves[3])
          movePower = (self.movePowerList[3])
          movePP = (self.movePPList[3])
        
        #MOVETYPE
        self.moveTypeCheck()
        moveTypeText = ""
        for i,char in enumerate(moveType):
          moveTypeText += char
          if i == 5:
            break
        moveTypePrint = battleNameFont.render((moveTypeText.upper()), 1, (0, 0, 0))

        #Going back to normal menu
        if menuSelectS == True:
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

      #MOVING CURSOR   
      #Going up
      if selectUp == True:
        P_offsetY = P_offsetY1
        up = True
        down = False
      #Going down
      if selectDown == True:
        P_offsetY = P_offsetY2
        down = True
        up = False
      #GOing right
      if selectRight == True:
        P_offsetX = P_offsetX2
        right = True
        left = False
      #Going left
      if selectLeft == True:
        P_offsetX = P_offsetX1
        left = True
        right = False

      #REPRINTING
      win.blit(menuScreen, (menuPosX, menuPosY))

      if moveScreen == True:
        #Display Moves
        win.blit(windowTextUp, (26, 280))
        win.blit(windowTextDown, (26, 310))
        win.blit(windowTextRU, (166, 280))
        win.blit(windowTextRD, (166, 310))
        #Display PP
        win.blit(movePPText, (412, 280))
        #Display move type
        win.blit(moveTypePrint, (360, 312))
      else:
        #Display text
        win.blit(windowTextUp, (24, 270))
        win.blit(windowTextDown, (24, 300))
      
      win.blit(Pointer2, (menuPosX + P_offsetX, menuPosY + P_offsetY))
      pygame.display.update()

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

    def moveTypeCheck(self):
      global pokeMove
      global moveType
      if pokeMove == "quick attack" or pokeMove == "Tackle" or pokeMove == "Scratch" or pokeMove == "Growl":
        moveType = "Normal"
      #ELECTRIC TYPE
      if pokeMove == "Thunder wave" or pokeMove == "Thundershock":
        moveType = "Electric"
      #FIRE TYPE
      if pokeMove == "Ember":
        moveType = "Fire"
      #GRASS TYPE
      if pokeMove == "Razor leaf" or pokeMove == "Sleep powder":
        moveType = "Grass"
      #WATER TYPE
      if pokeMove == "Bubble":
        moveType = "Water"   
        
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

      global lastBarLength
      global HPAnimation
      

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
      selectedMove = False

      #ACTUAL BATTLE  
      while inBattle == True:
        
        if self.healthPoints <= 0:
          #reset background
          self.printBattleBG(Pokemon2)
          text = self.name.upper() + " fainted..."

          #Print the text and delay
          delayPrint(text, 24, 270)
          pygame.time.delay(200)

          #reset background
          self.printBattleBG(Pokemon2)
          text = "You blacked out and lost $100"

          #Print the text and delay
          delayPrint(text, 24, 270)
          pygame.time.delay(200)


          firstScreen = False
          moveScreen = False
          inBattle = False
          break

        if Pokemon2.healthPoints <= 0:
          #reset background
          self.printBattleBG(Pokemon2)
          text = Pokemon2.name.upper() + " fainted..."

          #Print the text and delay
          delayPrint(text, 24, 270)
          pygame.time.delay(200)

          firstScreen = False
          moveScreen = False
          inBattle = False
          break
      

        selectedMove = False
        #Showing the graphics 
        clock.tick(FPS)
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

            #Text showing what move the trainer's pokemon used
            self.printBattleBG(Pokemon2)
            upperText = ((self.name).upper()) + " used"
            lowerText = (pokeMove.upper() + "!")
            delayPrint(upperText, 24, 270)
            delayPrint(lowerText, 24, 300)
            pygame.time.delay(300)

            #Checking types
            print(pokeMove)
            self.moveTypeCheck()
            
            #MOVE BASE POWERS (nah just make it a list in attributes)
            #if pokeMove == "quick attack":
              #movePower = 40
            #if pokeMove == "Tackle":
              #movePower = 50
            
            
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

            
            print(movePower)
            #DAMAGE CALCULATION
            damage = math.floor(((((((2*self.level)/5)+2) * movePower * ((self.attackStats)/Pokemon2.defenseStats))/50)+2)*critical*randomFactor*STAB*typeAdvtg)
            print("DAMAGE: " + str(damage))
            Pokemon2.healthPoints -= damage
            print("ENEMY HP: " + str(Pokemon2.healthPoints))

            #HEALTH
            damageRatio = damage / Pokemon2.maxHealthPoints            
            

            if SEffective == True or NVEffective == True:
              #reset background
              self.printBattleBG(Pokemon2)

              #Print if it was super effective
              if SEffective:
                text = "It's super effective!"
              #Print if it was not very effective
              if NVEffective:
                text = "It's not very effective..."
              
              #Print the text and delay
              delayPrint(text, 24, 270)
              pygame.time.delay(300)
            
            if criticalHit:
              #reset background
              self.printBattleBG(Pokemon2)
              text = "A critical hit!"

              #Print the text and delay
              delayPrint(text, 24, 270)
              pygame.time.delay(200)
            
            #Reset the type advantages
            SEffective = False
            NVEffective = False
            effective = False

            self.printBattleBG(Pokemon2)
            


#----------------FUNCTIONS----------------

def startUp():
  print("Welcome to the world of Pokemon!")
  print("Which pokemon would you like?")

def delayPrint(text, x, y):
  delayedText = ""
  for char in text:
    delayedText += char
    printText = font.render(delayedText, 1, (255, 255, 255))
    win.blit(printText, (x, y))
    pygame.display.update()
    pygame.time.delay(40)

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
        #pygame.time.delay(500)
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

#-----------------POKEMON-----------------
wildLevel = 5
Pikachu = pokemon("Pikachu", "Electric", "", ["quick attack", "Thunder wave", "Thundershock", "Tackle"], [40, 0, 40, 50], [30, 20, 30, 35], 55, 30, 35, 90, wildLevel)
Charmander = pokemon("Charmander", "Fire", "", ["Tackle", "Ember", "Scratch", "Growl"], [50, 40, 40, 0], [35, 25, 35, 40], 55, 30, 35, 65, wildLevel)
Bulbasaur = pokemon("Bulbasaur", "Grass", "Poison", ["Tackle", "Razor leaf", "Sleep powder", "Growl"], [50, 55, 0, 0], [35, 25, 15, 40], 55, 30, 35, 45, wildLevel)
Squirtle = pokemon("Squirtle", "Water", "", ["Tackle", "Bubble", "Scratch", "Growl"], [50, 40, 40, 0], [35, 30, 35, 40], 48, 65, 44, 43, wildLevel)

wildPokemonList = [Pikachu, Charmander, Bulbasaur, Squirtle]
ask = True
while ask == True:
  userInput = input("What pokemon do you want?")
  if userInput == "25":
    trainerPokemon = pokemon("Pikachu", "Electric", "", ["quick attack", "Thunder wave", "Thundershock", "Tackle"], [40, 0, 40, 50], [30, 20, 30, 35], 55, 30, 35, 90, wildLevel)
    ask = False
  if userInput == "1":
    trainerPokemon = pokemon("Bulbasaur", "Grass", "Poison", ["Tackle", "Razor leaf", "Sleep powder", "Growl"], [50, 55, 0, 0], [35, 25, 15, 40], 55, 30, 35, 45, wildLevel)
    ask = False
  if userInput == "2":
    trainerPokemon = pokemon("Charmander", "Fire", "", ["Tackle", "Ember", "Scratch", "Growl"], [50, 40, 40, 0], [35, 25, 35, 40], 55, 30, 35, 65, wildLevel)
    ask = False
  if userInput == "3":
    trainerPokemon = pokemon("Squirtle", "Water", "", ["Tackle", "Bubble", "Scratch", "Growl"], [50, 40, 40, 0], [35, 30, 35, 40], 48, 65, 44, 43, wildLevel)
    ask = False
  

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
        if encounterRate < 50:
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

    #Random pokemon generator
    pokemonRandNum = random.randint(0, 3)
    wildPokemon = wildPokemonList[pokemonRandNum]
    pokemonRandNum = random.randint(0, 3)
   
    trainerPokemon.fight(wildPokemon)
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