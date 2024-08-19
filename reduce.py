### Reduce
# The reduce(fun, seq) function is used to apply a particular function passed
# in its argument to all of the list elements in the sequence passed along.

# This function is defined in "functools" module.


import functools

lis = [1, 3, 5, 6, 2, 10, 13]

# Using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a + b, lis))

# Using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))


# =====================================================================

### Using Operator Functions

import operator
# operator performs similar function as with lambda function

print("The sum of the list elements is : ", end="")
print(functools.reduce(operator.add, lis))

print("THe product of list elements is : ", end="")
print(functools.reduce(operator.mul, lis))

print("The concatenated product is :", end="")
print(functools.reduce(operator.add, ["geeks", "for", "geeks"]))


### Reduce() vs accumulate()

# Both reduce() and accumulate() can be used to calculate the summation
# of a sequence elements. But there are differnces in the implementation: 
#    """
#      - reduce() is defined in "functools" module, accumulate() in itertools module
#      - reduce() stores the immediate result and only returns the final summmation value.
#    """
   
import itertools
import functools
   
lis = [1, 3, 4, 10, 4]
   
# printing summation using accumulate()
print("The summation of list using accumulate is :", end="")
print(list(itertools.accumulate(lis, lambda x, y: x + y)))
   
# printing summation using reduce()
print("The summation of list using reduce is :",end="")
print(functools.reduce(lambda x, y: x + y, lis))