"""
1 Director
2 Product
3 Abstract Builder
4 Concrete Builder
"""

#Product
class People(object):

    def __init__(self):
        self.name = None
        self.age = None

    def __str__(self):
        return '{} is {} year old.'.format(self.name, self.age)

#Director
class Director(object):

    def __init__(self):
        self.builder = None

    def construct_product(self):
        self.builder.new_product()
        self.builder.set_name()
        self.builder.set_age()

    def get_product(self):
        return self.builder.product

# Abstrace Builder
class AbstaceBuilder(object):

    def __init__(self):
        self.product = None

    def new_product(self):
        self.product = People()

    def set_name(self):
        raise NotImplementedError

    def set_age(self, age):
        raise NotImplementedError


class XiaoMingBuilder(AbstaceBuilder):

    def set_name(self):
        self.product.name = 'xiaoming'

    def set_age(self):
        self.product.age = 12

class XiaoGangBuilder(AbstaceBuilder):

    def set_name(self):
        self.product.name = 'XiaoGang'

    def set_age(self):
        self.product.age = 13


if __name__ == '__main__':
    
    director = Director()
    director.builder = XiaoMingBuilder()
    director.construct_product()
    xiaoming = director.get_product()
    print(xiaoming.__str__())

    director.builder = XiaoGangBuilder()
    director.construct_product()
    xiaogang = director.get_product()
    print(xiaogang)




