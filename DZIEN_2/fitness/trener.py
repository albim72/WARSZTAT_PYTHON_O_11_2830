from rep_trener.osoba import Osoba
from rep_trener.sport import Sport
from rep_trener.klub import Klub

class Trener(Osoba,Sport,Klub):
    def __init__(self,imie,nazwisko,wiek,waga,wzrost,nrlicencji,stawka,dyscyplina,lata_upr,zyciowka,
                 nr_kb="",nazwa="",adres=""):
        Osoba.__init__(self,imie,nazwisko,wiek,waga,wzrost)
        Sport.__init__(self,dyscyplina,lata_upr,zyciowka)
        Klub.__init__(self,nr_kb,nazwa,adres)
        self.nrlicencji = nrlicencji
        self.stawka = stawka
        if self.trener_bez_klubu() == False:
            print("Trener bez przydziału do klubu")
        else:
            print(f"Trener przydzielony do klubu nr {self.nr_kb}")

    def print_trener(self):
        return f'Trener -> nr {self.nrlicencji} - stawka: {self.stawka} zł/h'

    def trener_bez_klubu(self):
        return self.nr_kb != ""
