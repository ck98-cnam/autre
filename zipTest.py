# from functools import reduce
#
# tpl = ((1,2), (3,4))
#
# lst = [-1,2,-3,4,-5,6,-7,8,9]
#
#
# step1 = list(filter(lambda x: x < 0, lst))
# step1 = [1]
# step2 = reduce(lambda x, y: x + y if x < 0 else 0, step1)
# print(step2)

# g = lambda x, y, z, charbel: x + y + z + charbel
# print(g(1,2,3,4))
#
# x = 5
#
# def func(x, y, z, charbel):
#     return x + y + z + charbel
#
# g = lambda x, y, z, a: func(x,y,z,a)
#
# def g(a,b,c,d):
#     return func(a,b,c,d)
#
# print(g(1,2,3,4))
#
# print(type(g))
# print(type(func))
#
# lst = [(1,2), (3,4), (5,6)]
#
# print(list(map(lambda x: x[0], lst)))
#
# print(list(map(lambda x: x[0] if x[0] > 3 else None, lst)))

# print(reduce(lambda x,y: x + y, list(filter(lambda x: x < 0, lst))))

# lst = [1,2,3,4,5,6,7,8,9,-10,-5,-4]

# print(sum(x for x in list if x > 0))

# print(*enumerate(lst))

# for i, x in enumerate(list):
#     if x < 0:
#         print(i)

# for x in list:
#     if x < 0:
#         print(list[x])

# print(list[-3])

# print(list(filter(lambda x: x > 0, list(map(lambda x: x[0] if x[1] < 0 else 0, enumerate(lst))))))

# print(list(map(lambda x: x[0], list(filter(lambda x: x[1] < 0, enumerate(lst))))))
#
# lst = [2,2,3,3,43,24312]
# print(list(filter(lambda x: x < 0, lst)))
#
# print(filter(lambda x: x < 0, lst))
#
# class Etudiant:
#     def __init__(self, nom, prenom):
#         pass

# Etudiant et1 = new Etudiant()
# et1 = Etudiant("kahwaji", "charbel")
# print(type(et1))

# lst = [1, -2, -3]
#
# print(list(map(lambda x: x[0], filter(lambda x: x[1] < 0, enumerate(lst)))))
#
# lst2 = []
# for i in lst:
#     if i < 0:
#         lst2.append(i)
# print(lst2)
# lst  = [1,2,3,4,5,6,7]
# lst2 = ["a","b","c","d","e","f","g"]
# 
# l = zip(lst, lst2)
# 
# print(list(l))


# def charbel():
#     pass

# def charbel(a,b, c):
#     if a > 0:
#         return a + b + c
#     elif b > 0:
#         return "v"
#     else:
#         return ["v", "m"]

# def charbel(a,b):
#     return a + b

# charbel = lambda a,b,c: a+b+c
# charbel = lambda a,b: a+b

# print(charbel(10, 5, 5))
# print(charbel(-10, 5, 5))
# print(charbel(-10, -5, 5))

# def charbel(a,b, c):
#     return a + b + c
#
# print(charbel("charbel", "None", 5))

# def charbel(int a, int b):
#     pass
#
# def charbel(int b, String a):
#     pass

# class Etudiant:
#     x = 5

# etu = Etudiant()
#
# print(etu.x)
# etu.y = 10
# print(etu.y)
# # help(etu)
# print(etu.__dir__())
# print(Etudiant().__dir__())
# print(dir(Etudiant))

# def chris(x):
#     return x + 10
#
# def getChris(x):
#     return chris
#
# etu.charb = lambda x: x + 5
# etu.ch = chris(3)
#
# print(etu.charb(5))
# print(etu.ch)
# etu.foo = getChris(5)
# print(etu.foo)
#
# print(etu.foo(4))
#
# etu.bar = lambda x: getChris(x)
# print(etu.bar(3))


# class foo:
#     def __init__(self):
#         print(self)
#     def init():
#         return "nfo5"
#     def isOK(self):
#         return "ok"
#     def __str__(self):
#         return "foo instance"

# f1 = foo()
# print(foo.init())
# f1.init()
# foo.init(f1)
# print(f1)
# print(foo.__init__(f1))
# print(f1)

# print(foo.init("fshafas"))
# print(f1.init())

# print(f1.isOK())
# print(foo.init())
# print(f1.init())
# foo.init(f1)

# for i in range(-1, -5):
#     print(i)

# list1 = [1,2,3,4]
# list2 = ['a','b','c']
# list3 = ['x','y','z',1,'w']
#
# print(list(zip(list1,list2, list3)))

dict_one = {'name': 'John', 'last_name': 'Doe', 'job': 'Python Consultant'}
dict_two = {'name': 'Jane', 'last_name': 'Doe', 'job': 'Community Manager'}
# print(dict_one['name'])
# print(dict_one)
print(list(zip(dict_one.items(), dict_two.items())))
# for i in list(zip(dict_one, dict_two)):
#     print(i)
# for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)

for i in zip(dict_one.items(), dict_two.items()):
    # print(i)
    # print(*i)
    # print((**i))
    pass

# [(('name', 'John'), ('name', 'Jane')), (('last_name', 'Doe'), ('last_name', 'Doe')),(('job', 'Python Consultant'), ('job', 'Community Manager'))]

# def concatenate(**args):
#     result = ""
#     print(args.items())
#     for arg in args.values():
#         result += arg
#     return result
#
# concatenate(a="real",b="python",c="is",d="great")

# def sum(a,b):
#     return a + b
#
# sumLambda = lambda a,b: a+b
#
# print(sum(1,2))
# print(sumLambda(1,2))
# print(type(sum))
# print(type(sumLambda))
#
# sumLambda = sum
#
# print(sumLambda(1,2))

# a = 5
# b = 10
#
# # a,b = b,b+a
# a = b
# b = a + b
# print(a,b)


lst = [0,1,2,3]
print(all(i < 0 for i in lst))

from functools import partial

def multiply(x,y):
        return x * y

# create a new function that multiplies by 2
dbl = partial(multiply,2)
print(dbl(4))
# sera 8