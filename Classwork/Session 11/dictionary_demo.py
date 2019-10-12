def histogram(s):
    d = dict()
    for c in s:
        count = d.get(c, 0)
        d[c] = count + 1
        # if c not in d:
        #     d[c] = 1
        # else:
        #     d[c] += 1
        # print(d)
    return d

h = histogram("bookkeeper")
# print(h)

def print_hist(h):
    d = dict()
    for c in h:
        print(c, h[c])

with open('Classwork/Session 11/she_loves_you.txt') as f:
    lyrics = f.read().split()
    print(lyrics)

beatles = histogram(lyrics)
print_hist(beatles)
