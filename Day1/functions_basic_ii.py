# Countdown - Countdown from input to 0
def countdown(num):
    numberList = []
    while num >= 0:
        numberList.append(num)
        num -= 1
    return numberList
print(countdown(5))

# Print and return a list with two numbers, print the first value and return the second value
def print_and_return(numberList):
    print(numberList[0])
    return(numberList[1])
value = print_and_return([1,2])
print("This is our return value: {}" .format(value))

# Accepts a list and returns the sum of the first value and the length of the list
def first_plus_length(numberList):
    return numberList[0] + len(numberList)
print(first_plus_length([1, 2, 3, 4, 5]))

# Accepts a list and creates a new list containing only values greater than the second value in the first list and prints its length. If the list < 2, return False.
def values_greater_than_second(numberList):
    if len(numberList) < 2:
        return False
    
    newList = []
    counter = 0
    for i in range(len(numberList)):
        if numberList[i] > numberList[1]:
            newList.append(numberList[i])
            counter += 1
    print(counter)
    return newList
values_greater_than_second([3])
print(values_greater_than_second([5,2,3,2,1,4]))

# Accepts two integers as parameters, size of list and values of the list. Return a list whose length is equal to the given size, and the values are all equal to the given value.
def length_and_value(size, value):
    numberList = []
    while size > 0:
        numberList.append(value)
        size -= 1
    return numberList
print(length_and_value(4, 7))
print(length_and_value(6, 2))
