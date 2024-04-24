"""
link to kata : https://www.codewars.com/kata/5648b12ce68d9daa6b000099/train/python
"""

def number(bus_stops):
    on = 0
    off = 0
    for i in bus_stops:
        on = on + i[0]
        off = off + i[1]
    return on - off
