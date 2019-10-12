# Exercise 4.1 

random_dict = dict()
def create_dict():
    f = open('Classwork/Session 11/Exercises/words.txt')
    for line in f:
        words = line.strip()
        random_dict[words] = words
    return random_dict

test_dict = create_dict()

def check_dict(word, dictionary):
    if word in dictionary:
        return True
    else:
        return False

# print(check_dict('hello', test_dict))
# print(check_dict('merppppp', test_dict))

#Exercise 4.2

def has_duplicates(word, dictionary):
    if len(word) > len(set(word)):
        return True
    return False

# print(has_duplicates('hello', test_dict))
# print(has_duplicates('shot', test_dict))



