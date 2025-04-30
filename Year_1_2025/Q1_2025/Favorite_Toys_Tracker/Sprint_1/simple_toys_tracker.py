# Welcome message for Krishna's toy shop
print("Welcome to Krishna's Simple Toy Shop!")
print("Let’s play with my favorite toys!")

# List of my favorite toys
my_toys = ["car", "doll", "robot"]
print("Here are my favorite toys:")
for toy in my_toys:
    print(toy)

# Count the number of toys and check if it's a fun collection
toy_count = len(my_toys)
print(f"I have {toy_count} toys in my shop!")
if toy_count >= 3:
    print("Wow, that’s a fun collection!")
else:
    print("Let’s add more toys soon!")

# Display toys with their indices (e.g., Toy 1, Toy 2)
print("\nMy toys with indices:")
for i in range(len(my_toys)):
    print(f"Toy {i + 1}: {my_toys[i]}")

# Function to calculate the total price of toys
def calculate_total_price(count, price):
    return count * price

# Calculate and display the total price
total = calculate_total_price(len(my_toys), 10)
print(f"\nTotal price using function: {total} dollars")

# Format toy names in uppercase
print("\nFormatted toy names:")
for toy in my_toys:
    formatted_toy = toy.upper()
    print(f"Toy: {formatted_toy}")

# Dictionary to store toy details (price and weight)
toy_details = {
    "car": {"price": 10, "weight": 2},
    "doll": {"price": 15, "weight": 1},
    "robot": {"price": 25, "weight": 3}
}
print("\nToy details:")
for toy, details in toy_details.items():
    print(f"{toy}: Price = {details['price']} dollars, Weight = {details['weight']} kg")

# Check toy availability using a dictionary
toy_availability = {toy: True for toy in my_toys}
print("\nToy availability:")
for toy, available in toy_availability.items():
    print(f"{toy}: {'Available' if available else 'Not Available'}")

# Check if all toys are available using boolean logic
all_available = all(toy_availability.values())
print(f"All toys available: {all_available}")


# this is my toy shop name  
# Change the shop name to something new
shop_name = "Krishna's Magic Toy Shop"
print("My new shop name is:")
print(shop_name)

# Add my name to the shop
my_name = "Krishna"
shop_name = my_name + "'s Magic toy shop"
print("shop name wiht my name:")
print(shop_name)  
