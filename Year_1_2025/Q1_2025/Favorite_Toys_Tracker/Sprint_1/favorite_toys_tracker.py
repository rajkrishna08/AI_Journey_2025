# Favorite Toys Tracker Project
# A project to manage a list of my favorite toys, store them in a big toy box in the sky (database), and do fun things with them!

# Import the magic tools we need
import psycopg2  # This helps us talk to the big toy box (PostgreSQL database)
from psycopg2 import Error  # This helps us catch mistakes when talking to the database

# A special number to keep track of how many toys I’ve added
total_toys_added = 0  # Start with 0 toys added

def get_db_connection():
    """Connects to the big toy box in the sky (database) where I keep my toys."""
    try:
        # Try to connect to the database using my secret details
        conn = psycopg2.connect(
            dbname="training_db",  # The name of my toy box
            user="postgres",  # My username to open the toy box
            password="Qwerty123!!",  # My secret password (replace with yours!)
            host="localhost",  # Where my toy box lives (on my computer)
            port="5432"  # The special door number to enter the toy box
        )
        return conn  # Give back the connection so we can use it
    except Error as e:
        # If something goes wrong, tell me what happened
        print(f"Error connecting to the database: {e}")
        return None  # Say we couldn’t connect

def close_db_connection(conn, cursor):
    """Closes the door to the toy box so it’s safe."""
    cursor.close()  # Close the helper that talks to the toy box
    conn.close()  # Close the toy box door
    print("Database connection closed.")  # Let me know the door is closed

def load_toys_from_db(cursor):
    """Gets all my toys from the big toy box in the sky (database)."""
    try:
        # Ask the toy box: "Give me all the toy names!"
        cursor.execute("SELECT name FROM toys")
        # Put all the toy names in a list to use in Python
        return [row[0] for row in cursor.fetchall()]
    except Error as e:
        # If something goes wrong, tell me what happened
        print(f"Error loading toys from the database: {e}")
        return []  # Give back an empty list if there’s a problem

def add_toy_to_list(my_toys):
    """Asks me to add a new toy to my list and keeps track of how many I’ve added."""
    global total_toys_added  # Use the special number to count toys I’ve added
    # Ask me: "What toy do you want to add?"
    new_toy = input("Enter a new toy to add to your list: ")
    if new_toy:  # Make sure I typed something
        my_toys.append(new_toy)  # Add the new toy to my list
        total_toys_added += 1  # Add 1 to my toy counter
        print(f"Added a {new_toy}! Now my toys are: {my_toys}")  # Show my updated list
        print(f"You've added a total of {total_toys_added} toys so far!")  # Show how many toys I’ve added
    else:
        print("You didn't enter a toy name!")  # Tell me if I forgot to type a toy
    return my_toys  # Give back my updated list

def add_toy_to_db(cursor, conn, toy_name):
    """Saves a new toy to the big toy box in the sky (database) so I don’t lose it."""
    try:
        # Tell the toy box: "Save this toy name!"
        cursor.execute("INSERT INTO toys (name) VALUES (%s)", (toy_name,))
        conn.commit()  # Make sure the toy is saved
        print(f"Saved {toy_name} to my big toy box in the sky (database)!")  # Let me know it’s saved
    except Error as e:
        # If something goes wrong, tell me what happened
        print(f"Error adding toy to the database: {e}")
        conn.rollback()  # Undo the save if there’s a problem

