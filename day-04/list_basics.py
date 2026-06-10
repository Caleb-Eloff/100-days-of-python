states_of_ameria = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts",
                    "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina",
                    "Rhode Island", "Vermont"]
print(states_of_ameria[1])  
# Output: Pennsylvania
# The index starts at 0, so the second item is at index 1.

print(states_of_ameria[-1])
# Output: Vermont
# The index -1 refers to the last item in the list.

states_of_ameria[1] = "Pencilvaynia"
print(states_of_ameria[1])
# Output: Pencilvaynia
# We can change the value of an item in the list by assigning a new value to a
# specific index. In this case, we changed "Pennsylvania" to "Pencilvaynia".

states_of_ameria.append("Florida")
print(states_of_ameria)
# Output: ['Delaware', 'Pencilvaynia', 'New Jersey', 'Georgia', 'Connecticut', 'Massachusetts', 'Maryland',
# 'South Carolina', 'New Hampshire', 'Virginia', 'New York', 'North Carolina', 'Rhode Island', 'Vermont', 'Florida']
# The append() method adds a new item to the end of the list. In this case, we added "Florida" to the list of states.

length_of_states = len(states_of_ameria)
print(length_of_states)
# Output: 15
# The len() function returns the number of items in the list. In this case, there are 15 states in the list after
# we added Florida.

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
# Output: [['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears'], ['Spinach',
# 'Kale', 'Tomatoes', 'Celery', 'Potatoes']]
# We can create a list of lists, which is a list that contains other lists as its items. In this case,
# dirty_dozen is a list that contains the fruits list and the vegetables list as its items. When we print 
# dirty_dozen, it shows the two lists nested within it.