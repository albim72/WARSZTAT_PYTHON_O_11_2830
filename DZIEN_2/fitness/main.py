from rep_trener.osoba import Osoba
from rep_trener.sport import Sport
from rep_trener.klub import  Klub
from trener import Trener



print("___________________ Osoba ______________________")
os1 = Osoba("Feliks","Kot",31,74,176)
os1.print_osoba()

print(f'czy osoba jest trenerem? ({os1.czytrener()})')

print("___________________ Sport ______________________")
sp1 = Sport("Biegi Ultra",7,"50km 7h 23min 34s")
print(sp1.infosport())

print("___________________ Klub ______________________")
kb1 = Klub(12,"Herkules","ul. Bursztynowa 45, Krosno")
print(kb1.infoklub())

print("___________________ Trener ______________________")
tr1 = Trener("Jan","Kot",45,78,180,3453454,150,"Trójbój",10,450)
tr1.print_osoba()
print(tr1.infosport())
print(tr1.print_trener())
print("___________________ Trener ______________________")
tr1 = Trener("Olga","Knot",28,61,176,6546,130,"Biegi Ultra",8,"102km 18h 34min 6s",4,"Lotos","ul Trojańska 3 Ostrów Wlk")
