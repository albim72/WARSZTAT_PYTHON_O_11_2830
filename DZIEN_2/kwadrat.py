class Kwadrat:
    def __init__(self,bok):
        self.bok = bok

    def pole(self):
        return self.bok**2

class Prostokat:

    def __new__(cls,width:float,height:float):
        if width==height:
            return Kwadrat(bok=width)
        return object.__new__(Prostokat)

    def __init__(self,width:float,height:float):
        self.width = width
        self.height = height

    def pole(self):
        return self.width*self.height

p1 = Prostokat(9,3)
p2 = Prostokat(4,2)
p3 = Prostokat(7,7)

print(type(p1))
print(type(p2))
print(type(p3))

print(f"pole 1 -> {p1.pole()}")
print(f"pole 2 -> {p2.pole()}")
print(f"pole 3 -> {p3.pole()}")

