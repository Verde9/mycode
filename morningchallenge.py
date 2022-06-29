#!/usr/bin/env python3

def main():

    rock_lee={'name':'Rock Lee','age':'14','clan':'Lee Clan','specialty':'taijutsu','top abilities':['Eight Gates','Leaf Whirlwind','Drunken Fist']}

    rock_lee['fav_food'] = "ramen"

    print(rock_lee.keys())

    
    selection = True
    while(selection):
        choice = input("Type in a key for the values that you want to see: ")
        if choice not in rock_lee:
            print("invalid input try again")
            selection = True
        else:
            print(f"Rock Lee's {choice} is {rock_lee[choice]}")
            selection = False
            break
main()