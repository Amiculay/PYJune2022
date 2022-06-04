#1 - Returns and prints the value 5
def number_of_food_groups():
    return 5
print(number_of_food_groups())


#2 - Returns an error because "def number_of_days_in_a_week_silicon_or_triangle_sides()" was not initialized
""" def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches()) """


#3 - Returns and prints the value 5
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())


#4 - Returns and prints the value 5
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())


#5 - Prints the value when the function is called, but print(x) prints a blank value
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)


#6 - Prints 3 + 5 => 7
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))


#7 - Returns and prints a string "25"
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))


#8 - Prints the value of b when called, because the value of b > 10, it returns and prints the value 10
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())


#9 - If b < c, return and print 7. If that condition is false, return 14. We return and print 7 for the first call and 14 for the second call.
#    The third and fourth function calls return 7 and 14, which are also added because they are like data types, which then prints 21
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))


#10 - Return and print the value 8
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))


#11 - Each print(b) statement prints 500, but when foobar() is called, it prints 300 because b is a local variable inside the function
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)

#12 - Each print(b) statement prints 500, but when foobar() is called, it prints 300 because b is a local variable inside the function
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)


#13 - Each print(b) statement before foobar() prints 500, but when foobar() is called, it return and prints 300 and changes the value of b to 300. print(b) now prints 300
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)


#14 - foo() prints 1, calls on bar() which prints 3, then prints 2
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()


#15 - when foo is called, it prints 1, calls on bar() which prints 3 and returns 5, then prints 5 and returns 10 for the variable y. When we then print y, we print 10
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)