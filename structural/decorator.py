"""
The decorator is not python decorator.
"""
import abc 

import functools

# abstract component
class Component(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def render(self):
        """ """

# abstract decorator
class Decorator(Component, metaclass=abc.ABCMeta):

    def __init__(self, wrapped):
        self._wrapped = wrapped

    @abc.abstractmethod
    def render(self):
        """ """

#ConcreteComponent
class TextTag(Component):
    """Represents a base text tag"""
    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


# ConcreteDecorator
class BoldWrapper(Decorator):
    """Wraps a tag in <b>"""

    def render(self):
        return "<b>{}</b>".format(self._wrapped.render())


# ConcreteDecorator
class ItalicWrapper(Decorator):
    """Wraps a tag in <i>"""

    def render(self):
        return "<i>{}</i>".format(self._wrapped.render())


# def bold_wrapper(func):

#     @functools.wraps
#     def wrapper(*args, **kwargs):
#         text = func(*args, **kwargs)
#         return "<b>{}</b>".format(text)

#     return wrapper

# def italic_wrapper(func):

#     @functools.wraps
#     def wrapper(*args, **kwargs):
#         text = func(*args, **kwargs)
#         return "<i>{}</i>".format(text)

#     return wrapper


if __name__ == '__main__':
    simple_hello = TextTag("hello, world!")
    special_hello = ItalicWrapper(BoldWrapper(simple_hello))
    print("before:", simple_hello.render())
    print("after:", special_hello.render())