def remove_toy_from_list(my_toys, cursor, conn):
    """Asks me to remove a toy from my list and the big toy box in the sky."""
    # Ask me: "Which toy do you want to take out?"
    toy_to_remove = input("Type the name of a toy to remove: ")
    if toy_to_remove in my_toys:  # Check if the toy is in my list
        my_toys.remove(toy_to_remove)  # Take the toy out of my list
        print(f"Removed {toy_to_remove}! Now my toys are: {my_toys}")  # Show my updated list
        try:
            # Tell the toy box: "Take this toy out!"
            cursor.execute("DELETE FROM toys WHERE name = %s", (toy_to_remove,))
            conn.commit()  # Make sure the toy is gone
            print(f"Removed {toy_to_remove} from my big toy box in the sky (database)!")  # Let me know it’s gone
        except Error as e:
            # If something goes wrong, tell me what happened
            print(f"Error removing toy from the database: {e}")
            conn.rollback()  # Undo the removal if there’s a problem
    else:
        print(f"Sorry, {toy_to_remove} is not in my toy box!")  # Tell me if the toy isn’t there
    return my_toys  # Give back my updated list

def search_toy_in_list(my_toys, search_toy):
    """Looks for a toy in my list to see if I have it."""
    if search_toy in my_toys:  # Check if the toy is in my list
        print(f"Yay! I found {search_toy} in my toy box!")  # Happy message if I find it
    else:
        print(f"Sorry, I don't have {search_toy} in my toy box.")  # Sad message if I don’t

def display_toys_starting_with_letter(cursor):
    """Finds toys in the big toy box that start with a letter I choose (doesn’t care about big or small letters)."""
    # Ask me: "Which letter should the toys start with?"
    letter_to_find = input("Enter a letter to find toys starting with (e.g., 'c' or 'C'): ")
    try:
        # Ask the toy box: "Give me all toys starting with this letter!"
        query = "SELECT name FROM toys WHERE name ILIKE %s"
        cursor.execute(query, (letter_to_find + '%',))
        matching_toys = cursor.fetchall()  # Get all the toys that match
        if matching_toys:  # If I found some toys
            print(f"Toys starting with '{letter_to_find}' (case-insensitive):")
            for toy in matching_toys:  # Show each toy one by one
                print(toy[0])
        else:
            print(f"No toys found starting with '{letter_to_find}'!")  # Tell me if there are no matches
    except Error as e:
        # If something goes wrong, tell me what happened
        print(f"Error searching toys in the database: {e}")

def display_total_toys_added():
    """Shows how many toys I’ve added so far using my special counter."""
    print(f"You've added a total of {total_toys_added} toys to your collection so far!")
    if total_toys_added >= 5:  # If I’ve added 5 or more toys
        print("Wow, you've added a lot of toys! You're a toy collector!")  # Say I’m a big collector
    else:
        print("Keep adding more toys to grow your collection!")  # Encourage me to add more

def reset_total_toys_added():
    """Lets me reset my toy counter to start counting again from 0."""
    global total_toys_added  # Use my special counter
    # Ask me: "Do you want to start counting from 0?"
    reset_choice = input("Do you want to reset the total toys added counter? (yes/no): ")
    if reset_choice.lower() == "yes":  # If I say yes
        total_toys_added = 0  # Set the counter to 0
        print("The total toys added counter has been reset to 0!")  # Tell me it’s reset
    else:
        print("Okay, the counter was not reset.")  # Tell me I didn’t reset it
    print(f"Current total toys added: {total_toys_added}")  # Show the counter now

def display_total_toys_in_db(cursor):
    """Counts how many toys are in the big toy box in the sky (database)."""
    try:
        # Ask the toy box: "How many toys do you have?"
        cursor.execute("SELECT COUNT(*) FROM toys")
        total_toys_in_db = cursor.fetchone()[0]  # Get the number of toys
        print(f"There are {total_toys_in_db} toys in the database!")  # Show the number
        if total_toys_in_db >= 5:  # If there are 5 or more toys
            print("Wow, your database has a lot of toys!")  # Say I have a lot
        else:
            print("Your database has a few toys—let's add more!")  # Encourage me to add more
    except Error as e:
        # If something goes wrong, tell me what happened
        print(f"Error counting toys in the database: {e}")

