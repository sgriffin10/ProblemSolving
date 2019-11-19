def factorial(n):
    first = 1
    for i in range(1, n+1):
        first = first * i
    return first 

# print(factorial(5))

# or

for i in range(1, 5, 1):
    print(factorial(i))