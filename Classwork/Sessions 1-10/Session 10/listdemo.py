def capitalize_all(t):
    result = []
    for word in t:
        result.append(word.capitalize())
    
    return result

# row_3 = ['teenboi', 'spencer', 'xintong']
# print(capitalize_all(row_3))



def only_upper(t):
    res = []
    for s in t:
        if s[0].islower(): #isupper; islower; s[i].isupper
            res.append(s)
    return res

row_3 = ['Teenboi', 'SPENCER', 'xintong']
print(only_upper(row_3))



t = [1, 2, 3]
# print(sum(t))