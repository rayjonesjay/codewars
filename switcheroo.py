"""
link to kata : https://www.codewars.com/kata/55d6a0e4ededb894be000005/train/python
"""


def encode(st):
    #now i have to make a dictionary
    st = st.lower()
    res = ""
    d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    for char in st:
        if char in d.keys():
            res += str(d[char])
        else:
            res += char
    return res

