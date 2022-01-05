"""
https://rszalski.github.io/magicmethods/
"""

class A:
    def __new__(cls, *args, **kwags):

        if not hasattr(cls, '_exist'):
            cls._exist = super().__new__(cls)

        return cls._exist

    def __init__(self):
        print('iniciando')

class B:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        result = 1

        for i in args :
            result *= i
        
        return result


class C:
    def __init__(self):
        pass

    def __setattr__(self, name, value):
        return super().__setattr__(name, value)

class D:
    def __str__(self):
        return "hmm"


a = A()
aa = A()

print(a == aa)

b = B()
res = b(1,2,3,45,6,67,8,8,85,)
print(res)

c = C()
c.nome = "William"
print(c.nome)

d = D()
print(d)