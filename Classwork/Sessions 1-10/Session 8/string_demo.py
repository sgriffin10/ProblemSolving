team = "New England Patriots"
letter = team [0]
# print(letter)

# print(len(team))
# print(team[1])
# print(team[-1])
# print(team[-20])

# team = "New England Patriots"

index = 0
while index < len(team):
    letter = team[index]
    print(letter)
    index = index + 1

# for letter in team:
#     print(letter)
# print(letter)

# prefixes = "JKLMNOPQ"
# suffix = 'ack'

# for letter in prefixes:
#     if letter == 'O' or letter == 'Q':
#         print(letter+'u'+suffix)
#     else:
#         print(letter + suffix)

# print(team[0:11])
# print(team[12:])
# print(team[::2])

# team[12:20] = "Seahawks" # cant do this

# new_team = team[:12] + "Giants"
# print(new_team)
# print(team)

# def find(word, letter):
#     index = 0 
#     while index < len(word):
#         if word[index] == letter:
#             return index
#         index = index + 1
#     return -1
# print(find(team,'E'))

# def count(s, letter):
#     counter = 0
#     for c in s:
#         if c == letter:
#             counter += 1
#     return counter
# print(count(team, 'a'))
# print(count(team, 'e'))

