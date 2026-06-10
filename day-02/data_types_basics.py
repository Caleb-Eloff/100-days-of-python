# Subscript operator[] is used to access individual characters
# in a string.
print("Hello"[1])
# Output: e
print("Hello"[-1])
# Output: o

# Strings
print("123" + "456")
# Output: 123456
# Strings are indicated by quotes, and they can be concatenated
# using the + operator.

# Integers
print(123 + 456)
# Output: 579
# Integers are whole numbers without a decimal point.

# Large Integers
print(100_232_300)
# Output: 100232300
# Python allows you to use underscores in numeric literals for
# better readability.

# Float
print(3.14)
# Output: 3.14
# Floats are numbers that contain a decimal point.

# Boolean
print(True)
# Output: True
print(False)
# Output: False
# Booleans represent truth values and can be either True or
# False.

print(type("Hello"))
# Output: <class 'str'>
print(type(123))
# Output: <class 'int'>
print(type(3.14))
# Output: <class 'float'>
print(type(True))
# Output: <class 'bool'>
# The type() function is used to determine the data type of a
# value. It returns the class type of the object passed as an
# argument.

print(int("123") + int("456"))
# Output: 579
# The int() function converts a string to an integer, allowing
# for arithmetic operations to be performed on the numeric values
# represented as strings.
print("Number of letters in your name: " + str(len("Enter your name")))
# Output: Number of letters in your name: (Value)
# The str() function converts a value to a string, which is
# necessary for concatenating it with other strings. The len()
# function returns the number of characters in a string, which can
# be useful for various applications, such as counting the number of
# letters in a name.