def display_all_toys_in_db(cursor):
    """Shows all the toys in the big toy box in the sky (database)."""
    try:
        # Ask the toy box: "Give me all the toy names!"
        cursor.execute("SELECT name FROM toys")
        all_toys_in_db = cursor.fetchall()  # Get all the toys
        if all_toys_in_db:  # If there are toys
            print("Here are all the toys in the database:")
            for toy in all_toys_in_db:  # Show each toy one by one
                print(toy[0])
        else:
            print("There are no toys in the database yet!")  # Tell me if the toy box is empty
    except Error as e:
        # If something goes wrong, tell me what happened
        print(f"Error retrieving toys from the database: {e}")

def search_toys_by_keyword_in_db(cursor):
    """Looks for toys in the big toy box that have a word I choose in their name."""
    # Ask me: "What word should I look for in the toy names?"
    keyword = input("Enter a keyword to search for toys in the database (e.g., 'car'): ")
    try:
        # Ask the toy box: "Give me all toys with this word in their name!"
        query = "SELECT name FROM toys WHERE name ILIKE %s"
        cursor.execute(query, ('%' + keyword + '%',))
        matching_toys = cursor.fetchall()  # Get all the toys that match
        if matching_toys:  # If I found some toys
            print(f"Toys in the database containing '{keyword}':")
            for toy in matching_toys:  # Show each toy one by one
                print(toy[0])
        else:
            print(f"No toys found in the database containing '{keyword}'!")  # Tell me if there are no matches
    except Error as e:
        # If something goes wrong, tell me what happened
        print(f"Error searching toys in the database: {e}")

def delete_toy_from_db(cursor, conn):
    """Takes a toy out of the big toy box in the sky (database)."""
    # Ask me: "Which toy should I take out of the toy box?"
    toy_to_delete = input("Enter the name of a toy to delete from the database (e.g., 'car'): ")
    try:
        # Tell the toy box: "Take this toy out!"
        query = "DELETE FROM toys WHERE name = %s"
        cursor.execute(query, (toy_to_delete,))
        conn.commit()  # Make sure the toy is gone
        if cursor.rowcount > 0:  # If I took out a toy
            print(f"Deleted '{toy_to_delete}' from the database!")  # Let me know it’s gone
        else:
            print(f"No toy named '{toy_to_delete}' was found in the database!")  # Tell me if the toy wasn’t there
    except Error as e:
        # If something goes wrong, tell me what happened
        print(f"Error deleting toy from the database: {e}")
        conn.rollback()  # Undo the removal if there’s a problem

def update_toy_name_in_db(cursor, conn):
    """Changes a toy’s name in the big toy box in the sky (database)."""
    # Ask me: "Which toy’s name do you want to change?"
    old_name = input("Enter the current name of the toy to update (e.g., 'doll'): ")
    # Ask me: "What should the new name be?"
    new_name = input(f"Enter the new name for '{old_name}' (e.g., 'baby doll'): ")
    try:
        # Tell the toy box: "Change this toy’s name to the new name!"
        query = "UPDATE toys SET name = %s WHERE name = %s"
        cursor.execute(query, (new_name, old_name))
        conn.commit()  # Make sure the name is changed
        if cursor.rowcount > 0:  # If I changed a toy’s name
            print(f"Updated '{old_name}' to '{new_name}' in the database!")  # Let me know it’s changed
        else:
            print(f"No toy named '{old_name}' was found in the database!")  # Tell me if the toy wasn’t there
    except Error as e:
        # If something goes wrong, tell me what happened
        print(f"Error updating toy name in the database: {e}")
        conn.rollback()  # Undo the change if there’s a problem

