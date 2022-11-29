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


class MojaKlasa(Abstract):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z=z

    def fxy(self):
        return self.x+self.y+self.z

    def gxy(self):
        return super().gxy()+(self.z-7)


m = MojaKlasa(9,3,2)

print(f'funkcja fxy -> {m.fxy()}')
print(f'funkcja gxy -> {m.gxy()}')

print(f'pierwotne x: {m.xp}')
print(f'pierwotne y: {m.yp}')





