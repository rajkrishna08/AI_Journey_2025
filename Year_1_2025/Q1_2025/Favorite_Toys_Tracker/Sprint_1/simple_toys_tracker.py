# Simple Toys Tracker Project
# A fun way to keep track of my favorite toys with a simple list!

# Welcome to my toy shop
print("Welcome to Krishna's Simple Toy Shop!")
print("Let’s play with my favorite toys!")

# My list of favorite toys
my_toys = ["car", "doll", "robot"]

# Show all my toys one by one
print("Here are my favorite toys:")
for toy in my_toys:
    print(toy)

# Count how many toys I have
toy_count = len(my_toys)
print(f"I have {toy_count} toys in my shop!")
if toy_count >= 3:
    print("Wow, that’s a fun collection!")
else:
    print("Let’s add more toys soon!")

# List toys in reverse alphabetical order
print("\nHere are my toys in reverse alphabetical order:")
sorted_toys = sorted(my_toys, reverse=True)
for toy in sorted_toys:
    print(toy)
print(f"Wow, {len(sorted_toys)} toys listed from Z to A!")