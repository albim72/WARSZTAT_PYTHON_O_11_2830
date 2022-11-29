#import dane
#import dane as dn
from dane import nr_filia,book,WSPOLCZYNNIK_RABATOWY
from rep_funkcje.bfunkcje import czytaj_dict,czytaj_liste

print(nr_filia)
print(book)
print(f"podstawowy rabat: {book['cena']*WSPOLCZYNNIK_RABATOWY} zł")

print("__________________ czytanie za pomocą funkcji ________________")
czytaj_liste(nr_filia)
czytaj_dict(book)
