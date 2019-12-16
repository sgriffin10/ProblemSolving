# fin = open("Classwork/session09/words.txt")
# line = fin.readline()
# word = line.strip()
# print(word)

# for line in fin:
#     word = line.strip()
#     print(word)


def find_long_words():
    """
    prints only the words with more than 20 characters
    """
    f = open('Classwork/session09/words.txt')
    for line in f:
        word = line.strip()
        if len(word)>15:
            print(word, len(word))


# find_long_words()


def has_no_e(word):
    """
    returns True if the given word doesn’t have the letter "e" in it
    """
    for letter in word:
        if letter == 'e' or letter == 'E':
            return False
    return True

# print(has_no_e('Babson'))
# print(has_no_e('College'))
# print(has_no_e('EA'))


def find_words_no_e():
    """
    returns the percentage of the words that don't have the letter "e"
    """ 
    f = open('Classwork/session09/words.txt')
    counter = 0
    num_of_words = 0 
    num_of_words_with_e = 0
    for line in f:
        num_of_words += 1
        word = line.strip()
        if has_no_e(word):
            counter += 1
        else:
            num_of_words_with_e += 1
    return counter/num_of_words
            

# print('The percentage of the words with no "e" is {:.2f}%.'.format(
#     find_words_no_e()*100))


def avoids(word, forbidden):
    """
    returns True if the given word does not use any of the forbidden letters
    """
    for letter in word:
        if letter in forbidden:
            return False
    return True


# print(avoids('Babson', 'abcde'))
# print(avoids('College', 'e'))
# print(avoids('Boston', 'e'))


def find_words_no_vowels():
    """
    returns the percentage of the words that don't vowel letters
    """
    f = open('Classwork/session09/words.txt')
    num_of_words_no_vowel = 0
    num_of_words = 0 
    for line in f:
        num_of_words += 1
        word = line.strip()
        if avoids(word,'aeiou'):
            num_of_words_no_vowel += 1
    return num_of_words_no_vowel/num_of_words


# print('The percentage of the words without vowel letters is {:.2f}%.'.format(
#     find_words_no_vowels()*100))


def uses_only(word, available):
    """
    takes a word and a string of letters, and that returns True if the word
    contains only letters in the list.
    """
    for letter in word:
        if letter not in available:
            return False
    return True

# print(uses_only('Babson', 'aBbsonxyz'))
# print(uses_only('college', 'aBbsonxyz'))

def find_words_only_use_planet():
    f = open('Classwork/session09/words.txt')
    num_of_words_only_use_planet = 0
    for line in f:
        word = line.strip()
        if uses_only(word, 'planet'):
            num_of_words_only_use_planet += 1
            print(word)
    return num_of_words_only_use_planet

# print('Number of words that use only letter from "planet" is', find_words_only_use_planet())

def uses_all(word, required):
    """
    takes a word and a string of required letters, and that returns True if
    the word uses all the required letters at least once.
    """
    # for letter in required if letter not in word return False:
    for letter in required:
        if letter not in word:
            return False
    return True
  
# print(uses_all('Babson', 'abs'))
# print(uses_all('college', 'abs'))
# print(uses_all('Babson', 'aeoiu'))
# print(uses_all('Babesonious', 'aeoiu'))


def find_words_using_all_vowels():
    """
    return the number of the words that use all the vowel letters
    """
    f = open('Classwork/session09/words.txt')
    num_of_words_only_vowels_ = 0
    for line in f:
        word = line.strip()
        if uses_all(word, 'aeiou'):
            num_of_words_only_vowels_ += 1
            # print(word)
    return num_of_words_only_vowels_


# print('The number of words that use all the vowels:',
#       find_words_using_all_vowels())


def is_abecedarian(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    left = word[0]
    for letter in word[1:]:
        if left > letter:
            return False
        left = letter
    return True



# print(is_abecedarian('abs'))
# print(is_abecedarian('college'))


def find_abecedarian_words():
    f = open('Classwork/session09/words.txt')
    counter = 0
    current_longest_word = ''
    for line in f:
        word = line.strip()
        if is_abecedarian(word):
            # print(word)
            counter += 1
            if len(word) > len(current_longest_word):
                current_longest_word = word
    return counter, current_longest_word

# print(find_abecedarian_words())

# def find_abecedarian_words():
#     """
#     returns the number of abecedarian words and the longest abecedarian word
#     """
#     f = open('Classwork/session09/words.txt')
#     num_of_words_abecedarian = 0
#     for line in f:
#         word = line.strip()
#         index = ''
#         if is_abecedarian(word) == True:
#             num_of_words_abecedarian += 1
#         # if len(index) < len(word) and is_abecedarian(word) == True:
#         #     index = word
#         # print(word)
#         # # if is_abecedarian(word) and len(word) > 6:
#         # #     print(word)
#     return num_of_words_abecedarian 

# # print(find_abecedarian_words())

# def find_longest_abecedarian_words():
#     f = open('Classwork/session09/words.txt')
#     index = ''
#     for line in f:
#         word = line.strip()
#         if is_abecedarian(word) == True:
#             if len(word) > len(index):
#                 index = word
#     return index

# print('The longest abecedarian word is', find_longest_abecedarian_words(), 'and the amount of abecedarian words is', find_abecedarian_words())

def is_abecedarian_using_recursion(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    if len(word) <= 1:
        return True
    if word [0] > word [1]:
        return False
    return is_abecedarian_using_recursion(word[1:])

# print(is_abecedarian_using_recursion('Babson'))
# print(is_abecedarian_using_recursion('abbnos'))

def is_abecedarian_using_while(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    i = 0
    while i < len(word)-1:
        if word[i + 1] < word[i]:
            return False
        i += 1
    return True
    # word[i] 

print(is_abecedarian_using_while('babson')) 
print(is_abecedarian_using_while('abbnos')) 

