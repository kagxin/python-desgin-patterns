"""
作者：jatrix
链接：http://www.jianshu.com/p/371b2e6af53e
來源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

*References:
    http://www.jianshu.com/p/371b2e6af53e
"""

# meteclass

class Singleton(type):
    def __init__(cls, name, bases, attrs):
        super(Singleton, cls).__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance


class MyClass(metaclass=Singleton):
    pass


one = MyClass()
two = MyClass()
print(id(one))
print(id(two))

one.name = 1
print(two.name)


# __new__

class Singleton(object):
    __instance = None
    __first_init = None

    def __new__(cls, age, name):
        if not cls.__instance:
            Singleton.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, age, name):
        if not self.__first_init:
            self.age = age
            self.name = name
            Singleton.__first_init = True

a = Singleton(21, "jatrix")
b = Singleton(2, "jatrix")

print(id(a))
print(id(b))


print(a.age)
print(b.age)

a.age = 33
print(b.age)


# class decortor
def singleton(cls, *args, **kwargs):
    instance = {}

    def __singleton():
        if cls not in instance:
            instance[cls] = cls
        return instance[cls]

    return __singleton


@singleton
class MyClass:
    kind = "type"

    def __init__(self, name):
        self.name = name


@singleton
class MyAnotherClass:
    name = "another"

    def __init__(self, age):
        self.age = age


one = MyClass()
two = MyClass()
print(id(one))
print(id(two))


another_one = MyAnotherClass()
another_two = MyAnotherClass()
print(id(another_one))
print(id(another_two))

