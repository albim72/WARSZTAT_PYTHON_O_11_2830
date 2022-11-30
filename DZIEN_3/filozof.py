odp = input("Czy Ziemia jest płaska? Chcesz znać odpowiedź?(t/n)")

if odp.lower() == "t":
    required = True
else:
    required = False

def odpowiedz(self,*args):
    return "tak ziemia jest płaska!"

def odpowiedz_new(self,*args):
    return "nie! ziemia jest okrągła!"

def brak(self,*args):
    return "brak odpowiedzi..."

#tworzenie metaklasy
class SednoOdpowiedzi(type):
    def __init__(cls,clsname,supercls,attribs):
        if required:
            if clsname == "Kopernik":
                cls.odpowiedz = odpowiedz_new
            else:
                cls.odpowiedz = odpowiedz
        else:
            cls.odpowiedz = brak


class Arystoteles(metaclass=SednoOdpowiedzi):
    pass

class Platon(metaclass=SednoOdpowiedzi):
    pass

class SwTomasz(metaclass=SednoOdpowiedzi):
    pass

class Kopernik(metaclass=SednoOdpowiedzi):
    # def odpowiedz(self, *args):
    #     return "nie! ziemia jest okrągła!"
    pass


fil1 = Arystoteles()
fil2 = Platon()
fil3 = SwTomasz()
fil4 = Kopernik()

print(f"filozof: {fil1.__class__.__name__} odpowiada: {fil1.odpowiedz()}")
print(f"filozof: {fil2.__class__.__name__} odpowiada: {fil2.odpowiedz()}")
print(f"filozof: {fil3.__class__.__name__} odpowiada: {fil3.odpowiedz()}")
print(f"filozof: {fil4.__class__.__name__} odpowiada: {fil4.odpowiedz()}")

