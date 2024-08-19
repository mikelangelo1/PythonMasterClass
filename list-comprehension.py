### Syntax: newList = [ expression(element) for element in oldList if condition]
numbers = [12, 12, 14, 15]
doubled = [x *2 for x in numbers]
print(doubled)

double_only_even = [x * 2 for x in numbers if x%2 == 0]
print(double_only_even)

## Matrix using list comprehension

matrix = [[i for j in range(3)] for i in range(3)]

print(matrix)


### List comprehensions vs For Loop

# For loop
List = []

for character in 'Machine Learning':
    List.append(character)

print(List)


# List comprehension
compreList = [character for character in 'Machine Learning']
print(compreList)


### Nested List compreshension
matrix = []
 ### Traditional
for i in range(3):

    matrix.append([])

    for j in range(5):
        matrix[i].append(j)
print('matrix', matrix)

### comprehension List

matrix = [[j for j in range(5)] for i in range(3)]

### List comprehensions and Lambda
# lambda expressions are nothing but shorthand representations of python functions.

numbers = []

for i in range(1, 6):
    numbers.append(i*10)

print(numbers)


numbers = [i*10 for i in range(1, 6)]


# Lambda + List comprehension

numbers = list(map(lambda i: i*10, [i for i in range(1, 6)]))


### Display Transpose of 2D-Matrix

twoDMatrix = [[10, 20, 30],
              [40,50, 60 ],
              [70, 80,90]]
# Generate transpose
trans = [[i[j] for i in twoDMatrix] for j in range(len(twoDMatrix[0]))]

print('trans', trans)

### Toggle the case of each character in a String

string = 'Geeks4Geeks'

List = list(map(lambda i: chr(ord(i) ^ 32), string))

print(List)

### Reverse each string in a Tuple

List = [string[::-1] for string in ('Geeks', 'for', 'Geeks')]

print(List)

### Creating a list of Tuples from two separate Lists
names = ["G", "G", "g"] 
ages = [25, 30, 35] 
person_tuples = [(name, age) for name, age in zip(names, ages)]
print(person_tuples)