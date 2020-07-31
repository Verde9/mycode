#!/usr/bin/env python3

weight = int(input("What is your dogs weight? (Just add digits not 'lbs') "))

if 1 <= weight <= 5:
    print("You're dog needs to eat! You should serve your dog 1/2 - 5/8 cups of dog food")
elif 6 <= weight <= 10:
    print("You should serve your dog 3/4 - 1 cups of dog food")
elif 11 <= weight <= 29:
    print("You should serve your dog 1 1/4 - 1 3/4 cups of dog food")
elif 30 <= weight <= 59:
    print("You should serve your dog 2 1/4 - 3 cups of dog food")
elif 60 <= weight <= 79:
    print("You should serve your dog 3 - 4 cups of dog food")
elif 80 <= weight <= 99:
    print("You should serve your dog 3 2/3 - 5 cups of dog food")
elif 100 <= weight <= 100:
    print("You should serve your dog 4 1/4 - 6 cups of dog food")
elif weight > 150:
    print("You're dog is fat, stop feeding them.... food they have enough")
else:
    print("Invalid result")
