### The term Recursion can be defined as the process of defining something 
## in terms of itself. In simple words, it is a process in which a function
## calls itself directly or indirectly



## Advantages of using recursion
# - A complicated function can be split down into smaller sub-problems 
#   utilizing recursion
# - Sequence creation is simpler through recursion than utilizing any nested iteration
# - Recursive functions render the code look simple and effective

def recursive_fibonacci(n):
    if n <= 1:
        return n
    else: 
        return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))
    
n_terms = 10

# check if the number of terms is valid
if n_terms <= 10:
    print("Invalid input ! Please input a positive value")
else: 
    print("Fibonacci series:")
    for i in range(n_terms):
        print(recursive_fibonacci(i)) 