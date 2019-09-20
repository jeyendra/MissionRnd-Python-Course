__author__ = 'Kalyan'

max_marks = 30

problem_notes ='''
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

def encrypt(text, key):
    pass
# a basic test is given, write your own tests based on constraints.
def test_encrypt():
    assert "ao***?urhow y e" == encrypt("how are you?", EncryptKey(3, 5, Corner.TOP_RIGHT))

