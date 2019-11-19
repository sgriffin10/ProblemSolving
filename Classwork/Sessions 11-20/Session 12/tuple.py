t = 'a', 'b', 'c'
# print(type(t))
# print(t[0])
# print(t[-1])
# t[0] = 'z' #cant do

t = tuple('Babson')
# print(t)

t = tuple([1,2,3])
# print(t)

tel = '123-456-5432'
# print(tel.split('-'))
# print(tel.split('-')[-1])
a,b,local = tel.split('-')
# print(local)
*a,local = tel.split('-')
# print(local)
# print(a)

tel = '+1-123-345-6533'
# international, *_, local = tel.split('-')
# print(international, local)
# international, local = tel.split('-')

a = 10
b = 20
a,b = b,a
# print(a, b)

# print(divmod(7, 3))

def f():
    return 1, 2 #is a tuple
# print(f())
temp, humidity = f()
# print(temp, humidity)

def sumall(*nums):
    return sum(nums)

# print(sumall(1,2,3))

def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

# print(multiply(1,2,3,4,5,6))

s = set('victoria') 
# print(s)
s.add('e')
# print(s)
s.add('e')
# print(s) #wont change

s = {1, 2, 3}
s1 = {1, 2, 3}
s2 = {2, 3, 4}
# print(s1 & s2)
# print(s1 | s2)
# print(s1.difference(s2))
# print(s1.append(s2))

word = 'bookkeeper'
unique_letter =[]
for letter in word:
    if letter not in unique_letter:
        unique_letter.append(letter)

# print(unique_letter)
# print(set(word))
# print(list(set(word)))
# print(sorted(list(set(word))))

#string and list

name = 'victoria'
name_l = list(name) #str to list
# print(name_l) 
# print(''.join(name_l)) #list to str

#string and dictionary
name_d = dict()
for letter in name:
    name_d[letter] = name_d.get(letter, 0) + 1

# print(name_d)

#string & tuple 

name_t = tuple(name)
# print(name_t)
# print(''.join(name_t))

#string & set

name_s = set(name)
# print(name_s)

#list & tuple

t = [1,2,3,4,5,6,7,8]
# print(zip(name, t))

# for pair in zip(name, t):
#     print(pair)

# print(list(zip(name, t)))

#dictionary and tuples
# print(dict(zip(name,t)))

# name_d2 = dict(zip(name, t))
# print(name_d2.items())

