#Exercise 1

# import math


# def sum(x):
#     n = 0
#     for i in range(1, x+1):
#         if (i % 2 == 0):
#             n = n + i
#         else: 
#             pass
#     return(n)
    
# print(sum(1000))

#sum to 100 is 5,050
#sum to 1000 is 500,500
#sum of all odd numbers is 250,000
#sum of even numbers is 250,500

# def countdown(n):
#     while n>0:
#         print(n)
#         n = n - 1
#     print("Blastoff!")

# countdown(1000)

# iteration = 0
# count = 0
# while iteration < 5:
#     # count = 0
#     for letter in "hello, world":
#         count += 1
#         if iteration % 2 == 0:
#             break
#     print("Iteration" + str(iteration) +  ": count is " + str(count))
#     iteration += 1

#print count: 12, 24, 36, 48, 60 (12 increments)
#print count: 12, 12, 12, 12, 12 (0 increments)
#executed 4 times; largest iteration is 4; largest count value is 12; smallest count value is 1

# count = 0 
# while n < 101:
#     sum = 0
#     sum += n
#     print(sum)

# n=0
# sum = 0
# while n < 11: #change value n
#     sum = sum + n
#     n += 1
# print(sum)        
    
# n=0
# sum = 0
# while n < 11: #change value n  
#     for n in range(1, 11, 2):
#         sum = sum + n
#         n += 1
# print(sum)        

  
# def mysqrt(a):
#     epsilon = 0.00000000000000001
#     x = a
#     while True:
#         y = (x + a/x) / 2
#         if abs(y-x) < epsilon:
#             break
#         x = y
#     return x   
        
# def square_root_method(a):
#     print(mysqrt(a))
#     print(math.sqrt(a))
#     diff = int(mysqrt(a)) - int(math.sqrt(a))
#     print(abs(diff))

# for i in range (1,10):
#     square_root_method(i)
    