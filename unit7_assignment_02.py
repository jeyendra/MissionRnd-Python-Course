__author__ = 'Kalyan'

problem = """
Pig latin is an amusing game. The goal is to conceal the meaning of a sentence by a simple encryption.

Rules for converting a word to pig latin are as follows:

1. If word starts with a consonant, move all continuous consonants at the beginning to the end
   and add  "ay" at the end. e.g  happy becomes appyhay, trash becomes ashtray, dog becomes ogday etc.

2. If word starts with a vowel, you just add an ay. e.g. egg become eggay, eight becomes eightay etc.

You job is to write a program that takes a sentence from command line and convert that to pig latin and
print it back to console in a loop (till you hit Ctrl+C).

e.g "There is, however, no need for fear." should get converted to  "Erethay isay, oweverhay, onay eednay orfay earfay."
Note that punctuation and capitalization has to be preserved

You must write helper sub routines to make your code easy to read and write.

Constraints: only punctuation allowed is , and . and they will come immediately after a word and will be followed
by a space if there is a next word. Acronyms are not allowed in sentences. Some words may be capitalized
(first letter is capital like "There" in the above example) and you have to preserve its capitalization in the
final word too (Erethay)
"""
def case(s):
    k={'a','e','i','o','u','A','E','I','O','U'}
    r=""
    for i in range(len(s)):
        if (s[i] in k):
            r=s[i:]+s[:i]
            break
    res=[]
    for j in range(len(s)):
        if s[j].isupper():
            res.append(r[j].upper())
        if s[j].islower():
            res.append(r[j].lower())
    return  "".join(res)+"ay"
def piglatin(s):
    i=0
    res=[]
    while i<len(s):
        j=i
        try:
            if s[i].isalpha():
                while s[i].isalpha():
                    i+=1
                st=case(s[j:i])
                for it in st:
                    res.append(it)
            else:
                res.append(s[i])
                i+=1
        except IndexError:
            st=case(s[j:i])
            for it in st:
                res.append(it)
    ans="".join(res)
    print(ans)
import sys
def main():
    try:
        while True:
            i = input()
            print(i)
    except KeyboardInterrupt as k:
        return

if __name__ == "__main__":
    sys.exit(main())