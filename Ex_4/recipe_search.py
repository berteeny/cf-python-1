import pickle

def display_recipe(recipe):
    print("Recipe: ", recipe["name"])
    print("Cooking time: ", recipe["cooking_time"], " minutes")
    print("Ingredients: ")
    for ingredient in recipe["ingredients"]:
        print(ingredient)
    print("Difficulty: ", recipe["difficulty"])


def search_ingredient(data):
    avail_ingredients = enumerate(data["all_ingredients"])
    ordered_ingredients = list(avail_ingredients)
    print("Your ingredients: ")
    for ingredient in ordered_ingredients:
        print(ingredient[0], ingredient[1])

    try:
        num = int(input("Type a number from this list: "))
        ingredient_searched = ordered_ingredients[num][1]
        print("Searching for recipes with ", ingredient_searched)
    except:
        print("That number seems to be unassigned to any ingredient. Please try again")
    else:
        for recipe in data["recipes_list"]:
            if ingredient_searched in recipe["ingredients"]:
                print(recipe)

file_name = str(input("Please type the name of the file that contains your recipes: "))

try:
    file = open(file_name, "rb")
    data = pickle.load(file)
    print("File loaded successfully")
except:
    print("The file has not been found.")
else:
    search_ingredient(data)
    file.close()