"""
link to kata : https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train/python
"""

def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    if sq < 0:
        return -1
    
    result = sq ** 0.5 #find the square root of sq
    
    if result % 1 == 0:
        return (result + 1)**2
    elif result % 1 < 0:
        return -1
    return -1
