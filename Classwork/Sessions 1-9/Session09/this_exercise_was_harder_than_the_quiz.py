total = 0
words = ['bananas', 'rice', 'paprika', 'potato chips']

def cost(word):
    price = 0
    for i in word:
        price += float(ord(i))-96
    return price

# print(cost('bananas'))

def total_price(words):
    total = 0
    longest = 0
    for word in words:
        if len(word)>longest:
            longest = len(word)
    longest += 10
    for word in words:
        print(word, '$',int((cost(word))))
        total += cost(word)
    print("-"*(longest*2))
    print("Total ", '$',int(total))

total_price(words)