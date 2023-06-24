fruits = [
    {"name": "Apple", "price": 2},
    {"name": "Grape", "price": 1},
    {"name": "Orange", "price": 3}
]

print("Welcome to the GC Fruit Market!")
name = input("What is your name? ")

cart = {}
subtotal = 0
tax_rate = 0.05

while True:
    print("\nWelcome, {}! Which fruit would you like to buy?".format(name))
    print("Fruit          Price")
    for i, fruit in enumerate(fruits, start=1):
        print("{}. {}         ${}".format(i, fruit["name"], fruit["price"]))

    choice = input("> ")

    if choice.isdigit() and 1 <= int(choice) <= len(fruits):
        fruit_index = int(choice) - 1
        selected_fruit = fruits[fruit_index]

        if selected_fruit["name"] in cart:
            cart[selected_fruit["name"]] += 1
        else:
            cart[selected_fruit["name"]] = 1

        subtotal += selected_fruit["price"]
        print("You bought {} {} at ${} ".format(
            cart[selected_fruit["name"]],
            selected_fruit["name"],
            selected_fruit["price"]
        ))

        buy_more = input("Would you like to buy another piece of fruit? (y/n): ")
        if buy_more.lower() != "y":
            break

    else:
        print("Invalid choice. Please try again.\n")

# Print the receipt
print("\nOrder for {}:\n".format(name))
for fruit, quantity in cart.items():
    fruit_price = next((item["price"] for item in fruits if item["name"] == fruit), None)
    fruit_subtotal = quantity * fruit_price
    print("{} {}(s) at ${} apiece".format(quantity, fruit, fruit_price))

tax = subtotal * tax_rate
total_cost = subtotal + tax

print("Sub Total: ${}".format(subtotal))
print("5% Tax: ${}".format(tax))
print("Total: ${}".format(total_cost))
