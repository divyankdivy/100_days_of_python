print("Welcome to Tip Calculator")

# Ask for the bill
bill = float(input("What was the total bill?\n$"))

# Ask for the tip percentage
tip = int(input("How much percent of tip would you like to pay? 10, 12, 15 or custom select between 1 to 100\n"))

bill_tip = bill*(tip/100)

# Calculate the total bill with tip
total_bill = round(bill + bill_tip,2)

# How many people to split the bill
people = int(input("How many people to split the bill?\n"))

# Calculate the bill on each person
bill_on_each = round(bill/people,2)

print(f"Your total bill is: ${total_bill}")
print(f"Each person should pay: ${bill_on_each}")