p1="""def fun(s1,s2):
    se1=set(s1)
    se2=set(s2)
    if se1==se2:
        for i in se1:
            if s1.count(i)!=s2.count(i):
                return False
    else:
        return False
    return True
print(fun("mad","dam"))"""
# import collections
# s1=input()
# s2=input()
# c1=collections.Counter(s1)
# c2=collections.Counter(s1)
# if c1==c2:
#     print("anagrams")
# else:
#     print("not anagrams")