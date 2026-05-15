print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni on your pizza? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")
# This code calculates the final bill for a pizza order based on
# the size of the pizza, whether the customer wants pepperoni, 
# and whether they want extra cheese. It uses if statements to 
# add the appropriate amounts to the bill based on the customer's 
# choices.