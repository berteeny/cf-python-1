recipes_list = []
ingredients_list = []

# takes user input for recipe components
def take_recipe():
    name = str(input("Recipe name: "))
    cooking_time = int(input("Cooking time in minutes: "))
    ingredients = list(input("Ingredients (seperate ingredients with commas): ").split(", "))
    recipe = {
       "name": name,
       "cooking_time": cooking_time,
       "ingredients": ingredients
    }

    return recipe
    
# initial prompt to user
n = int(input("How many recipes would you like to enter?"))

# iterates over take_recipe function n times
for i in range(n):
    recipe = take_recipe()

    for ingredient in recipe["ingredients"]:
        # adds ingredients to list if not there
        if not ingredient in ingredients_list:
            ingredients_list.append(ingredient)
    # adds recipe to recipes list
    recipes_list.append(recipe)

# iterates through recipes and assigns a difficulty based on cooking_time and ingredients
for recipe in recipes_list:
    if recipe["cooking_time"] < 10 and len(recipe["ingredients"]) < 4:
        recipe["difficulty"] = "Easy"
    
    elif recipe["cooking_time"] < 10 and len(recipe["ingredients"]) >= 4:
        recipe["difficulty"] = "Medium"
    
    elif recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) < 4:
        recipe["difficulty"] = "Intermediate"
    
    elif recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) >= 4:
        recipe["difficulty"] = "Hard"

# iterates over all recipes and prints their content into console
for recipe in recipes_list:
    print("Recipe: ", recipe["name"])
    print("Cooking time: ", recipe["cooking_time"], " minutes")
    print("Ingredients: ")
    for ingredient in recipe["ingredients"]:
        print(ingredient)
    print("Difficulty: ", recipe["difficulty"])

# iterates over ingredients_list and prints each ingredient in alphabetical order
def sort_ingredients():
    print("Ingredients available in database: ")
    print("----------------------------------")
    ingredients_list.sort()
    for ingredient in ingredients_list:
        print(ingredient)

sort_ingredients()