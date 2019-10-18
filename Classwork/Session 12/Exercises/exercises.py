#Exercise 2.1

# import operator
# word = input("Enter a word:")

# letter_d = dict()
# for letter in word:
#     letter_d[letter] = letter_d.get(letter, 0) + 1

# sorted_d = sorted(letter_d.items(), key = operator.itemgetter(1),reverse=True)
# print(sorted_d)

#Exercise 2.2 

''' Hint: you might want to build a dictionary that maps from a collection of letters to a list of words that can be spelled with those letters. The question is, how can you represent the collection of letters in a way that can be used as a key? '''

anagram_list = ['deltas', 'jesus', 'lasted', 'is', 'slated', 'king']

def anagram(l):
    d = {}  
    for word in l: 
        key = ''.join(sorted(word))
        # print(key)
        if key in d:  
            d[key].append(word)
        else:
            d[key] = [word]  
    return d

if __name__ == '__main__':
    d = anagram(anagram_list)

    for words in d.values():
        if len(words) > 1:
            print('Anagrams: {}'.format(', '.join(words)))

