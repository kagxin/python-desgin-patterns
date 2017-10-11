"""
The decorator is not python decorator.
"""

import functools

class TextTag(object):
    """Represents a base text tag"""
    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


class BoldWrapper(TextTag):
    """Wraps a tag in <b>"""
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<b>{}</b>".format(self._wrapped.render())


class ItalicWrapper(TextTag):
    """Wraps a tag in <i>"""
    def __init__(self, wrapped):
        self._wrapped = wrapped

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

    print('-----------------------------')

