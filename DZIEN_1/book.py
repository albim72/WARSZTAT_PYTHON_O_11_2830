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
    
