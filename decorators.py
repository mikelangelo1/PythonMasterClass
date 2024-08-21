# Decorators allows developers to modify the behaviour of a function or a 
# class. 


# Functions are first class objects which means that functions can be used or passed as arguments


### Properites of first class functions
# - You can store the function in a variable.
# - You can pass the function as a parameter to another function
# - you can return the function from a function
# - You can store them in data structures such as hash tables, lists, ...


import time
import math

# decorator to calculate duration
# taken by any function
def calculate_time(func):
    
    def inner1(*args, **kwargs):
        # storing time before function execution
        begin = time.time()
        
        func(*args, **kwargs)
        
        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)
    return inner1


# this can be added to any function present in this case to calculate a factorial

@calculate_time
def factorial(num):
    # sleep 2 seconds because it takes very less time so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))

# calling the function
factorial(10)


def hello_decorator(func):
    def inner1(*args, **kwargs):
        
        print('before execution')
        
        # getting the returned value
        returned_value = func(*args, **kwargs)
        print('After execution')
        
        return returned_value
    return inner1

# Adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b

a, b = 1, 2
print('Sum =', sum_two_numbers(a, b))

### *args and **kwargs means that a tuple of positional arguments or a 
### dictionary of keyword arguments can be passed of any length. This makes
### a general decorator that can decorate a function having any number of arguments.

### Chaining Decorators
# Chaining decorators means decorating a function with multiple decorators


def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner

def decor(func):
    def inner():
        x = func()
        return 2 * x
    return inner


@decor1
@decor
def num():
    return 10

@decor
@decor1
def num2():
    return 10

print(num())
print(num2())