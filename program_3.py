def calculate_total_purchase():
    # Get prices of five items
    item1 = float(input("Enter the price of item 1: "))
    item2 = float(input("Enter the price of item 2: "))
    item3 = float(input("Enter the price of item 3: "))
    item4 = float(input("Enter the price of item 4: "))
    item5 = float(input("Enter the price of item 5: "))

    # Calculate subtotal
    subtotal = item1 + item2 + item3 + item4 + item5

    # Calculate sales tax (7%)
    tax = subtotal * 0.07

    # Calculate total
    total = subtotal + tax

    # Display results
    print("Subtotal: $", subtotal)
    print("Sales Tax: $", tax)
    print("Total: $", total)


# Line which calls the above function.
calculate_total_purchase()