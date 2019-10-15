# Exercise 4.1 

# random_dict = dict()
def create_dict():
    words = {}
    f = open('Classwork/Session 11/Exercises/words.txt')
    for line in f:
        word = line.strip()
        words[word] = 0
    return words

test_dict = create_dict()



def check_word(word, d):
    return word in d

if __name__ == "__main__":
    test_dict = create_dict
    # for w in test_dict:
#   print(w, test_dict[w])

#   for w, v in test_dict.items():
#   print(w, v)
    word = input('Enter a word:')
    if check_word(word, test_dict):
        print(f'yes, the word {word} is in the dictionary')
    else:
        print(f'Sorry, the word {word} is not here')

# def check_dict(word, dictionary):
#     if word in dictionary:
#         return True
#     else:
#         return False

# print(check_dict('hello', test_dict))
# print(check_dict('zhi', test_dict))

#Exercise 4.2

def has_duplicates(word, dictionary):
    if len(word) > len(set(word)):
        return True
    return False

# print(has_duplicates('hello', test_dict))
# print(has_duplicates('shot', test_dict))



