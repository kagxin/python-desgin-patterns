"""
#refrences
https://sourcemaking.com/design_patterns/chain_of_responsibility/python/1
"""
import abc
from enum import Enum

Week = Enum('Week', ('Sun', 'Mon', 'Tue', 'Web', 'Thu', 'Fri', 'Sat'))

class Handler(metaclass=abc.ABCMeta):

    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, request):
        res = self._handle(request)
        if res == None:
            res = self._successor.handle(request)
        return res


    @abc.abstractmethod
    def _handle(self, request):
        """ """

class ConcreteHandler1(Handler):

    def _handle(self, request):
        """ """
        if request in (Week.Mon, Week.Tue, Week.Web, Week.Thu, Week.Fri):
            print('I am work.')
            return 'I am work.'

class ConcreteHandler2(Handler):

    def _handle(self, request):
        """ """
        if request in (Week.Sat, ):
            print('I am sleep.')
            return 'I am sleep.'

class ConcreteHandler3(Handler):


    def _handle(self, request):
        """ """
        if request in (Week.Sun, ):
            print('I am play.')
            return 'I am play.'

class DefaultHandler(Handler):

    def handle(self, request):
        res = self._handle(request)
        return res
        
    def _handle(self, request):
        """ """
        return 'Get default handler.'

class Client(object):

    def __init__(self):
        self.hander = ConcreteHandler1(ConcreteHandler2(ConcreteHandler3(DefaultHandler())))

    def deal_requests(self, requests):
        ret_list = map(self.hander.handle, requests)
        print(list(ret_list))

def main():
    c = Client()
    c.deal_requests(Week)

if __name__ == '__main__':
    main()
