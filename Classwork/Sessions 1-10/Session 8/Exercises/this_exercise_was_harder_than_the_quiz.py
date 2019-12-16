total = 0
words = ['bananas', 'rice', 'paprika','potato chips'] 

def cost(word):
    price = 0
    for i in word:
        price += ord(i)-96
    return price

print(cost('bananas'))

def total_price(words):
    total = 0
    longest = max(words, key=len)
    # print(longest)
    for word in words:
        price = cost(words)
        print("{:<{number_length}} ${:>6,.2f}".format(words, price, number_length = width))
        # word, '$',int((cost(word))))
    #     total += cost(word)
    # print("-"*(longest*2))
    # print("Total ", '$',int(total))

total_price(words)