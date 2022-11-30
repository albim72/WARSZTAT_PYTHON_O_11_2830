class MojaMeta(type):
    def __new__(cls,clsname,superclasses,attribdict):
        print(f"nazwa klasy: {clsname}")
        print(f"dziedziczone klasy: {superclasses}")
        print(f"zbiór atrybutów: {attribdict}")
        return type.__new__(cls,clsname,superclasses,attribdict)

    def info(cls):
        return "metaklasa działa..."

class Zwykla:
    def oblicz(self,x,y):
        return x+y

class Pierwsza(Zwykla,metaclass=MojaMeta):
    def oblicz(self, x, y):
        return x + y - 2

class Druga(Pierwsza):
    pass

class Dodatkowa:
    pass

class Trzecia(Dodatkowa,Druga):
    pass
