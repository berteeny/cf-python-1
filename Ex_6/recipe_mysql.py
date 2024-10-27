import mysql.connector

line = "-------------------------------"

# main menu navigator
def main_menu(conn, cursor):
    choice = None
    while(choice != "quit"):
        print(f"\n{line}")
        print("What would you like to do?")
        print(f"{line}\n")
        print("1. Create a new recipe")
        print("2. Search for a recipe")
        print("3. Update an existing recipe")
        print("4. Delete an existing recipe")
        print("5. Exit\n")
        choice = str(input("Your choice (1-5): ")).strip()
        print(line)

        if choice == "1":
            create_recipe(conn, cursor)
        elif choice == "2":
            search_recipe(conn, cursor)
        elif choice == "3":
            update_recipe(conn, cursor)
        elif choice == "4":
            delete_recipe(conn, cursor)
        elif choice == "5":
            print("See you next time!")
            conn.commit()
            cursor.close()
            conn.close()
            break
        else:
            print("*****Invalid choice, please type one of the numbers above (1-5)")

# calculating difficulty based on cooking_time and number of ingredients
def calculate_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and len(ingredients) >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and len(ingredients) < 4:
        difficulty = "Intermediate"
    elif cooking_time >= 10 and len(ingredients) >= 4:
        difficulty = "Hard"

    return difficulty


# creating a new recipe + adding to db
def create_recipe(conn, cursor):
    name = str(input("Recipe name:  "))
    cooking_time = int(input("Cooking time (in minutes): "))
    ingredients = input("Ingredients (seperated by commas): ").strip().split(",")
    difficulty = calculate_difficulty(cooking_time, ingredients)

    ingredients_list = ", ".join(ingredients)

    insert_recipe = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"

    cursor.execute(insert_recipe, (name, ingredients_list, cooking_time, difficulty))
    conn.commit()

    print(line)
    print("Recipe added!")

    


# searching for a recipe by ingredient
def search_recipe(conn, cursor):
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()

    if not results:
        print(line)
        print("*****There are no recipes in this database yet.")
        print("*****Create a recipe!")
        return

    all_ingredients = set()

    try: 
        for row in results:
            ingredients = row[0].split(", ") 
            for ingredient in ingredients:
                if not ingredient in all_ingredients:
                    all_ingredients.add(ingredient.strip())
    except:
        print("*****An error occurred, please try again")


    for i, ingredient in enumerate(sorted(all_ingredients)):
        print(f"{i}. {ingredient}")
    choice = int(input("Type a number to select an ingredient to search by: "))
    if choice >= len(all_ingredients):
        print("*****That number is unassigned, please choose a valid number.")
    else:    
        selected_ingredient = sorted(all_ingredients)[choice]

        search_query = "SELECT * FROM Recipes WHERE ingredients LIKE %s"

        cursor.execute(search_query, ("%" + selected_ingredient + "%",)) 

        search_results = cursor.fetchall()
        if search_results:
            for row in search_results:
                print("\n", row)
        else:
                print(f"*****No recipes were found with {selected_ingredient}.")


# updating an existing recipe
def update_recipe(conn, cursor):
    cursor.execute("SELECT id, name FROM Recipes")
    results = cursor.fetchall()

    for row in results:
        print(f"{row[0]}. {row[1]}")

    print(line)
    selected_recipe = int(input("Type a number to select a recipe: "))
    # here vvv
    try:
        cursor.execute("SELECT id FROM Recipes WHERE id = %s", (selected_recipe,))
        result = cursor.fetchone()
        if not selected_recipe in result:
            print("*****That number is not assigned to a recipe, please select one with an assigned number. ")
        else:

        # here ^^^
            print(line)
            print("1. Name\n")
            print("2. Cooking time\n")
            print("3. Ingredients\n")
            choice = int(input("Please select a number to update the name, cooking time or ingredients of your recipe: ").strip())
            if choice == 1:
                update = input("Enter the new name for your recipe: ")
                update_query = "UPDATE Recipes SET name = %s WHERE id = %s"
                cursor.execute(update_query, (update, selected_recipe))
                print(line)
                print("Recipe updated!")
            elif choice == 2:
                update = int(input("Enter the new cooking time for your recipe (in minutes): "))
                update_query = "UPDATE Recipes SET cooking_time = %s WHERE id = %s"
                cursor.execute(update_query, (update, selected_recipe))
                print(line)
                print("Recipe updated!")
            elif choice == 3:
                ingredients = input("Enter all ingredients for your recipe (seperated by commas): ").strip().split(",")
                update = ", ".join(ingredients)
                update_query = "UPDATE Recipes SET ingredients = %s WHERE id = %s"
                cursor.execute(update_query, (update, selected_recipe))
                print(line)
                print("Recipe updated!")
                
            else:
                print("*****Please type 1, 2 or 3 to update the corresponding element of your recipe. ")

            if choice in [2, 3]:
                cursor.execute("SELECT cooking_time, ingredients FROM Recipes WHERE id = %s", (selected_recipe,))
                row = cursor.fetchone()
                difficulty = calculate_difficulty(row[0], row[1])
                update_query = "UPDATE Recipes SET difficulty = %s WHERE id = %s"
                cursor.execute(update_query, (difficulty, selected_recipe))
    except:
        print("\n*****That number is not assigned to a recipe, please type an assigned number")
    conn.commit()



# deleting an existing recipe
def delete_recipe(conn, cursor):
    cursor.execute("SELECT id, name FROM Recipes")
    results = cursor.fetchall()

    for row in results:
        print(f"{row[0]}. {row[1]}")
    try:
        selected_recipe = int(input("Type a number to select a recipe to delete: "))
        # 
        cursor.execute("SELECT id FROM Recipes WHERE id = %s", (selected_recipe,))
        result = cursor.fetchone()
        if not selected_recipe in result:
            print("\n*****That number is not assigned to a recipe, please select one with an assigned number. ")
        else:

        # 
            print(line)
            print(f"You have selected {selected_recipe}.\n Do you wish to delete this recipe?")
            print("This action cannot be undone.")
            confirmation = input("Continue? (y/n): ").lower()
            print(confirmation)
            if confirmation == "y":
                delete_query = "DELETE FROM Recipes WHERE id = %s"
                cursor.execute(delete_query, (selected_recipe,))
                conn.commit()
                print("Recipe deleted.")
            elif confirmation == "n":
                print("Deletion cancelled.")
            else:
                print("*****Please enter a valid value (y/n)")
    except:     
        print("*****That number is not assigned to a recipe, please select one with an assigned number. ")

            
   


# setting up conn, cursor and running main_menu()
conn = mysql.connector.connect(
    host="localhost",
    user="cf-python",
    passwd="password"
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

cursor.execute("USE task_database")

cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes(
               id INT AUTO_INCREMENT PRIMARY KEY,
               name VARCHAR(50),
               ingredients VARCHAR(255),
               cooking_time INT,
               difficulty VARCHAR(20)
)''')

main_menu(conn, cursor)