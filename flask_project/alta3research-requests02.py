#!/usr/bin/env python3
import requests
import random
from pprint import pprint

URLm= "http://127.0.0.1:2224/yomama"

URLd="http://127.0.0.1:2224/yodaddy"

respM= requests.get(URLm).json()

respD= requests.get(URLd).json()

print("Do you want to hear a yo mama joke or a dad joke? [1. Mama, 2. Daddy]")
choice = input(">")
print()

if int(choice) == 1:
    number = random.randrange(0,10)
    print(respM[number]["joke"])
elif int(choice) == 2:
    number = random.randrange(0,10)
    print(respD[number]["joke"])   

