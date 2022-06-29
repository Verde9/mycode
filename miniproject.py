#!/usr/bin/env python3
import time
import random

def main():

    playAgain = True

    while playAgain:
        print("HOW DISTURBING ARE YOU??")
        time.sleep(2)
        print()
        print("Let's find out by playing a game of would you rather")
        time.sleep(2)
        print()
        print("Ready? Let's play!")
        time.sleep(2)
        print()
        while(True):
           print("Question Number 1. Would you rather...")
           time.sleep(2)
           print() 
           print("a. Smell like poop all the time and not be able to smell it yourself")
           time.sleep(2)
           print()
           print("b. Have your significant other smell like poop and have to smell it all the time?")
           time.sleep(2)
           print() 
           questionOne = input("Enter either [a] or [b]: ")
           if questionOne.lower() != "a" and questionOne.lower() != "b":
               print("That's not a choice please try again")
           elif questionOne.lower() == "a":
               time.sleep(2)
               print() 
               print("Figured you pick that.. You smelled like that already")
               break
           else:
               time.sleep(2)
               print() 
               print("Smart choice.. You can just make it a long distance relationship.")
               break
        while(True):
           time.sleep(2)
           print()
           print("Question Number 2. Would you rather...") 
           time.sleep(2)
           print() 
           print("a. Lick a homeless man’s toe while passionately looking into their eyes for 3 hours?")
           time.sleep(2)
           print()
           print("b. Chew a piece of gum you found on the floor of a gas station bathroom for the rest of the day?")
           time.sleep(2)
           print()
           questionOne = input("Enter either [a] or [b]: ")
           if questionOne.lower() != "a" and questionOne.lower() != "b":
               print("That's not a choice please try again")
           elif questionOne.lower() == "a":
               time.sleep(2)
               print()
               print("oooooo... always knew you were a freak nasty ;)")
               break
           else:
               time.sleep(2)
               print()
               print(".....I'm speechless")
               break
        while(True):
           time.sleep(2)
           print() 
           print("Question Number 3. Would you rather...") 
           time.sleep(2)
           print() 
           print("a. Have random uncontrollable farts that are super loud and smell like nothing?")
           time.sleep(2)
           print()
           print("b. Have controllable farts that are silent but kills a infant at random in your local area")
           time.sleep(2)
           print()
           questionOne = input("Enter either [a] or [b]: ")
           if questionOne.lower() != "a" and questionOne.lower() != "b":
               print("That's not a choice please try again")
           elif questionOne.lower() == "a":
               time.sleep(2)
               print()
               print("Interesting choice.. better not go to a library then.")
               break
           else:
               time.sleep(2)
               print()
               print(".........You monster......")
               break
        while(True):
           time.sleep(2)
           print() 
           print("Question Number 4. Would you rather...")
           time.sleep(2)
           print() 
           print("a. Pull your own thumbnail off with a fork? (and you can't use anything to numb it) ")
           time.sleep(2)
           print() 
           print("b. Put a toothpick under your big toenail and kick a brick wall as hard as possible?")
           time.sleep(2)
           print() 
           questionOne = input("Enter either [a] or [b]: ")
           if questionOne.lower() != "a" and questionOne.lower() != "b":
               print("That's not a choice please try again")
           elif questionOne.lower() == "a":
               time.sleep(2)
               print()
               print("Wow.... I'm concerned for your mental health at this point.")
               break
           else:
               time.sleep(2)
               print()
               print("Damn... If this was Spongebob's universe you'd DEFINITLEY would make it into the Salty Spitoon")
               break
        while(True):
           time.sleep(2)
           print()  
           print("FINAL QUESTION!!!!!!!! WOULD YOU RATHER...")
           time.sleep(2)
           print() 
           print("a. Drink two litres of your piss after you eat asparagus and swish it around your mouth before you swallow it?")
           time.sleep(2)
           print() 
           print("b. Drink two litres of sweat of a sumo wrestler and do the exact same thing?")
           time.sleep(2)
           print() 
           questionOne = input("Enter either [a] or [b]: ")
           if questionOne.lower() != "a" and questionOne.lower() != "b":
               print("That's not a choice please try again")
           elif questionOne.lower() == "a":
               time.sleep(2)
               print()
               print("LMAO wow... pretend it's lemonade and maybe it'll help?")
               break
           else:
               time.sleep(2)
               print()
               print("ewwwwwww.....imagine all the body hair and germs in your mouth XD.")
               break                
        
        time.sleep(2)
        print()
        print("That's it now let's see how disturbing your are based on your answers")
        randomNum = random.randrange(0,100)
        time.sleep(1.5)
        print()
        print("Calulating....")
        time.sleep(1)
        print(".......")
        time.sleep(1)
        print(".......")
        time.sleep(1)
        print(".......")
        time.sleep(1)
        print("Drum roll please! *DRUM ROLL NOISES*")
        time.sleep(2)
        print()
        print(f"Based on your answers your disturbing rank is {randomNum}!")
        time.sleep(2)
        print()
        print("You are officialy one nasty individual!")
        time.sleep(1)
        print()
        while True:
            playAgainInput = input("Would you like to play again? [enter y or n]")
            if playAgainInput.lower() != "y" and playAgainInput.lower() != "n":
                print()
                print("Invalid input, please enter either y or n")
            elif playAgainInput == "y":
                break
            else:
                time.sleep(1)
                print()
                print("Ok cool, thanks for playing!")
                time.sleep(1)
                print()
                print("GAME OVER")
                playAgain = False; 
                break

main()