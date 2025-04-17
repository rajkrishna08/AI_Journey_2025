# My simple toy tracker, like a magic toy box!
toys = []  # Empty list to store toys and prices, like a toy box

def add_toy_with_price(toy_name, price):
    """Adds a toy and its price to the toy box, like a smart helper."""
    try:
        price = float(price)  # Make sure price is a number
        if price < 0:
            print(f"Oops! Price for '{toy_name}' can't be negative!")
            return
        toys.append({"name": toy_name, "price": price})  # Add toy as a dictionary
        print(f"Added '{toy_name}' with price ${price:.2f} to the toy box! 🌟")
    except ValueError:
        print(f"Please enter a valid number for the price of '{toy_name}'!")

def show_total_value():
    """Shows the total value of all toys in the toy box, like a smart counter."""
    if not toys:
        print("Your toy box is empty! Add some toys first!")
        return
    total = sum(toy["price"] for toy in toys)
    print(f"Total value of your toy box is ${total:.2f}! 💰")

# Add some toys to start
add_toy_with_price("doll", 12.50)  # Add a doll
add_toy_with_price("truck", 15.00)  # Add a truck
add_toy_with_price("teddy bear", 9.00)  # Add a teddy bear

# Show the toy box
print("My toy box:", toys)

# Show the total value
show_total_value()

# Remove a toy
for toy in toys:
    if toy["name"] == "doll":
        toys.remove(toy)
        print(f"Removed 'doll' from the toy box!")
        break

# Show the toy box and total value again
print("My toy box after removing doll:", toys)
show_total_value()