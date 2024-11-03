import pickle
   
# takes recipe input from user and returns recipe dictionary
def take_recipe():
    name = str(input("Recipe name: "))
    cooking_time = int(input("Cooking time in minutes: "))
    ingredients = list(input("Ingredients (seperate ingredients with commas): ").split(", "))
    difficulty = calc_difficulty(cooking_time, ingredients)
    recipe = {
       "name": name,
       "cooking_time": cooking_time,
       "ingredients": ingredients,
       "difficulty": difficulty
    }

    return recipe

# assigns a difficulty level based on ingredients and cooking_time
def calc_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        difficulty = "Easy"
    if cooking_time < 10 and len(ingredients) >= 4:
        difficulty = "Medium"
    if cooking_time >= 10 and len(ingredients) < 4:
        difficulty = "Intermediate"
    if cooking_time >= 10 and len(ingredients) >= 4:
        difficulty = "Hard"

    return difficulty

# prompts user to enter a file name for the binary recipe file
file_name = str(input("Enter a name for your file: "))

# will load file if it exists
try:
    file = open(file_name, "rb")
    data = pickle.load(file)
    print("File loaded successfully")

# if there is no file, this will create one
except FileNotFoundError:
    print("File was not found, creating one for you")
    data = {
        "recipes_list": [],
        "all_ingredients": []
    }

# handles all other errors
except: 
    print("Something went wrong, please try again")
    data = {
        "recipes_list": [],
        "all_ingredients": []
    }

 # closes file if no errors occurred
else: 
    file.close()

# extracts data into recipes and ingredients lists
finally:
    recipes_list = data["recipes_list"]
    all_ingredients = data["all_ingredients"]


# prompts user to initiate take_recipe() loop with range(n)
n = int(input("How many recipes would you like to enter?"))

# iterates over take_recipe function n times
for i in range(n):
    recipe = take_recipe()

    for ingredient in recipe["ingredients"]:

        # adds ingredients to list if not there
        if not ingredient in all_ingredients:
            all_ingredients.append(ingredient)

    # adds recipe to recipes list
    recipes_list.append(recipe)

# creates an updated dictionary with recipes and ingredients
data = {"recipes_list": recipes_list, "all_ingredients": all_ingredients}

# opens and writes updated data to updated file
updated_file = open(file_name, "wb")
data = pickle.dump(data, updated_file)

updated_file.close()
print("All done, goodbye")