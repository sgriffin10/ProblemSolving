with open('Classwork/Session 11/she_loves_you.txt') as f:
    lyrics = f.read().split()
    print(lyrics)

# def (s):
#     d = dict()
#     for word in s:
#         count = d.get(word, 0)
#         d[word] = count + 1
#     return d


beatles = histogram(lyrics)
print(breatles)