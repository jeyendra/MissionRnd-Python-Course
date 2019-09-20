__author__ = 'Kalyan'

max_marks = 20

problem_notes = '''
 This problem deals with number conversion from a custom base 36 notation.

 In this notation, the digits 0 to 9 and letters a to z and  are to represent 0 to 35. 
 E.g. decimal 10 in this notation will be "a", 15 will be "f", 35 will be "z". "10" will represent 36.

 The notation in case insensitive so even "Z" is a valid representation for 35.

 Your job is to write a decoding routine for this notation.

 Note: 

 1. make good use of python features and avoid huge if else statement flow!
 2. read additional constraints on the function comments below.
 3. add any standard imports that you need.
'''


# Notes:
# - if s is not a string, raise TypeError
# - if the encoding is not right or empty string, raise ValueError
# - allow both - and + as prefixes which represent sign.
# - allow trailing and starting spaces (but not once the sign or number starts)
# - allow both capital and small letters.
# - return a int or long that corresponds to the number.
def crt(s):
    return s.isalnum()


def from_custom_base36(s):
    k = 0
    if type(s).__name__ != "str":
        raise TypeError
    if s[0] == '-':
        if (not (crt(s[1:]))) or (s == ""):
            raise ValueError
    else:
      if (not (crt(s))) or (s == ""):
            raise ValueError
    s = s.lower()
    if (s[0] == "-"):
        k = -1
        s = s[1:]
    s = s[::-1]
    res = 0
    for i in range(0, len(s)):
        if (s[i].isalpha()):
            t = (ord(s[i]) - ord('a')) + 10
            res = res + t * (36 ** i)
        else:
            t = (int)(s[i])
            res = res + t * (36 ** i)
    if (k == -1):
        return res * (-1)
    return res


# a basic test is given, write your own tests based on constraints.
def test_from_custom_base36():
    assert -10 == from_custom_base36("-a")
    assert 10 == from_custom_base36("a")
    assert -10 == from_custom_base36("-A")
    assert 10 == from_custom_base36("A")
    assert 100 == from_custom_base36("2s")
    assert 35 == from_custom_base36("z")
    assert  76873132946 == from_custom_base36(" zbca102 ")