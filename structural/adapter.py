"""
"""
class XiaoMing(object):

    def __init__(self):
        self.name = 'xiaoming'
        self.age = 12

    def speak(self):
        return '{} is {} years old.'.format(self.name, self.age)

class XiaoGang(object):

    def __init__(self):
        self.name = 'xiaogang'
        self.age = 14

    def say(self):
        return '{} is {} years old.'.format(self.name, self.age)

class Adapt(object):

    def __init__(self, obj, **adapt_methods):
        self.obj = obj
        self.__dict__.update(adapt_methods)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)

    def o_dict(self):
        return self.obj.__dict__

if __name__ == '__main__':
    
    xiaogang = XiaoGang()
    xiaoming = XiaoMing()
    xiaoming = Adapt(xiaoming, say=xiaoming.speak)
    for p in [xiaogang, xiaoming]:
        print(p.say())