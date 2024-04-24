"""
link to kata : https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python
"""
def high_and_low(numbers):
    # ...
    #transform the string to a list of integers
    nums = list(map(int, numbers.split()))
    
    if len(nums) == 1:
        return f"{nums[0]} {nums[0]}"
    
    #max() and min() are inbuilt 
    h = max(nums)
    l = min(nums)
    return f"{h} {l}"

