print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")
# The if statement checks if the height is greater than or equal
# to 120 cm. If it is, it prints a message allowing the person
# to ride the rollercoaster. If not, it prints a message saying
# they need to grow taller.

bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your photo costs $3. Your total is ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")
# This code adds a billing system to the rollercoaster ride. 
# It checks the age of the rider to determine the ticket price
# and also asks if they want a photo taken, which adds an 
# additional cost to the bill. Finally, it prints the total
# cost.
