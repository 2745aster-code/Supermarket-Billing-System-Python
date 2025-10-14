# Supermarket Cashier

# Enter Product name & product quantity and store it in a dictionary
def enterProducts():
    product_list = {}
    option_check = True

    while option_check:
        option = input("Enter 'A' to add item and 'Q' to quit: ")

        if option == "A" or option == "a":
            product_name = input("Enter name of the Product: ")
            product_quantity = int(input("Enter quantity of the Product: "))
            product_list.update({product_name: product_quantity})
        elif option == "Q" or option == "q":
            option_check = False
        else:
            print("Enter a valid Option.")

    return product_list

# Enter price of the products
def getPrice(product_name, product_quantity):
    product_price = {
        'Biscuit': 3,
        'Chicken': 5,
        'Egg': 1,
        'Fish': 3,
        'Coke': 2,
        'Bread': 2,
        'Apple': 3,
        'Onion': 3
    }

    total_price = product_price[product_name] * product_quantity
    print(f"{product_name}: ${product_price[product_name]} * {product_quantity} = ${total_price}")
    return total_price

# Discount Calculation
def getDiscount(total_bill, membership):
    discount = 0
    if total_bill >= 25:
        if membership == "G" or membership == "g":
            discount = 20
            discount_price = (total_bill * discount) / 100
            total_bill = total_bill * 0.80
        elif membership == "S" or membership == "s":
            discount = 10
            discount_price = (total_bill * discount) / 100
            total_bill = total_bill * 0.90
        elif membership == "B" or membership == "b":
            discount = 5
            discount_price = (total_bill * discount) / 100
            total_bill = total_bill * 0.95
        print(f"Your total bill: {total_bill + discount_price}")
        print(f"{discount}% off for {membership.upper()} mebership on total amount: ${discount_price}")
    else:
        print("No Discount on amount less than $25.")
    return total_bill

# Bill Finalize
def makeBill(product_list, membership):
    total_bill = 0
    for key, values in product_list.items():
        total_bill += getPrice(key, values)
    total_bill = getDiscount(total_bill, membership)

    print(f"The total amount is ${total_bill}")

product_list = enterProducts()
membership = input("""Membership Details
    1. Gold Membership (G / g)
    2. Silver Membership (S / s)
    3. Bronze Membership(B / b)
    4. No Membership (N / n)
    Enter the membership you have: """)
makeBill(product_list, membership)