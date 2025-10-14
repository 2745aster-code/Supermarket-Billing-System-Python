# 🛒 Supermarket Billing System (Python)

A simple command-line based billing system written in Python.

## 🚀 Features
- Add multiple products and quantities.
- Calculates total price based on predefined product prices.
- Applies membership-based discounts:
  - 🥇 Gold (20%)
  - 🥈 Silver (10%)
  - 🥉 Bronze (5%)
- Validates inputs and prints a clear bill summary.

## 💻 Technologies
- Python 3
- Dictionaries & Functions
- Conditional Logic

## 📸 Sample Output
Enter 'A' to add item and 'Q' to quit: a
Enter name of the Product: Biscuit
Enter quantity of the Product: 1
Enter 'A' to add item and 'Q' to quit: a     
Enter name of the Product: Chicken
Enter quantity of the Product: 2
Enter 'A' to add item and 'Q' to quit: a
Enter name of the Product: Egg
Enter quantity of the Product: 3
Enter 'A' to add item and 'Q' to quit: a
Enter name of the Product: Fish
Enter quantity of the Product: 4
Enter 'A' to add item and 'Q' to quit: a
Enter name of the Product: Coke
Enter quantity of the Product: 5
Enter 'A' to add item and 'Q' to quit: a
Enter name of the Product: Bread
Enter quantity of the Product: 6
Enter 'A' to add item and 'Q' to quit: a
Enter name of the Product: Apple
Enter quantity of the Product: 7
Enter 'A' to add item and 'Q' to quit: a
Enter name of the Product: Onion
Enter quantity of the Product: 8
Enter 'A' to add item and 'Q' to quit: q
Membership Details
    1. Gold Membership (G / g)
    2. Silver Membership (S / s)
    3. Bronze Membership(B / b)
    4. No Membership (N / n)
    Enter the membership you have: G
Biscuit: $3 * 1 = $3
Chicken: $5 * 2 = $10
Egg: $1 * 3 = $3
Fish: $3 * 4 = $12
Coke: $2 * 5 = $10
Bread: $2 * 6 = $12
Apple: $3 * 7 = $21
Onion: $3 * 8 = $24
Your total bill: 95.0
20% off for G mebership on total amount: $19.0
The total amount is $76.0

## 🧠 Future Enhancements
- Add color and table formatting using `colorama` and `tabulate`
- Add date/time and save bill as text file
- Add option to remove or update items before checkout

---

✅ **Author:** Asish  
📍 **GitHub:** [github.com/2745aster-code](https://github.com/2745aster-code)
