"""
"""
import abc

class AbstractSubject(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def request(self):
        """ """

class Proxy(AbstractSubject):

    def __init__(self, subject):
        self.allow = False
        self._subject = subject

    def request(self):
        if self.allow:
            self._subject.request()
        else:
            print("do not allow.")

class Subject(AbstractSubject):

    def __init__(self, subject_name):
        self.subject_name = subject_name

    def request(self):
        print('get request, do subject request.')

def main():
    real_subject = Subject('just a subject.')
    proxy = Proxy(real_subject)
    proxy.request()
    proxy.allow = True
    proxy.request()

if __name__ == '__main__':
    main()