bill = float(input("Welcome to the tip calculator!\nWhat was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

total_bill = (bill + (bill * (tip / 100))) / people
print(f"Each person should pay: ${round(total_bill, 2)}") 