def update_toy_category_in_db(cursor, conn):
    """Changes a toy’s category in the big toy box in the sky (database)."""
    # Ask me: "Which toy’s category do you want to change?"
    toy_to_update = input("Enter the name of the toy to update its category (e.g., 'baby doll'): ")
    # Ask me: "What should the new category be?"
    new_category = input(f"Enter the category for '{toy_to_update}' (e.g., 'doll', 'vehicle', 'game'): ")
    try:
        # Tell the toy box: "Change this toy’s category to the new category!"
        query = "UPDATE toys SET category = %s WHERE name = %s"
        cursor.execute(query, (new_category, toy_to_update))
        conn.commit()  # Make sure the category is changed
        if cursor.rowcount > 0:  # If I changed a toy’s category
            print(f"Set the category of '{toy_to_update}' to '{new_category}' in the database!")  # Let me know it’s changed
        else:
            print(f"No toy named '{toy_to_update}' was found in the database!")  # Tell me if the toy wasn’t there
    except Error as e:
        # If something goes wrong, tell me what happened
        print(f"Error updating toy category in the database: {e}")
        conn.rollback()  # Undo the change if there’s a problem

def display_toys_with_categories(cursor):
    """Shows all toys in the big toy box with their categories (like ‘doll’ or ‘vehicle’)."""
    try:
        # Ask the toy box: "Give me all the toys and their categories!"
        cursor.execute("SELECT name, category FROM toys")
        all_toys_with_categories = cursor.fetchall()  # Get all the toys and categories
        if all_toys_with_categories:  # If there are toys
            print("Here are all the toys in the database with their categories:")
            for toy in all_toys_with_categories:  # Look at each toy one by one
                toy_name, category = toy  # Get the toy’s name and category
                category_display = category if category else "No category set"  # Show ‘No category set’ if there’s no category
                print(f"Toy: {toy_name}, Category: {category_display}")  # Show the toy and its category
        else:
            print("There are no toys in the database yet!")  # Tell me if the toy box is empty
    except Error as e:
        # If something goes wrong, tell me what happened
        print(f"Error retrieving toys from the database: {e}")

def add_toy_with_category_to_db(cursor, conn):
    """Adds a new toy with a category to the big toy box in the sky (database)."""
    try:
        # Ask me: "What new toy do you want to add?"
        toy_name = input("Enter the name of the new toy to add to the database (e.g., 'truck'): ")
        if not toy_name:  # Make sure I typed something
            print("Toy name cannot be empty!")  # Tell me if I forgot to type a toy
            return

        # Ask me: "What kind of toy is it?"
        category = input("Enter the category for the new toy (e.g., 'vehicle', 'doll', 'game') or press Enter to skip: ")
        category = category if category else None  # If I don’t type a category, use None (no category)

        # Tell the toy box: "Save this toy with its category!"
        query = "INSERT INTO toys (name, category) VALUES (%s, %s)"
        cursor.execute(query, (toy_name, category))
        conn.commit()  # Make sure the toy is saved

        print(f"Added '{toy_name}' to the database with category: {category if category else 'None'}")  # Let me know it’s saved
    except Error as e:
        # If something goes wrong, tell me what happened
        print(f"Error adding toy to the database: {e}")
        conn.rollback()  # Undo the save if there’s a problem

def search_toys_by_category_in_db(cursor):
    """Looks for toys in the big toy box that have the kind (category) I choose."""
    try:
        # Ask me: "What kind of toys do you want to find?"
        category_to_find = input("Enter a category to search for toys (e.g., 'doll', 'vehicle', 'game'): ")
        if not category_to_find:  # Make sure I typed something
            print("Category cannot be empty!")  # Tell me if I forgot to type a category
            return

        # Ask the toy box: "Give me all toys with this category!"
        query = "SELECT name, category FROM toys WHERE category = %s"
        cursor.execute(query, (category_to_find,))
        matching_toys = cursor.fetchall()  # Get all the toys that match
        if matching_toys:  # If I found some toys
            print(f"Toys in the database with category '{category_to_find}':")
            for toy in matching_toys:  # Show each toy one by one
                toy_name, category = toy
                print(f"Toy: {toy_name}, Category: {category}")
        else:
            print(f"No toys found in the database with category '{category_to_find}'!")  # Tell me if there are no matches
    except Error as e:
        # If something goes wrong, tell me what happened
        print(f"Error searching toys by category in the database: {e}")

