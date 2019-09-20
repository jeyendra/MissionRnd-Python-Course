__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
A palindrome is a word which spells the same from both ends (case-insensitive).  

If a word is not a palindrome, you can make a palindrome out of it by adding letters to either ends of the word.

Your goal is to make a palindrome of the minimum length.

For e.g.  cat is not a palindrome, you can add letters at the ends to make palidromes like catac (ending), cattac (ending), 
taccat (beginning), tacat (beginning), acattaca (both ends). However, of all this the minimum length ones are catac and tacat.
  
Notes:

1. If word is not a str, raise TypeError
2. empty string is considered to be a palindrome.
3. if multiple palindromes of same length are possible, return the one earlier in alphabetical ordering (catac in 
   the example above, keep it case insensitive)
4. Only small letters should be added. The casing of original letters should be unchanged.
5. Write your own tests and test thoroughly.
'''

# returns the min length palidrome defined by the criteria given above.

def test_palin(s):
    s=s.lower()
    s1=s[::-1]
    if s1==s:
        return 1
    else:
        return 0
def make_palindrome(word):
    if type(word).__name__!="str":
        raise TypeError
    i=0
    for i in range(len(word)):
        if test_palin(word[i:]):
            break
    k=word[:i]
    k=k[::-1]
    k=k.lower()
    return word + k
def test_make_palindrome():
    assert "cATac" == make_palindrome("cAT")
    assert "dudedud" == make_palindrome("duded")
    assert "RoTator" == make_palindrome("RoTator")
    assert "dudedud" == make_palindrome("duded")
    assert "RORaror" == make_palindrome("RORar")
    assert "ababa" == make_palindrome("abab")