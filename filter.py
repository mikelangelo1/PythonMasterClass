### Filter
# Syntax: filter(function, sequence)
def fun(variable):
    letters = ['a', 'b', 'c', 'd', 'e']
    if variable in letters:
        return True
    else:
        return False
    
# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

# using filter function
filtered = filter(fun, sequence)
print('The filtered letters are:')
for s in filtered:
    print(s)


### Filter funtion with lambda

seq = [0, 1, 2, 3, 5, 8, 13]

result = filter(lambda x: x % 2 != 0, seq)
print(list(result))