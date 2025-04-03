# Step 1: Make a box with a word toy and do word tricks
word_box = "hello, krishna!"  # Put a word toy in the box
print("My word box has:", word_box)  # Show the box
print("Shout the word:", word_box.upper())  # Make it shout
print("Make it fancy:", word_box.capitalize())  # Make the first letter big
print("Swap krishna for world:", word_box.replace("krishna", "world"))  # Swap a word

# Step 2: Make a box with a shelf of toys and do shelf tricks
toy_shelf = ["car", "ball", "doll"]  # A shelf with 3 toys in the box
print("My toy shelf has:", toy_shelf)  # Show the shelf
toy_shelf.append("teddy")  # Add a teddy bear
print("After adding teddy:", toy_shelf)  # Show the shelf again
toy_shelf.remove("ball")  # Take the ball away
print("After taking ball away:", toy_shelf)  # Show the shelf again
print("How many toys I have:", len(toy_shelf))  # Count the toys