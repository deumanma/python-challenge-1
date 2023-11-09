# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

menu_dashes = "-" * 42

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered

customer_order = []

# Launch the store and present a greeting to the customer
print("Welcome to the Betsy's food truck.")
# inserting a line break to break up the visual output to the customer
"\n"
print("   ")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")
    "\n"
    print("   ")


    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")
    "\n"
    print("   ")

    #This block of comments was code I used to create a quit loop for myself 
    # got this code from openAI chat gpt, as i got myself into a 
    # neverending loop and i had to run it so many times it 
    # was easier than quitting out of terminal.
    #  # # Get the customer's input
    # menu_category = input("Type menu number to view menus or q to quit: ")

    # # Exit the loop if user typed 'q'
    # if menu_category == 'q':
    #     break

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            menu_selection = input(f"What item would you to order from {menu_category_name}? ")
            "\n"
            print("   ")

            # 3. Check if the customer typed a number
            if menu_selection.isdigit(): 

                # Convert the menu selection to an integer
                menu_selection = int(menu_selection)

                # 4. Check if the menu selection is in the menu items
            if menu_selection in menu_items.keys():
                    # Store the item name as a variable
                food_item = menu_items[menu_selection]['Item name']
                item_price = float(menu_items[menu_selection]['Price'])


                    # Ask the customer for the quantity of the menu item

                customer_quantity = input(f"How many {food_item}'s would you like to order? ")
                "\n"
                print("   ")

                    # Check if the quantity is a number, default to 1 if not
                if customer_quantity.isdigit() and int(customer_quantity) >0:
                        customer_quantity = int(customer_quantity)
                else: customer_quantity = 1


                    # Add the item name, price, and quantity to the order list
                customer_order.append({'Item Name': food_item, 'Price': item_price, 'Quantity': customer_quantity})

                    # Tell the customer that their input isn't valid

            else: print("Your selection wasn't valid please try again." )


                # Tell the customer they didn't select a menu option

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")
        "\n"
        print("   ")

        # 5. Check the customer's input
        match keep_ordering:
            case "y":
                place_order = True
                break
            case "yes":
                place_order = True
                break
            case "Y":
                place_order = True
                break
            case "no":
                place_order = False
                break
            case "N":
                place_order = False
                break
            case "n":
                place_order = False
                print("Thank you for your order at Betsy's Food Truck!")
                break
                
                   
                # Keep ordering

                # Exit the keep ordering question loop

                # Complete the order

                # Since the customer decided to stop ordering, thank them for
                # their order

                # Exit the keep ordering question loop
                #These instructions were all completed from lines 193-212

                # Tell the customer to try again
            case _:
                print("Please try again.")

                

"\n"
print("   ")
# Print out the customer's order
print("This is what we are preparing for you. Yum!")
"\n"
print("   ")


# Uncomment the following line to check the structure of the order
#print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order

for order_item in customer_order:
    # 7. Store the dictionary items as variables
    food_item, item_price, customer_quantity = order_item['Item Name'], order_item['Price'], order_item['Quantity']


    # 8. Calculate the number of spaces for formatted printing
    food_space_str_len = 26 - len(food_item)
    price_space_str_len = 9 - len(str(item_price))

    # 9. Create space strings
    food_spaces = food_space_str_len * " "
    price_spaces = price_space_str_len * " "

    # 10. Print the item name, price, and quantity
    print(f"{food_item}{food_spaces} | {item_price}{price_spaces} | {customer_quantity}")

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
total_cost = sum([item['Price']*item['Quantity'] for item in customer_order])
print(f"\nThe total cost of your order will be ${total_cost: .2f}.")