__author__ = 'Kalyan'

problem = """
 We are going to revisit unit6 assignment3 for this problem.

 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.

 With in an anagram group, order them in case insensitive ascending sorting order.

 If 2 anagram groups have same count, then set with smaller starting word comes first.

 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.

 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.

 This program should be written as a command line script. It takes one argument the input file of words and outputs
 <input>-results.txt where <input>.txt is the input file of words.
"""
import sys
import os
import inspect
def get_module_dir():
    mod_file = inspect.getfile(inspect.currentframe())
    mod_dir = os.path.dirname(mod_file)
    return mod_dir

def get_temp_dir():
    module_dir = get_module_dir()
    temp_dir = os.path.join(module_dir, "tempfiles")
    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)
    return temp_dir

# open files generated as a part of the tests. Allow them to be in a different dir via DATA_DIR
def open_temp_file(file, mode):
    data_dir = os.getenv("DATA_DIR", default=get_temp_dir())
    out_file = os.path.join(data_dir, file)
    return open(out_file, mode)

#opens a file from the module directory for reading. These are input files that are part of course material
#and must be submitted along with this lesson.
#Read: https://docs.python.org/3/library/functions.html#open

def open_input_file(file, mode="rt"):
    mod_dir = get_module_dir()
    test_file = os.path.join(mod_dir, file)
    return open(test_file, mode)
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



def prob(inpfil):
    s=open_input_file(inpfil)
    k=inpfil+"-results"
    d = open(k, "w")
    l = s.readlines()
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
        while (temp1 == temp2) and (i < (len(r) - 1)):
            l.append(r[i])
            temp1 = anag(r[i])
            temp2 = anag(r[i + 1])
            i += 1
        if len(l) == 0:
            l.append(r[i])
            i += 1
        res.append(l)
    temp1 = anag(r[len(r) - 1])
    temp2 = anag(res[len(res) - 1][0])
    if temp1 == temp2:
        res[len(res) - 1].append(r[len(r) - 1])
    else:
        res.append(r[len(r) - 1])
    for i in res:
        i = orde(i)
    res.sort(key=fun2)
    res.sort(key=len, reverse=True)
    for i in res:
        for j in i:
            d.write(j)
            d.write("\n")


if __name__ == "__main__":
    inp=sys.argv[1]
    prob(inp)