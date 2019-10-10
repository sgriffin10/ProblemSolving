def nested_sum(t):
    """Computes the total of all numbers in a list of lists.
    t: list of list of numbers
    returns: number """
    total = 0
    for i in t:        
        if isinstance(i, list):
            total += nested_sum(i)
        else:
            total += i
    return total

# print(nested_sum([[1, 2], [3], [4, 5, 6]]))



def cumsum(t):
    """Computes the cumulative sum of the numbers in t.
    t: list of numbers
    returns: list of numbers
    Expected output:
    >>> t = [1, 2, 3]
    >>> cumsum(t)
    [1, 3, 6]
    """
    result = 0
    cumsum_numbers = []
    for i in t:
        result += i
        cumsum_numbers.append(result)
    return cumsum_numbers

# print(cumsum([1, 2, 3]))

def middle(t):
    """Returns all but the first and last elements of t.
    t: list
    returns: new list
    Expected output:
    >>> t = [1, 2, 3, 4]
    >>> middle(t)
    [2, 3]
    """
    t.pop(0)
    t.pop()
    return t

# print(middle([1, 2, 3, 4]))

def chop(t):
    """Removes the first and last elements of t.
    t: list
    returns: None
    Expected output:
    >>> t = [1, 2, 3, 4]
    >>> chop(t)
    >>> t
    [2, 3]
    """
    del t[0]
    del t[len(t)-1]
    return t

# print(chop([1, 2, 3, 4]))



def is_sorted(t):
    """Checks whether a list is sorted.
    t: list
    returns: boolean
    Expected output:
    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted(['b', 'a'])
    False
    """
    list_t = t[:]
    list_t.sort()
    if list_t == t :
        return True 
    return False

# print(is_sorted([1, 2, 2]))
# print(is_sorted(['b', 'a']))


def is_anagram(word1, word2):
    """Checks whether two words are anagrams
    Two words are anagrams if you can rearrange the letters from one to 
    spell the other.
    word1: string or list
    word2: string or list
    returns: boolean
    Expected output:
    >>> is_anagram('stop', 'pots')
    True
    >>> is_anagram('different', 'letters')
    False
    >>> is_anagram([1, 2, 2], [2, 1, 2])
    Ture
    """
    for letter in word1:
        if letter not in word2:
            return False
    return True

# print(is_anagram('stop', 'pots'))
# print(is_anagram('different', 'letters'))
# print(is_anagram([1, 2, 2], [2, 1, 2]))


def has_duplicates(s):
    """Returns True if any element appears more than once in a sequence.
    s: string or list
    returns: bool
    output:
    >>> print(has_duplicates('cba'))
    False
    >>> print(has_duplicates('abba'))
    True
    """
    if len(s) > len(set(s)):
        return True
    return False

# print(has_duplicates('cba'))
# print(has_duplicates('abba'))

def has_adjacent_duplicates(s):
    """Returns True if there are two same adjacent elements.
    s: string or list
    returns: bool
    output:
    >>> print(has_adjacent_duplicates('cba'))
    False
    >>> print(has_adjacent_duplicates('abca'))
    Flase
    >>> print(has_adjacent_duplicates('abbc'))
    True
    """
    adjacent = ''
    for letter in s:
        if adjacent == letter:
            return True
        adjacent = letter
    return False

# print(has_adjacent_duplicates('cba'))
# print(has_adjacent_duplicates('abca'))
# print(has_adjacent_duplicates('abbc'))

def main():
    t = [[1, 2], [3], [4, 5, 6]]
    print(nested_sum(t))

    t = [1, 2, 3]
    print(cumsum(t))

    t = [1, 2, 3, 4]
    print(middle(t))
    chop(t)
    print(t)

    print(is_sorted([1, 2, 2]))
    print(is_sorted(['b', 'a']))

    print(is_anagram('stop', 'pots'))
    print(is_anagram('different', 'letters'))
    print(is_anagram([1, 2, 2], [2, 1, 2]))

    print(has_duplicates('cba'))
    print(has_duplicates('abba'))


if __name__ == "__main__":
    main()