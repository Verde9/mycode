#!/usr/bin/python3

from instructions import showInstructions
import time
from soul import Soulstepper
from enemy import Enemy
from boss import Boss

enemy = Enemy()
player = Soulstepper()
boss = Boss()


def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Main Street' : {
                  'west' : 'Treble Pkwy',
                  'east'  : 'Bass Circle',
                },

            'Treble Pkwy' : {
                  'east' : 'Main Street',
                  'north': 'Riff Runway',
                  'enemy': 'Break Dancer',
                  'item' : 'health kit',
                },
            'Bass Circle' : {
                  'west' : 'Main Street',
                  'south': 'Riff Runway',
                  'enemy': 'Break Dancer',
                  'item' : 'health kit',
               },
            'Riff Runway' : {
                  'south' : 'Treble Pkwy',
                  'north' : 'Bass Circle',
                  'boss' : 'LoVibe'
               }
         }


def enemyFight(player, enemy):
  print("You encountered a " + rooms[currentRoom]["enemy"] + " and they want to dance!!")
  print()
  dance_moves = ["Hustle", "Bus Stop", "Michael Jackson Robot", "Funky Chicken"]
  
  currentEnemy = rooms[currentRoom]["enemy"]

  while enemy.get_health() > 0:

      print('''
      Pick a number to select a dance move:
      0. The Hustle
      1. Bus Stop
      2. Michael Jacson Robot
      3. Funky Chicken ''')
      print()

      userChoice = input('>')

      if int(userChoice) == 0:
        print(f"Soulstepper hit em with the {dance_moves[0]} !")
        print()
        time.sleep(1.5)
        enemy.decrease_health()
        enemy.enemyDance(player, currentEnemy)
        print(f"{currentEnemy} was felt the soul, and there current health is {enemy.get_health()} !")
        print()
        time.sleep(1.5)
      elif int(userChoice) == 1:
        print(f"Soulstepper broke out the {dance_moves[1]} !")
        print()
        time.sleep(1.5)
        enemy.decrease_health()
        enemy.enemyDance(player, currentEnemy)
        print(f"{currentEnemy} got hit by the bus, and there current health is {enemy.get_health()} !")
        print()
        time.sleep(1.5)
      elif int(userChoice) == 2:
        print(f"Soulstepper took it back to the 70's with the {dance_moves[2]} !")
        print()
        time.sleep(1.5)
        enemy.decrease_health()
        enemy.enemyDance(player, currentEnemy)
        print(f"{currentEnemy} got hit by little Michael's spirit, and there current health is {enemy.get_health()} !")
        print()
        time.sleep(1.5)
      elif int(userChoice) == 3:
        print(f"Soulstepper was feeling a little weird and did the {dance_moves[3]} !")
        print()
        time.sleep(1.5)
        enemy.decrease_health()
        enemy.enemyDance(player, currentEnemy)
        print(f"{currentEnemy} got pecked by the chicken, and there current health is {enemy.get_health()} !")
        print()
        time.sleep(1.5)
      else:
        continue 

      if enemy.get_health() == 0:   
        print()
        print(f"You defeated {currentEnemy} and can now move on! ")
      elif player.get_health() == 0:
        break


def finalBattle(player, boss):
      print("Awesome! you found your wife Melody but oh no...")
      print()
      time.sleep(1.5)
      print(f"It looks like {rooms[currentRoom]['boss']} is holding her captive")
      print()
      time.sleep(1.5)
      print("He challenges you to the ultimate dance off to free her !")
      print()
      time.sleep(1.5)
      dance_moves = ["Hustle", "Bus Stop", "Michael Jackson Robot", "Funky Chicken"]
    
      currentEnemy = rooms[currentRoom]["boss"]

      while boss.get_health() > 0:
        print('''
        Pick a number to select a dance move:
        0. The Hustle
        1. Bus Stop
        2. Michael Jacson Robot
        3. Funky Chicken ''')
        print()

        userChoice = input('>')

        if int(userChoice) == 0:
          print(f"Soulstepper hit em with the {dance_moves[0]} !")
          print()
          time.sleep(1.5)
          boss.decrease_health()
          boss.bossDance(player, currentEnemy)
          print(f"{currentEnemy} was felt the soul, and there current health is {boss.get_health()} !")
          print()
          time.sleep(1.5)
        elif int(userChoice) == 1:
          print(f"Soulstepper broke out the {dance_moves[1]} !")
          print()
          time.sleep(1.5)
          boss.decrease_health()
          boss.bossDance(player, currentEnemy)
          print(f"{currentEnemy} got hit by the bus, and there current health is {boss.get_health()} !")
          print()
          time.sleep(1.5)
        elif int(userChoice) == 2:
          print(f"Soulstepper took it back to the 70's with the {dance_moves[2]} !")
          print()
          time.sleep(1.5)
          boss.decrease_health()
          boss.bossDance(player, currentEnemy)
          print(f"{currentEnemy} got hit by little Michael's spirit, and there current health is {boss.get_health()} !")
          print()
          time.sleep(1.5)
        elif int(userChoice) == 3:
          print(f"Soulstepper was feeling a little weird and did the {dance_moves[3]} !")
          print()
          time.sleep(1.5)
          boss.decrease_health()
          boss.bossDance(player, currentEnemy)
          print(f"{currentEnemy} got pecked by the chicken, and there current health is {boss.get_health()} !")
          print()
          time.sleep(1.5)
        else:
          continue  

        if boss.get_health() == 0:   
          break
        elif player.get_health() == 0:
          break              






#start the player in the Hall
currentRoom = 'Main Street'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  if "enemy" in rooms[currentRoom]:
      enemyFight(player, enemy)
      if player.get_health() == 0:
        print()
        print("SoulStepper Died, game over!")
        break
      else:
        del rooms[currentRoom]['enemy']            

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
  if move[0] == 'use' :
    if move[1] == 'health kit' or 'health' and 'health kit' or 'health' in inventory:
        print("Soulstepper used the health kit")
        print()
        time.sleep(1.5)
        player.increase_health()
        print(f"Soulsteppers health has increased to {player.get_health()}")
        if 'health kit' in inventory:
          inventory.remove('health kit')
        elif 'health' in inventory:
          inventory.remove('health')  
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  ## Define how a player can win
  if currentRoom == 'Riff Runway' and 'boss':
    finalBattle(player, boss)
    if player.get_health() == 0:
        print()
        print("SoulStepper Died, game over!")
        break
    else:
      print("You kicked LoVibe's ass and got your wife back")
      print()
      time.sleep(2)
      print("Groove and soul has been restored to the city")
      print()
      time.sleep(2)
      print("GAME OVER")
      break

  