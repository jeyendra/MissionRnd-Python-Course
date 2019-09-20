__author__ = 'Kalyan'

max_marks = 25

problem_notes ='''
Write a routine to sort the given list of numbers according to the number
of prime factors it has.

Constraints:
1. 1 and 0 are considered to have 0 factors
2. For negative numbers, the factor count of the corresponding
   positive numbers is considered for sorting
3. Numbers with more factors come before numbers with fewer factors
4. In case of a tie, bigger numbers (numerically) comes first
5. Return a new sorted list of numbers (not-inplace)
6. Refer to the testcase for an example.

Notes:
1. Use the python built in sorting functionality to get this done.
2. Write additional helper routines as required.
3. Assume that input is valid list of numbers.
'''

# assume numbers is a valid list of numbers
def nooffacts(n):
    c=0
    for i in range(1,n):
        if n%i==0:
            c+=1
    return c
def sort_by_factor_count(numbers):
    numbers.sort(reverse=True)
    numbers.sort(key=nooffacts,reverse=True)
    return numbers
# one basic test given, write more exhaustive tests
def test_sort_by_factor_count():
    # 10 has 2 factors [2,5] , 6 has 2 [2,3], 8 has 1 [2] and 2 has 1 [2], hence the result
    assert [210, 119166912514748563375849, 7, -353243309509] == sort_by_factor_count(([119166912514748563375849, 210, -353243309509, 7],))
