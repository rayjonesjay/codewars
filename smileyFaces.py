"""
link to kata : https://www.codewars.com/kata/583203e6eb35d7980400002a/train/python
"""
def count_smileys(arr):
    valid_faces = [':D',':~)',';~D',':)',':-)',';D',';-D',':-D']
    count = 0
    if len(arr) == 0:
        return 0
    strfaces = ''.join(arr)
    for face in valid_faces:
        count+=strfaces.count(face)
    return count


