# def fibonacci(n):
#     if n == 1 or n == 2:
#         return 1
#     else: 
#         return fibonacci(n-1) + fibonacci(n-2)

# # print(fibonacci(35))

# for i in range(1, 10, 1):
#     print(fibonacci(i))

# fac(n) = n * fac(n-1)

def factorial(n):
    first = 1
    for i in range(1, n+1):
        first = first * i
    return first 

for i in range(1, 300, 1):
    print(factorial(i))

# print(factorial(12))


    # for i in range(1, n, 1)
    #     print