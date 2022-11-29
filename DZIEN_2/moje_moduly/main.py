#import dane
#import dane as dn
from dane import nr_filia,book,WSPOLCZYNNIK_RABATOWY

print(nr_filia)
print(book)
print(f"podstawowy rabat: {book['cena']*WSPOLCZYNNIK_RABATOWY} zł")
