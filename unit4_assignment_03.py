__author__ = 'Kalyan'

notes = '''
You have written similar code in earlier units. These exercise are for practicing 
writing code using comprehensions. 
'''

import string

def get_reverse_mapping():
    """
    Maps a -> z , b -> y, c -> x etc. Only smalls. Use dict comprehension
    """
    return {chr(i+97):chr(122-i) for i in range(0,26)}

def test_get_reverse_mapping():
    result = get_reverse_mapping()
    for index, letter in enumerate(string.ascii_lowercase):
        value = result[letter]
        assert 1 == len(value)
        index2 = string.ascii_lowercase.find(value)
        assert index + index2 == 25


def get_lower_to_upper_dict():
    """
    returns a dict which contains a mapping from lower case letters to upper case letters. Use dict comprehension
    """
    return {chr(i+32): chr(i) for i in range(65,91)}

def test_lower_to_upper_dict():
    #print(get_lower_to_upper_dict())
    lower_to_upper = get_lower_to_upper_dict()
    assert 26 == len(lower_to_upper)
    for x in lower_to_upper:
        y = lower_to_upper[x]
        assert 1 == len(x)
        assert x.islower()
        assert 1 == len(y)
        assert y.isupper()
        assert x.upper() == y


def get_encoding_dict():
    """
    returns a dict which maps a -> 1, b -> 2 ... z->26 and A -> 1, B ->2 ... Z->26
    """
    d1={chr(i + 65): i+1 for i in range(26)}
    d1.update({chr(i + 97): i+1 for i in range(26)})
    return d1
def test_get_encoding_dict():
    d = get_encoding_dict()
    assert len(d) == 52
    for key in d:
        assert ord(key.lower()) - ord('a') + 1 == d[key]

import calendar

# use the calendar.month_abbr (read the source code in calendar.py and understand how it works. yes, really!)
#
# right click on calendar import above and go to declaration
# and use it in your comprehension below)
def get_months():
    """
    returns a map of month index (1 to 12) to the month abbreviation ("Jan", "Feb"....).
    Use calendar.month_abbr as indicated above. Use dict comprehensions
    """
    l=list(calendar.month_abbr)[1:]
    return {i+1:l[i] for i in range(len(l))}
def test_get_months():
    month_map = get_months()
    assert type(month_map) == dict
    assert len(month_map) == 12

    months = list(calendar.month_abbr)
    for index in range(1,13):
        assert months[index] == months[index]