def main():
    """The main part of my toy tracker that runs everything."""
    # Part 1: Welcome Message
    my_name = "Krishna"  # My name to show everyone
    print("Welcome to Krishna's Favorite Toys Tracker!")  # Say hello to me
    print("My name is:", my_name.upper())  # Show my name in big letters
    print("I'm ready to keep track of my favourite toys!")  # Let everyone know I’m ready

    # Load my toys from the big toy box in the sky
    my_toys = load_toys_from_db(cursor)  # Get all my toys from the database
    print("Here are my favourite toys from the database:", my_toys)  # Show my toys
    print("I have this many toys:", len(my_toys))  # Count how many toys I have

    # Show each toy one by one
    print("Here are my favourite toys:")
    for toy in my_toys:  # Look at each toy one by one
        print(toy)  # Show the toy’s name

    # Part 3: Manage My Toy List
    my_toys.append("robot")  # Add a robot to my list
    print("Added a robot! Now my toys are:", my_toys)  # Show my updated list
    my_toys.remove("ball")  # Take the ball out of my list
    print("Took the ball away! Now my toys are:", my_toys)  # Show my updated list
    print("I have this many toys now:", len(my_toys))  # Count my toys again

    # Part 4: Search for Toys
    search_toy_in_list(my_toys, "car")  # Look for a car in my list
    search_toy_in_list(my_toys, "train")  # Look for a train in my list

    # Part 5: Add Toys Interactively
    print("Let's add a new toy to your toy box!")  # Let’s add a new toy
    my_toys = add_toy_to_list(my_toys)  # Add a toy to my list
    add_toy_to_db(cursor, conn, my_toys[-1])  # Save the new toy to the big toy box
    print("I have this many toys now:", len(my_toys))  # Count my toys again
    print("Final toy list:", my_toys)  # Show my final list

    # Part 6: Remove Toys Interactively
    print("Let's remove a toy from your toy box!")  # Let’s take a toy out
    my_toys = remove_toy_from_list(my_toys, cursor, conn)  # Remove a toy from my list and toy box
    print("I have this many toys now:", len(my_toys))  # Count my toys again
    print("Final toy list:", my_toys)  # Show my final list

    # Day 5, Hour 3 Features
    display_toys_starting_with_letter(cursor)  # Find toys starting with a letter
    display_total_toys_added()  # Show how many toys I’ve added
    reset_total_toys_added()  # Let me reset my toy counter
    display_total_toys_in_db(cursor)  # Count all toys in the toy box
    display_all_toys_in_db(cursor)  # Show all toys in the toy box
    search_toys_by_keyword_in_db(cursor)  # Look for toys with a word in their name
    delete_toy_from_db(cursor, conn)  # Take a toy out of the toy box
    update_toy_name_in_db(cursor, conn)  # Change a toy’s name in the toy box
    update_toy_category_in_db(cursor, conn)  # Change a toy’s category in the toy box
    display_toys_with_categories(cursor)  # Show all toys with their categories
    add_toy_with_category_to_db(cursor, conn)  # Add a new toy with a category
    search_toys_by_category_in_db(cursor)  # Look for toys by their category

if __name__ == "__main__":
    # Open the door to the big toy box in the sky
    conn = get_db_connection()  # Try to connect to the toy box
    if conn is None:  # If I can’t connect
        print("Failed to connect to the database. Exiting...")  # Tell me I can’t play
        exit()  # Stop the program
    cursor = conn.cursor()  # Get a helper to talk to the toy box

    # Start my toy tracker
    main()  # Run the main part of my program

    # Close the door to the toy box when I’m done
    close_db_connection(conn, cursor)  # Make sure the toy box is safe