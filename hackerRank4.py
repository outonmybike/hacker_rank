import math

def repeatedString(s, n):
    str = list(s)
    str_l = len(str)
    a = 0
    for x in range(len(str)):
        if str[x] == 'a':
            a += 1
    repeats = math.floor(n/len(str))
    # print(repeats)
    # print(a)
    a_count = repeats * a
    # print(a_count)
    left_over = n % str_l
    # print(left_over)
    partial_str = str[0:left_over]
    # print(partial_str)
    for x in range(len(partial_str)):
        if partial_str[x] == 'a':
            a_count += 1
    # print(a_count)
    return a_count
    


repeatedString('a',1000000000000)