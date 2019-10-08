a = [] #is a list
# print(type(a))
# print(len(a))

a = [10, 20, 30, 40]
b = ['spam', 2.0, 5, [10, 20]] 
# print(len(b[-1]))
# print(b[0])
# print(b[-1])
# print(b[3])
# print(b[3][0]) # print first value of b[3] list
# b[3] = [10]
# print(b[3])

AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
# print(AFC_east)
AFC_east[2] = 'New York Giants'
# print(AFC_east)

gang = 'Buffalo Bills' in AFC_east
# print(gang)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', ['Ruby','On Rail'], 'PHP'],
    ['Adam', 'Bart', 'Lisa']    
]
# print(L[1][2][1][2])

# for team in AFC_east:
#     # print(team)
#     for letter in team:
#         print(letter)

numbers = [2019, 10, 8, 3, 43]
for number in numbers:
    number = number * 2
# print(numbers)


# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 2
    
# print(numbers)

my_list = ['spam', 1, ['New England Patriots', \
                       'Buffalo Bills', 'Miami Dolphins', \
                       'New York Giants'], \
           [1, 2, 3]]
# print(len(my_list))

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
# print(c)

# print([0] * 4)
# print(['Tom Brady', 'Bill Belichick']*3)

t = ['a', 'b', 'c', 'd', 'e', 'f']
# print(t[1:3])
# print(t[0:4])
# print(t[3:6])
# print(t[::2]) #first colon is whole list; second colon means skip 1

t = ['a', 'b', 'c', 'd', 'e', 'f']
# t[1:3] = ['x', 'y']
# print(t)

t[1:3] = ['Shaun', 'Jinna']
# print(t)

t[1:3] = 'Nico'
# print(t)
t = ['a', 'Victoria', 'd', 'e', 'f']
t[1] = 'Nico'
# print(t)

# print(type(t[1:3]))
# print(type(t[1]))

row_3 = ['TeenBoi', 'Spencer', 'Xintong']
# row_3.append('ShaunyBoi')
# print(row_3)

boys = ['Shaun', 'Brian', 'Patrick']
# row_3.extend(boys)
# print(row_3)
row_3.append(boys)
# print(row_3)

t = ['a', 'b', 'c', 'd']
x = t.pop(1)
# pop modifies the list and returns 
# the element that was removed. 
# print(x)
# print(t)

the_abandoned_name = t.pop(2)
# print(the_abandoned_name)

del t[1]
# print(t)



# print(('sgriffin4@babson.edu').split('@')[0])