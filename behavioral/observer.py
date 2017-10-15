"""
observer
"""


class Observer:

    def notify(self, pub):
        raise NotImplementedError


class Publisher:

    def __init__(self):
        self.observers = []

    def add(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print('{} in observers.'.format(observer))

    def remove(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print('{} not in observers.'.format(observer))

    def notify(self):
        for observer in self.observers:
            observer.notify(self)


class JustPublisher(Publisher):

    def __init__(self, name):
        super(JustPublisher, self).__init__()
        self.name = name
        self.__data = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data
        self.notify()

    data = property(get_data, set_data)


class PrintObserver(Observer):

    def notify(self, pub):
        print('{}:{}'.format(self.__class__.__name__, pub.data))


class Print2Observer(Observer):

    def notify(self, pub):
        print('{}:{}'.format(self.__class__.__name__, pub.data))

if __name__ == '__main__':

    just = JustPublisher('just test')
    po = PrintObserver()
    po2 = Print2Observer()
    just.add(po)
    just.add(po2)

    just.data = 'hello'
    just.data = 'hello2'

    just.remove(po)

    just.data = 'hello3'

