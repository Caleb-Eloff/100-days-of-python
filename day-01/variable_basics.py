name = input("What is your name?")
print("Hello " + name + "!")
# In this code, we are using the input() function to get input
# from the user, which is then stored in the variable name as
# a string. This variable is then used in the print() function
# to create a personalized greeting.

name_length = len(name)
print("The name variable contains a total of " + str(name_length) + " characters.")
# In this code, we are using the len() function to get the
# length of the string stored in the name variable. The len()
# function returns an integer representing the number of characters
# in the string. We then convert this integer to a string using
# the str() function so that we can concatenate it with the
# other strings in the print() function. The final output
# will then display the length of the name variable.