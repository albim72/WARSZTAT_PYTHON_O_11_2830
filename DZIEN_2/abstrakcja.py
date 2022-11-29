from abc import ABC,abstractmethod

class Abstract(ABC):
    def __init__(self,x,y):
        self.x = 2*x
        self.y = y**2
        self.xp = x
        self.yp = y
        self.msg()


    def msg(self):
        print(f'pierwotnie zadane wartości: x = {self.xp}, y = {self.yp}')

    @abstractmethod
    def fxy(self):
        pass

    @abstractmethod
    def gxy(self):
        #ciało domyślne metody abstrakcyjnej
        return self.x+self.y





