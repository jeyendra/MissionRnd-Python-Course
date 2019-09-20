__author__ = 'Kalyan'

max_marks = 30

problem_notes = '''
This problem deals with a custom encryption/decryption scheme that works as follows. 

Given a string like "how are you?" and m * n grid. The characters of the string are filled 
into the grid row wise top to bottom. So for 3 * 5 you get

h o w _ a
r e _ y o
u ? * * *

In the above example _ is shown visually where there is a space character. Unfilled cells are filled with *'s

The encrypted string is found by starting at a specified corner and going clockwise in 
a decreasing spiral till all the cells are covered. So if corner is top right you get "ao***?urhow y e"


Notes:
1. raise TypeError if text is not a str or key is not EncryptKey
2. raise ValueError if the grid cannot accomodate the text  or if rows/cols are <= 0 
3. returns the encrypted string as specified above.
4. see the definitions for Corner and EncryptKey in mock1common.py
'''

from mock1common import EncryptKey, Corner


def rotateMatrix(mat):
    ''' Clockwise rotation of a matrix '''
    return [list(reversed(row)) for row in zip(*mat)]


def transpose_and_yield_top(arr):
    ''' Yields the first row of a matrix and transposes the rest of the matrix '''
    while arr:
        yield arr[0]
        arr = list(zip(*arr[1:]))
        arr.reverse()


import itertools


def encrypt(text, key):
    rows = key.rows
    cols = key.cols
    if type(text).__name__ != 'str' or type(key).__name__ != 'EncryptKey':
        raise TypeError
    if rows <= 0 or cols <= 0 or rows * cols < len(text):
        raise ValueError

    grid = []
    add_len = (rows * cols) - len(text)
    text += '*' * add_len  # make text length equal to rows*cols product

    for i in range(rows):
        grid.append(list(text[cols * i:cols * (i + 1)]))  # convert text into rowsxcols matrix

    # Rotate the matrix to make it Corner.TOP_LEFT problem
    if key.corner == Corner.TOP_RIGHT:
        grid = rotateMatrix(grid)
        grid = rotateMatrix(grid)
        grid = rotateMatrix(grid)
    if key.corner == Corner.BOTTOM_RIGHT:
        grid = rotateMatrix(grid)
        grid = rotateMatrix(grid)
    if key.corner == Corner.BOTTOM_LEFT:
        grid = rotateMatrix(grid)

    # chain makes an iterator to return elements from the first iterable until it is exhausted,
    # then proceeds to the next iterable, until all of the iterables are exhausted.
    result = list(itertools.chain(*transpose_and_yield_top(grid)))
    return ''.join(result)


# a basic test is given, write your own tests based on constraints.
def test_encrypt():
    assert "ao***?urhow y e" == encrypt("how are you?", EncryptKey(3, 5, Corner.TOP_RIGHT))

test_encrypt()