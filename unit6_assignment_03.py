__author__ = 'Kalyan'

notes = '''
 This problem will require you to put together many things you have learnt
 in earlier units to solve a problem.

 In particular you will use functions, nested functions, file i/o, functions, lists, dicts, iterators, generators,
 comprehensions,  sorting etc.

 Read the constraints carefully and account for all of them. This is slightly
 bigger than problems you have seen so far, so decompose it to smaller problems
 and solve and test them independently and finally put them together.

 Write subroutines which solve specific subproblems and test them independently instead of writing one big
 mammoth function.

 Do not modify the input file, the same constraints for processing input hold as for unit6_assignment_02
'''

problem = '''
 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.

 With in an anagram group, order them in case insensitive ascending sorting order.

 If 2 anagram groups have same count, then set with smaller starting word comes first.

 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.

 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.

 source - file containing words, one word per line, some words may be capitalized, some may not be.
 - read words from the source file.
 - group them into anagrams. how?
 
 - sort each group in a case insensitive manner
 - sort these groups by length (desc) and in case of tie, the first word of each group
 - write out these groups into destination
'''

import unit6utils
import string
def fun2(l):
    return l[0].lower()
def fun1(s):
    return s.lower()
def orde(l):
    l.sort(key=fun1)
    return l
def anag(s):
    s=s.lower()
    return "".join(sorted(s))
def fun(s):
    s= s.lower()
    return "".join(sorted(s))
def anagram_sort(source, destination):
    s=open(source)
    d=open(destination,"w")
    l=s.readlines()
    r = []
    for i in range(0, len(l)):
        l[i] = l[i].strip()
        if (l[i] != ""):
            if (l[i][0] != "#"):
                r.append(l[i])
    r.sort(key=fun)
    r.sort(key=len, reverse=True)
    res = []
    i = 0
    while i < (len(r) - 1):
        l = []
        temp1 = anag(r[i])
        temp2 = anag(r[i + 1])
        while (temp1 == temp2) and (i <(len(r) - 1)):
            l.append(r[i])
            temp1 = anag(r[i])
            temp2 = anag(r[i + 1])
            i += 1
        if len(l) == 0:
            l.append(r[i])
            i += 1
        res.append(l)
    temp1=anag(r[len(r)-1])
    temp2=anag(res[len(res)-1][0])
    if temp1==temp2:
        res[len(res)-1].append(r[len(r)-1])
    else:
        res.append(r[len(r)-1])
    for i in res:
        i=orde(i)
    res.sort(key=fun2)
    res.sort(key=len,reverse=True)
    for i in res:
        for j in i:
            d.write(j)
            d.write("\n")

def test_anagram_sort():
    source = unit6utils.get_input_file("unit6_testinput_03.txt")
    expected = unit6utils.get_input_file("unit6_expectedoutput_03.txt")
    destination = unit6utils.get_temp_file("unit6_output_03.txt")
    anagram_sort(source, destination)
    result = [word.strip() for word in open(destination)]
    expected = [word.strip() for word in open(expected)]
    assert expected == result
