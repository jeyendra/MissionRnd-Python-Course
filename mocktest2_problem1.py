__author__ = 'Kalyan'

max_marks = 20

problem_notes = '''
Given a sequence [a1, ... ,an], the diff sequence is [|a1- a2|, |a2-a3|, .... |an -a1|] (loop around at the end).
(|x| denotes absolute value of x)

A sequence of 0s is called a null sequence.  

If we apply the diff process repeatedly on a given sequence, it may or may not end in a null sequence. 
For e.g. 
 - [1, 1, 1] becomes [0, 0, 0] in 1 step. 
 - [1, 1, 0] loops and never becomes a null sequence.

Write a routine to find out the number of steps it takes for a sequence to end in a null sequence. If it does not 
end (due to some repetition), then return -1.

Notes:
1. Assume nums is a valid list of integers.
2. Refer to the testcase for an example.
3. Write your own tests and edge cases, don't rely only on the examples given.
4. Feel free to write additional helper methods as appropriate.
5. Treat this as a coding problem, don't try to find O(1) maths formulas :) 
'''

# assume numbers is a valid list of numbers
def allone(l):
    for i in range(0,len(l)):
        if l[i]!=0:
            return 0
    return 1
def alleq(l):
    for i in range(0,len(l)-1):
        if l[i]!=l[i+1]:
            return 0
    return 1
def count_steps(numbers):
    diff=[]
    c=0
    if type(numbers).__name__!="list":
        return ValueError
        raise ValueError
    if(allone(numbers)):
        return 0
    for i in range(0,len(numbers)):
        if i==len(numbers)-1:
            diff.append(numbers[len(numbers)-1]-numbers[0])
        else:
            diff.append(numbers[i]-numbers[i+1])
    if allone(diff):
        return c+1
    elif alleq(diff):
        return c+2
    else:
        return -1

# one basic test given, write more exhaustive tests
print(type(count_steps((1,2,3))).__name__)