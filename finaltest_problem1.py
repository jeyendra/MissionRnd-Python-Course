__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
This is a simple text transformation problem. 

Some definitions:

Mirror:
We define mirror of a letter as the corresponding letter from the end in the alphabet. For e.g. 'z' is mirror of 'a', 
'y' is mirror of 'b'.

Similarly we define mirror of a digit. 9 is mirror of 0, 8 is mirror of 1 etc. So mirror of "25" is "74"
Mirrored word is formed by mirroring all its letters and digits. For e.g. mirror of "bac1" is "yzx8".

Ordinal score:
Ordinal score of a word is sum of ordinals of its characters. (The ord builtin is useful here).

Problem: 

Rearrange the sentence by:

1. mirror each of the words (as defined above)
2. sort the mirrored words by their ordinal scores in ascending order (defined below). In case of a tie, the word which 
comes LATER in the original sentence takes precedence. 


Notes:
1. Maintain case.
2. Any punctuation or special chars in the words/sentence must be removed.
3. You can assume that words are separated by spaces. The final sentence should be 
   separated by spaces as well.
4. You are free to create additional helper routines.
5. raise TypeError if sentence is not a string.

'''
def fun1(s):
    r=0
    for i in s:
       r=r+ord(i)
    return r
def mirror(s):
    if s.islower():
        return chr(ord("z")-ord(s)+ord("a"))
    if s.isupper():
        return chr(ord("Z")-ord(s)+ord("A"))
    if s.isdigit():
        return (str)(9-int(s))
def transform(sentence):
    if  type(sentence).__name__!="str":
        raise TypeError
    i=0
    l=[]
    res=[]
    l1=[]
    l=sentence.split()
    for i in l:
        l11=[]
        for j in i:
            if j.isalnum():
                l11.append(j)
        l1.append("".join(l11))
    l=l1
    for i in l:
        if i.isalnum():
            r1=[]
            for j in i:
                if j.isalnum():
                    r1.append(mirror(j))
            res.append("".join(r1))
    res=list(reversed(res))
    res.sort(key=fun1)
    l = []
    i = 0
    k = 0
    while i < len(sentence):
        if sentence[i] == " ":
            l.append(sentence[i])
            i += 1
        else:
            if sentence[i].isalnum():
                l.append(res[k])
                k += 1
                while i < len(sentence):
                    if sentence[i]!=" ":
                        i += 1
                    else:
                        break
            else:
                i+=1
    return "".join(l)
#assert "Z a87"==
def test_transform():
    assert "Z a87" ==transform("A z12.")
    assert "yzx8" == transform("bac1")
    assert "4 7 " == transform("2 5 ")
