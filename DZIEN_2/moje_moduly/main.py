#import dane
#import dane as dn
from dane import nr_filia,book,WSPOLCZYNNIK_RABATOWY
from rep_funkcje.bfunkcje import czytaj_dict,czytaj_liste
from rep_klasy.czytajdane import CDane

print(nr_filia)
print(book)
print(f"podstawowy rabat: {book['cena']*WSPOLCZYNNIK_RABATOWY} zł")

print("__________________ czytanie za pomocą funkcji ________________")
czytaj_liste(nr_filia)
czytaj_dict(book)
print("__________________ czytanie za pomocą klasy i jej metod ________________")
cd = CDane(nr_filia,book)
cd.czytaj_l()
cd.czytaj_s()
