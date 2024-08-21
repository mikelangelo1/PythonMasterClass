## Hoe Decorator with parameters is implemented

# def decorators(*args, **kwargs):
#     def inner(func):
#         '''
#             do operaions with func
#         '''
        
#         return func
#     return inner


# @decorators(params)
# def func():
#     """
#         function implementation
#     """
    
# # Example

def decorator(*args, **kwargs):
    print("Inside decorator")
    
    def inner(func):
        
        # code functionality here
        print("Inside inner function")
        print("I like", kwargs['like'])
        
        func()
        
    return inner


@decorator(like = "geeksforgeeks")
def my_func():
    print("Inside function")



def decorator_func(x, y):
    
    def Inner(func):
        
        def wrapper(*args, **kwargs):
            print("I like Geeksforgeeks")
            print("Summation of values - {}".format(x + y))
            
            func(*args, **kwargs)
            
        return wrapper
    return Inner


# Not using decorator
def my_fun(*args):
    for ele in args:
        print(ele)
        
        
# # another way of using decorators
decorator_func(12, 15) (my_fun) ('Geeks', 'for', 'Geeks')



# Multi-level Decorators

def decodecorator(dataType, message1, message2):
    def decorator(fun):
        print(message1)
        def wrapper(*args, **kwargs):
            print(message2)
            if all([type(arg) == dataType for arg in args]):
                return fun(*args, **kwargs)
            return "Invalid input"
        return wrapper
    return decorator


@decodecorator(str, "Decorator for 'stringJoin'", "stringJoin started ...")
def stringJoin(*args):
    st = ''
    for i in  args:
        st += i
    return st


@decodecorator(int, "Decorator for 'summation'\n", "Summation started")
def summation(*args):
    summ = 0
    for arg in args:
        summ += arg
    return summ

print(stringJoin("I ", 'like ', "Geeks", 'for', "geeks"))
print()
print(summation(19, 2, 8, 533, 42, 23, 323))