import math

def mysqrt(a):
    x = 3
    while True:
        y = (x + a/x) / 2
        if y == x:
            return y
            break
        x = y

# print(mysqrt(4))

def test_square_root(list_of_a):
    
    s1 = " "
    s2 = "       "
    s3 = "     "

    d1 = "-"
    d2 = "---------"
    d3 = "------------"
    d4 = "----"

    c1 = "a"
    c2 = "mysqrt(a)"
    c3 = "math.sqrt(a)"
    c4 = "diff"
    print(c1, s1, c2, s2, c3, s3, c4)
    print(d1, s1, d2, s2, d3, s3, d4)

    for a in list_of_a:
        l1 = a
        l2 = mysqrt(a)
        l3 = math.sqrt(a)
        l4 = l3 - l2
        print(l1, s1, '{:<10f}'.format(l2), s2, '{:<10f}'.format(l3), s3, s1, l4)

test_square_root(range(1,10))