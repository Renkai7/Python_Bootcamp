print("Welcome to the tip calculator.")
bill_amount = float(input("What was the total bill? $"))
tip_input = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))

tip_percentage = (tip_input / 100) * bill_amount
bill_with_tip = bill_amount + tip_percentage
bill_split_amt = round(bill_with_tip / split, 2)

print(f"Each person should pay: ${bill_split_amt}")


