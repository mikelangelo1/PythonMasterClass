### Dictionary comprehension
## Syntax: { key: value for (key, value) in iterable}

keys = ['a','b','c','d','e']
values = [1,2,3,4,5] 

myDict = { k:v for (k, v) in zip(keys, values)}

print(myDict)

### Using fromKeys() Method -> returns a dictionary with specific keys and values
dic=dict.fromkeys(range(5), True)
print('dic', dic)


### Using conditional statements in dictionary comprehension
newDict = { x: x**3 for x in range(10) if x**3 % 4 == 0}
print('newDict', newDict)

### Using nested ductionary comprehension
l="GFG"

dic = {
    x: {y: x + y for y in l} for x in l
}

print('dic2', dic)
