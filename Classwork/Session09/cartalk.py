
def three_doubles_consecutive(word):
    index = 0
    while index < len(word)-5:
        if word[index] == word[index+1] and word[index+2] == word[index+3] and word[index+4] == word[index+5]:
            return True
        index += 1
    return False

def find_words_with_three_consecutive_double_letters():
    f = open('Classwork/session09/words.txt')
    for line in f:
        word = line.strip()
        if three_doubles_consecutive(word):
            print(word)

find_words_with_three_consecutive_double_letters()

