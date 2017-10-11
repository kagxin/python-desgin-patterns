"""
Bridge的意思是桥梁，作用就是将两边连接起来。桥接模式的作用也是如此，桥接模式分别类的功能层次和类的实现层次连接起来。
# References
https://sourcemaking.com/design_patterns/bridge
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-


import abc

#abstract implementor
class AbstractAction(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def action(self, x):
        """"""


# ConcreteImplementor
class Action1(AbstractAction):

    def action(self, x):
        print('double x*2={}'.format(x*2))


# ConcreteImplementor
class Action2(AbstractAction):

    def action(self, x):
        print('triple x*3={}'.format(x*3))


# Abstraction
class Function(object):

    def __init__(self, x, action):
        self._x = x
        self.action = action

    def do(self):
        self.action.action(self._x)

    def mul(self, n):
        self._x *= n


def main():
    shapes = (
        Function(1, Action1()),
        Function(5, Action2())
    )

    for shape in shapes:
        shape.mul(2.5)
        shape.do()


if __name__ == '__main__':
    main()

### OUTPUT ###
# API1.circle at 1:2 radius 7.5
# API2.circle at 5:7 radius 27.5
