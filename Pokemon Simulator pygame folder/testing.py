
import math

class pokemon(object):
  def __init__(self, name, type, moves, attack, defense, health, speed, level, moveType):
    self.name = name
    self.type = type
    self.moves = moves
    self.attack = attack
    self.defense = defense
    self.health = health
    self.level = level
    self.speed = speed
    self.moveType = moveType
    IV = 0
    EV = 0

    #STATS
    self.HealthPoints = math.floor(0.01 * (2 * health + IV + math.floor(0.25 * EV)) * level) + level + 10
    self.attackStats = (math.floor(0.01 * (2 * attack + IV + math.floor(0.25 * EV)) * level) + 5)
    self.defenseStats = (math.floor(0.01 * (2 * defense + IV + math.floor(0.25 * EV)) * level) + 5)
    self.speedStats = (math.floor(0.01 * (2 * speed + IV + math.floor(0.25 * EV)) * level) + 5)

  def fight(self, Pokemon2):
    poop()
    self.level += 1
    Pokemon2.level += 1
    #Fighting mechanism
    typeList = ["Fire", "Water", "Grass", "Electric", "Poison", "Flying"]

    for i,k in enumerate(typeList):
      
      #Both are same 
      if self.moveType == k:
        if Pokemon2.moveType == k:
          stringAttack1 = "Its not very effective..."
          stringAttack2 = "Its not very effective..."
          notEffective = True
          
    
    #if self.moveType
      
      while (self.health > 0) and (Pokemon2.health > 0):
            
            # Print the health of each pokemon
            #PRINT ALL THE INFO (name, moves, health)
            #Print name
            #Print health
            #print moves
            #for i, x in enumerate(self.moves):
            #    print(f"{i+1}.", x)
            #index = int(input('Pick a move: '))
            #delay_print(f"\n{self.name} used {self.moves[index-1]}!")
            #time.sleep(1)
            #delay_print(string_1_attack)

        #if 

            # Determine damage
            Pokemon2.health -= self.attack

            # Add back bars plus defense boost
            
            # Check to see if Pokemon fainted
            if Pokemon2.health <= 0:
                #delay_print("\n..." + Pokemon2.name + ' fainted.')
                break

            # Pokemon2s turn

            # Determine damage
            self.health -= Pokemon2.attack

            # Add back bars plus defense boost

            # Check to see if Pokemon fainted
            if self.health <= 0:
                #delay_print("\n..." + self.name + ' fainted.')
                break

        #Money add

def poop():
   for i in range(1, 10):
      print("your mum")


    
wildLevel = 5
#----------------POKEMON----------------
    
Pikachu = pokemon("Pikachu", "Electric", ["quick attack", "Thunder wave", "Thunderbolt", "Tackle"], 55, 30, 35, 90, wildLevel, "Electric")
Charmander = pokemon("Charmander", "Fire", ["Tackle", "Ember", "Scratch", "Growl"], 55, 30, 35, 65, wildLevel, "Electric")
Bulbasaur = pokemon("Bulbasaur", "Grass", ["Tackle", "Razor leaf", "Sleep powder", "Growl"], 55, 30, 35, 45, wildLevel, "Electric")
Squirtle = pokemon("Squirtle", "Water", ["Tackle", "Bubble", "Muddy water", ""], 48, 65, 44, 43, wildLevel, "Electric")

#print("What pokemon do you want g")
trainerPokemon = pokemon("Pikachu", "Electric", ["quick attack", "Thunder wave", "Thunderbolt", "Tackle"], 55, 30, 35, 90, wildLevel, "Electric")
Pikachu.fight(Charmander)
print("Pikachu level: " + str(Pikachu.level))
print("trainer level: " + str(trainerPokemon.level))

trainerPokemon.fight(Charmander)
print("Pikachu level: " + str(Pikachu.level))
print("trainer level: " + str(trainerPokemon.level))

#STATS CALCULATOR
Base = 44
IV = 0
EV = 0
Level = 5
HealthPoints = math.floor(0.01 * (2 * Base + IV + math.floor(0.25 * EV)) * Level) + Level + 10
Base = 48
attackStats = (math.floor(0.01 * (2 * Base + IV + math.floor(0.25 * EV)) * Level) + 5)

print("HP: " + str(HealthPoints))
print("Attack: " + str(attackStats))
poo = [2, 3, 3, 4]
for i, k in enumerate(poo):
  print(i)
  if i == 4:
    poopoo = True

print(poopoo)