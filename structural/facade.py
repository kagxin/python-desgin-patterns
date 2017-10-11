"""
#refrences
https://sourcemaking.com/design_patterns/facade
"""

class SubSystem1(object):

    def operation1(self):
        print('{} operation1'.format(self.__class__.__name__))

    def operation2(self):
        print('{} operation2'.format(self.__class__.__name__))


class SubSystem2(object):

    def operation1(self):
        print('{} operation1'.format(self.__class__.__name__))

    def operation2(self):
        print('{} operation2'.format(self.__class__.__name__))

class Facade:
    def __init__(self):
        self.subsytem1 = SubSystem1()
        self.subsytem2 = SubSystem2()

    def run_all(self):
        self.subsytem1.operation1()
        self.subsytem1.operation2()
        self.subsytem2.operation1()
        self.subsytem2.operation2()


if __name__ == '__main__':
    facade = Facade()
    facade.run_all()
