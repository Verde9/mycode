#!/usr/bin/env python3

# Asks for to input name
name = input("What is your name? ")

# Creates a list in a variable "col_list"
col_list = ["blue", "Columbus"]

# Appends value "1492" to list "col_list"
col_list.append(1492)

# Prints the following string using the given list arguements
print(f"{col_list[2]}, {col_list[1]} sailed the ocean {col_list[0]}. {name} fell off the boat. :(")
