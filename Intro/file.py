num1 = 42 # Variable initialization, integer value
num2 = 2.3 # Variable initizalization, float value
boolean = True # Boolean data type, checks if true/false
string = 'Hello World' # String data type
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # Initializes the list "pizza_toppings"
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # Initializes the dictionary "person" and creates keys
fruit = ('blueberry', 'strawberry', 'banana') # Initializes the tuple "fruit"
print(type(fruit)) # Prints the data type of "fruit"
print(pizza_toppings[1]) # Prints "Sausage" from the list "pizza_toppings"
pizza_toppings.append('Mushrooms') # Adds the string "Mushrooms" to the end of the list of "pizza_toppings"
print(person['name']) # Prints "John" from the key "name" in the dictionary "person"
person['name'] = 'George' # Changes the value of the key "name" from "John" to "George"
person['eye_color'] = 'blue' # Adds the key "eye_color" with the value of "blue" to the dictionary "person"
print(fruit[2]) # Prints "banana" from the tuple "fruit"

# Conditional if else statement
if num1 > 45: # If num1 > 45, print "It's greater"
    print("It's greater")
else: # Else print "It's lower" -- If above condition is not met
    print("It's lower")


# Conditional if else utilizing elif
if len(string) < 5: # If the length of the string < 5, print "It's a short word!"
    print("It's a short word!")
elif len(string) > 15: # If the length of the string > 15, print "It's a long word!"
    print("It's a long word!")
else: # Else print "Just right!" -- If above conditionals are not met
    print("Just right!")

for x in range(5): # For loop that prints x from range 0 to 5, but not including 5
    print(x)
for x in range(2,5): # For loop that prints x from range 2 to 5, but not including 5
    print(x)
for x in range(2,10,3): # For loop that prints x from range 2 to 10, incrementing by 3, but not including 10
    print(x)
x = 0
while(x < 5): # While loops that prints x while x < 5
    print(x)
    x += 1 # Increments x in the while loop

pizza_toppings.pop() # Pops the last value in the list "pizza_toppings"
pizza_toppings.pop(1) # Pops the value at index 1 in the list "pizza_toppings"

print(person) # Prints the dictionary for person
person.pop('eye_color') # Removes the key "eye_color"
print(person) # Prints the dictionary for person (no longer has the key for "eye_color")

for topping in pizza_toppings: # For loop that iterates the length of the list
    if topping == 'Pepperoni': # If topping == 'Pepperoni', ignore the index
        continue
    print('After 1st if statement') # If topping != 'Pepperoni', print "After 1st if statement"
    if topping == 'Olives': # If topping == 'Olives', break out of the for loop
        break

def print_hello_ten_times(): # Initialize function without a parameter
    for num in range(10): # For loop that prints "Hello" from range 0 to 10, but not including 10
        print('Hello')

print_hello_ten_times() # Runs the function

def print_hello_x_times(x): # Initalize function with a parameter
    for num in range(x): # For loop that prints "Hello" from range 0 to the value of parameter x, but not including x
        print('Hello')

print_hello_x_times(4) # Runs the function with the given parameter

def print_hello_x_or_ten_times(x = 10): # Initialize function with an initialized parameter that can change if parameter is passed in
    for num in range(x): # For loop that prints "Hello" from range 0 to the value of the parameter x, but not including x (x can be either 10 or passed in value)
        print('Hello')

print_hello_x_or_ten_times() # Runs the function with the default parameter
print_hello_x_or_ten_times(4) # Runs the function with the given parameter


"""
Bonus section
"""

# Have the variable initialized before printing
num3 = 72
print(num3) 

# Convert tuple to list
fruit = list(fruit)
fruit[0] = 'cranberry'
print(fruit)

# Add key
person['favorite_team'] = 'Dallas Cowboys'
print(person['favorite_team'])

# Add values empty values to list to allow index 7 to exist
for x in range(3):
    pizza_toppings.append('')
pizza_toppings.append('Pineapple')
print(pizza_toppings[7])

# Fix indent
print(boolean)

# Continue with fruit as a list, but add print statements to see if the list changes
fruit.append('raspberry')
print(fruit)
fruit.pop(1)
print(fruit)