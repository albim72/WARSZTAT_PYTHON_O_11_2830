class Osoba:
    def __init__(self,imie,nazwisko,wiek,waga,wzrost):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.waga = waga
        self.wzrost = wzrost
        self.kolor_oczu = "brązowe"
        self.trener = False
        
    def print_osoba(self):
        print(f'Osoba -> {self.imie} {self.nazwisko}, wiek: {self.wiek}, waga: {self.waga} kg, '
              f'wzrost: {self.wzrost} cm, kolor oczu: {self.kolor_oczu}.')
        
    def czytrener(self):
        return self.trener
