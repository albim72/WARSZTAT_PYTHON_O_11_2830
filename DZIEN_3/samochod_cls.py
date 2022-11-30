class Samochod:
    def __init__(self,marka,model,rocznik,cena,rata):
        self.marka = marka
        self.model = model
        self.rocznik = rocznik
        self.cena = cena
        self.rata = rata

    @staticmethod
    def salon(miasto):
        return f"salon sprzedaży -> miasto {miasto}"

    @classmethod
    def obliczenieRaty(cls,cena,miesiac):
        return cls("Opel","Insignia",2019,56000,1.3*cena/miesiac)

sm = Samochod("Jeep","Cherokee",2017,124500,2700)
sm2 = Samochod.obliczenieRaty(57800,48)

print(sm.salon("Toruń"))
print(sm.rata)

print(sm2.salon("Kraków"))
print(f"{sm2.rata:.2f}")
