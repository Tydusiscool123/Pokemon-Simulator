
import pygame
import random
import subprocess
import time
import math
#initialise pygame
pygame.init()
from pygame.constants import WINDOWCLOSE
from pygame.locals import QUIT

win = pygame.display.set_mode((450, 400))
pygame.display.set_caption('Sandbox Yo')

#PRINTING TEXT
def printText(textList, textCount, colourNumber1, colourNumber2, colourNumber3, textPosX, textPosY):
  global textSentence
  text = textList[textCount]
  #textSentence = font.render(text, 1, (colourNumber1, colourNumber2, colourNumber3))
  win.blit (text, (textPosX, textPosY))
  #for char in textSentence:
        
        #font.render(text, 1, (colourNumber1, colourNumber2, colourNumber3))
        #pygame.time.delay(50)
        #pygame.display.update()

typeList = ["Fire", "Water", "Grass", "Electric", "Normal"]

for i,k in enumerate(typeList):
  



        
