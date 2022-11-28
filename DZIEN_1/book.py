class Book:
    #opis stanu  konstrukotr klasy
    def __init__(self,id,tytul,autor,cena=30):
        self.idksiazki = id
        self.tytul = tytul
        self.autor = autor
        self.cena =cena
        self.oprawa = "miękka"
        self.create_book()

    #opis zachowań -> metody
    def create_book(self):
        print("utworzono nową książkę....")

    def print_book(self):
        print(f"książka {self.tytul}, autor: {self.autor}, cena: {self.cena},"
              f" oprawa: {self.oprawa}")

    def rabat(self):
        return 0.1*self.cena

    def getcena(self):
        return self.cena

    def set_cena(self,nowacena):
        self.cena = nowacena


b1 = Book(34,"Wiedźmin","Andrzej Sapkowski",38)
b1.print_book()
print(f'rabat: {b1.rabat():.2f} zł')

print(f"tytuł książki: {b1.tytul}")
b1.cena = 41
b1.print_book()

b1.set_cena(43)
print(f"nowa cena: {b1.getcena()} zł")

b2 = Book(44,"Hobbit","J.R.R. Tolkien",39)
b2.oprawa = "twarda"
b2.print_book()

print(f'rabat: {b2.rabat():.2f} zł')

print(f'cena po rabacie: {b2.cena - b2.rabat()} zł')
