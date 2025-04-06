
# Favorite Toys Tracker Project - Part 1: Welcome Message
# Make a box for my name (variable with a string object)
my_name = "Krishna"  # My Name is Krishna

# Welcome to my magic toy box project!
import psycopg2
print("Welcome to krishna's Favorite Toys Tracker!")

# Tell everyone my name (using a variable and upper() method)
my_name = "krishna"
print("My name is:", my_name.upper())

# Tell everyone I'm ready (using a string)
print("I'm ready to keep track of my favourite toys!")

# Make a list of my favourite toys (using a list)
my_toys = ["car", "ball", "doll"]
print("Here are my favourite toys:", my_toys)

# Count my toys (using len() method)
print("I have this many toys:", len(my_toys))

# Print my toy list again (using a loop)
print("Here are my favourite toys:")
for toy in my_toys:
    print(toy)

# Favorite Toys Tracker Project - Part 3: Manage My Toy List
# Add a new toy to my list (using append() method)
my_toys.append("robot")  # Add a robot
print("Added a robot! Now my toys are:", my_toys)

# Remove a toy from my list (using remove() method)
my_toys.remove("ball")  # Take the ball away
print("Took the ball away! Now my toys are:", my_toys)

# Count my toys again (using len())
print("I have this many toys now:", len(my_toys))

# Favorite Toys Tracker Project - Part 4: Search for Toys
# Search for a toy in my list (using in operator)
search_toy = "car"  # Let's look for a car
if search_toy in my_toys:
    print(f"Yay! I found {search_toy} in my toy box!")
else:
    print(f"Sorry, I don't have {search_toy} in my toy box.")

# Search for another toy
search_toy = "train"  # Let's look for a train
if search_toy in my_toys:
    print(f"Yay! I found {search_toy} in my toy box!")
else:
    print(f"Sorry, I don't have {search_toy} in my toy box.")
    
# Favorite Toys Tracker Project - Part 5: Add Toys Interactively
# Ask the user to add a new toy (using input())
print("Let's add a new toy to your toy box!")
new_toy = input("Type the name of a toy to add: ")  # Get the toy name from the user
my_toys.append(new_toy)  # Add the new toy to the list
print(f"Added {new_toy}! Now my toys are:", my_toys)

# Store the new toy in PostgreSQL (add it to the database)
conn = psycopg2.connect(dbname="training_db", user="postgres", password="Qwerty123!!", host="localhost", port="5432")
cur = conn.cursor()
cur.execute("INSERT INTO toys (name) VALUES (%s)", (new_toy,))  # Insert the new toy into the toys table
conn.commit()
print(f"Saved {new_toy} to my big toy box in the sky (database)!")
conn.close()

# Count my toys again (using len())
print("I have this many toys now:", len(my_toys))
print("Final toy list:", my_toys)

# Favorite Toys Tracker Project - Part 6: Remove Toys Interactively
# Ask the user to remove a toy (using input())
print("Let's remove a toy from your toy box!")
toy_to_remove = input("Type the name of a toy to remove: ")  # Get the toy name from the user

# Check if the toy is in the list before removing
if toy_to_remove in my_toys:
    my_toys.remove(toy_to_remove)  # Remove the toy from the list
    print(f"Removed {toy_to_remove}! Now my toys are:", my_toys)

    # Remove the toy from PostgreSQL
    conn = psycopg2.connect(dbname="training_db", user="postgres", password="Qwerty123!!", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("DELETE FROM toys WHERE name = %s", (toy_to_remove,))  # Delete the toy from the toys table
    conn.commit()
    print(f"Removed {toy_to_remove} from my big toy box in the sky (database)!")
    conn.close()
else:
    print(f"Sorry, {toy_to_remove} is not in my toy box!")

# Count my toys again (using len())
print("I have this many toys now:", len(my_toys))
print("Final toy list:", my_toys)