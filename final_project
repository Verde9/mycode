#!/usr/bin/env python3

"""Food Saver Script | By: Gregory Green """

import requests
import sys

# Initial code that welcomes the user and lists the directions on how to use the script
print()
print('WELCOME TO FOOD SAVER !\n')
print('Directions:\n'
      '1) List the ingredients you have in your pantry\n'
      '2) Enter the number of recipes you want to receive back *Note: Quantity of recipes is dependent on ingredients specified\n'
      '3) Choose the desired recipe from output\n'
      '4) Food Saver will generate a file with your recipe and needed ingredients\n')
print(input('Once you understood the directions press ENTER to continue'))


# recipe_finder is a function using the spoonacular api to attain a list of recipes.
def recipe_finder():
    print('RECIPE FINDER\n')

    # User will input there ingredients seperated by commas, enter a number of recipes they would like to receive back, then function will output results on screen
    while True:
        try:
            ingredients = input(
                'Alright, now for the recipes! Enter the ingredients you have here [PLEASE SEPARATE EACH INGREDIENT WITH COMMAS]: ')

            print('\nCool! Now enter in the number of recipes you want to receive back.\n')
            number = int(input('How many recipes do you want back?: '))
            print()
            print('Cool, loading your recipes... \n')
            api_key = 'bebd83d22bd642b6b2c4a2cb8f1dc1d8'
            r = requests.get(
                f"https://api.spoonacular.com/recipes/findByIngredients?apiKey={api_key}&ingredients={ingredients}&number={number}")
            print()

            for yum in r.json():
                print(yum['title'])
            print()
            break
        except:
            print("\nLooks like you messed something up. Take your time, and enter it in again. \n")


# Once the user has found their desired recipe the instructions_generator function ask for the name of the recipe and generate the ingredients as well as the directions
def instructions_generator():
    global ingredients_api
    chosen_recipe = input(
        "Great! Looks like you found a recipe, now copy and paste it here so I can generate the recipe: ").lower()
    print()
    print(f"Generating recipe for {chosen_recipe}. . . \n")

    api_key = 'bebd83d22bd642b6b2c4a2cb8f1dc1d8'
    r = requests.get(
        f"https://api.spoonacular.com/recipes/complexSearch?apiKey={api_key}&query={chosen_recipe}&addRecipeInformation=true")
    directions_api = r.json()
    
    try:
        recipe_id = directions_api['results'][0]['id']

        re = requests.get(f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={api_key}")
        ingredients_api = re.json()
    except:
        print(
            "So sorry, looks like this recipe doesn't have an ID to generate a full recipe. Please, run the script again")
        sys.exit()
    with open(f"{chosen_recipe}.txt", "a") as recipe_doc:
        title = f"RECIPE FOR {chosen_recipe} <3\n"
        ingredients = "INGREDIENTS\n"
        recipe_doc.write(title.upper())
        recipe_doc.write('\n')
        recipe_doc.writelines(ingredients)

    for items in ingredients_api['extendedIngredients']:
        with open(f"{chosen_recipe}.txt", "a") as recipe_doc:
            recipe_doc.write(f"- {items['original']} \n")

    num = 1

    with open(f"{chosen_recipe}.txt", "a") as recipe_doc:
        recipe_doc.write('\n')
        directions = "DIRECTIONS\n"
        recipe_doc.write(directions)

    try:

        for steps in directions_api['results'][0]['analyzedInstructions'][0]['steps']:
            with open(f"{chosen_recipe}.txt", "a") as recipe_doc:
                recipe_doc.write(f"{num}. {steps['step']} \n")
                num += 1
    except:
        print("Uh oh, looks like this recipe doesn't come with instructions sorry :(\n")
        with open(f"{chosen_recipe}.txt", "a") as recipe_doc:
            recipe_doc.write('\n')
            unavailable = "Sorry directions not available!"
            recipe_doc.write(unavailable)


recipe_finder()
satisfaction = input("Are you cool with these recipes? If not let me know by entering yes or no: ")

while True:
    if satisfaction.lower() == 'no':
        recipe_finder()
        satisfaction = input("Are you cool with these recipes? If not let me know by entering yes or no: ")
        print()
    elif satisfaction.lower() == 'yes':
        print()
        break
    elif satisfaction.lower() != 'yes' or 'no':
        print("Invalid input try again \n")
        satisfaction = input("Are you cool with these recipes? If not let me know by entering yes or no: ")

instructions_generator()
# After the instructions_generator is finished it will complete compile all recipe information into a .txt in the users current directory.
print("BOOM! ALL DONE! Your recipe should now be in your current directory, now get cooking!")


