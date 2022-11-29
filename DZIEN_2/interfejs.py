from abc import ABCMeta, abstractmethod

class IPojazd(metaclass=ABCMeta):
    @abstractmethod
    def spalanie100(self,odl,litry):raise NotImplementedError

    @abstractmethod
    def kosztprzejazdu(self,odl,litry,cena_l):raise NotImplementedError


class Pojazd(IPojazd):
    def spalanie100(self, odl, litry):
        return litry*100/odl

    def kosztprzejazdu(self, odl, litry, cena_l):
        return self.spalanie100(odl,litry)*(odl/100)*cena_l


p1 = Pojazd()
odl = 670
litry = 62
cena_l = 7.89

print(f'spalanie [l/100km]: {p1.spalanie100(odl,litry):.2f}')
print(f'koszt przejzdu na trasie {odl} km wynosi {p1.kosztprzejazdu(odl,litry, cena_l):.2f} zł')
