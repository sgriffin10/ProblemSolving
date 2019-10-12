name = ['Emely', 'Krishna','Patrick']
grades = [90, 80, 65]
names = ['Emely', 'Krishna','Patrick']

# for i in range(3):
#     print(names[i],grades[i])

grades = dict()

# print(type(grades))

grades['Emely'] = 90

# print(grades)

grades = {'Emely':90, 'Krishna':80, 'Patrick':65}
# print(grades)

names = dict()

for name in names:
    import random
    names[name] = random.randint(0,99)

print(names)