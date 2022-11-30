odp = input("Czy Ziemia jest płaska? Chcesz znać odpowiedź?(t/n)")

if odp.lower() == "t":
    required = True
else:
    required = False

def odpowiedz(self,*args):
    return "tak ziemia jest płaska!"

def brak(self,*args):
    return "brak odpowiedzi..."

#tworzenie metaklasy
class SednoOdpowiedzi(type):
    def __init__(cls,clsname,supercls,attribs):
        if required:
            cls.odpowiedz = odpowiedz
        else:
            cls.odpowiedz = brak


class Arystoteles(metaclass=SednoOdpowiedzi):
    pass

class Platon(metaclass=SednoOdpowiedzi):
    pass

class SwTomasz(metaclass=SednoOdpowiedzi):
    pass


fil1 = Arystoteles()
fil2 = Platon()
fil3 = SwTomasz()

print(fil1.odpowiedz())
print(fil2.odpowiedz())
print(fil3.odpowiedz())

