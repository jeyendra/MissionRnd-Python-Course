#
# def test_palin(s):
#     s=s.lower()
#     s1=s[::-1]
#     if s1==s:
#         return 1
#     else:
#         return 0
# def make_palindrome(word):
#     if type(word).__name__!="str":
#         raise TypeError
#     i=0
#     for i in range(len(word)):
#         if test_palin(word[i:]):
#             break
#     k=word[:i]
#     k=k[::-1]
#     k=k.lower()
#     return word + k
# print(make_palindrome("abab"))


# class myclass(object):
#     var=10
#     @staticmethod
#     def fun(self):
#         self.var+=10
#         print(self.var)
#     @classmethod
#     def clsmet(cls):
#         print("haha",cls.var)
# obj1=myclass()
# obj2=obj1
# obj2.var=20
# print(obj2.var)
# print(obj1.var)
# myclass.clsmet()
# myclass.fun()

# class a:
#     x1=10
#     def __init__(self):
#         self.x=10
#         self.y=10
#     def hah(self):
#         print("haha in a")
# class b(a):
#     def __init__(self):
#         print(super().x1)
#     def hah(self):
#         print("haha in b")
# bob=b()
# bob.hah()

l=[1,2,3]
l1=[]
l1.extend(l)
l1.sort(reverse=True)
print(l1)
print(l)