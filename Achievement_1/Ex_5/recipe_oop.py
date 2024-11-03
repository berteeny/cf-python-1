class Recipe:
    all_ingredients = []
    def __init__(self, name, ingredients, cooking_time):
        self.name = name
        self.ingredients = ingredients
        self.cooking_time = cooking_time
        self.difficulty = None

# getters
    def get_name(self):
        return self.name
    
    def get_cooking_time(self):
        return self.cooking_time
    
    def get_ingredients(self):
        return self.ingredients
    
    def get_difficulty(self):
        if not self.difficulty:
            return self.calculate_difficulty()

# setters
    def set_name(self, name):
        self.name = name
        
    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time

# add ingredients to list
    def add_ingredients(self, *ingredients):
        for ingredient in ingredients:
            self.ingredients.append(ingredient)
        self.update_all_ingredients()

# evaluates + assigns recipe difficulty
    def calculate_difficulty(self):
        if self.cooking_time < 10 and len(self.ingredients) < 4:
            difficulty = "Easy"
        if self.cooking_time < 10 and len(self.ingredients) >= 4:
            difficulty = "Medium"
        if self.cooking_time >= 10 and len(self.ingredients) < 4:
            difficulty = "Intermediate"
        if self.cooking_time >= 10 and len(self.ingredients) >= 4:
            difficulty = "Hard"

        return difficulty

# searches available ingredients
    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients
    
# adds all new ingredients to list
    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if not ingredient in Recipe.all_ingredients:
                Recipe.all_ingredients.append(ingredient)

# string representation of recipe
    def __str__(self):
        output = f"Name: {self.name}\nIngredients: {', '.join(self.ingredients)}\nCooking time: {self.cooking_time} minutes\nDifficulty: {self.get_difficulty()}\n"
        return output
    
# finds recipe by ingredient search
    def recipe_search(data, search_term):
        print("Recipes that contain " + search_term + ":\n")
        for recipe in data:
            if recipe.search_ingredient(search_term):
                print(recipe)

# recipes
tea = Recipe("Tea", ["Tea leaves", "Sugar", "Water"], 5)
coffee = Recipe("Coffee", ["Coffee powder", "Suagr", "Water"], 5)
cake = Recipe("Cake", ["Sugar", "Butter", "Eggs", "Vanilla", "Flour", "Baking powder", "Milk"], 50)
smoothie = Recipe("Smoothie", ["Raspberries", "Milk", "Peanut butter", "Sugar", "Ice cubes"], 5)

# adding recipes to list
recipes_list = [tea, coffee, cake, smoothie]

# printing string representations of all recipes
for recipe in recipes_list:
    print(recipe)

# testing recipe_search method
    
for ingredient in ["Water", "Sugar", "Raspberries"]:
    Recipe.recipe_search(recipes_list, ingredient)



