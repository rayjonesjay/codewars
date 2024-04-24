"""
link to kata :  https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python
"""

def duplicate_encode(word):
    l = []
    word = word.lower() #ignore casing
    for char in word:
        if word.count(char) > 1:
            l.append(")")
        elif word.count(char) == 1:
            l.append("(")
    return ''.join(l)
    #your code here
