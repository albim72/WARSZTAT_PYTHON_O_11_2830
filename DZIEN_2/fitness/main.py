from rep_trener.osoba import Osoba
from rep_trener.sport import Sport


print("___________________ Osoba ______________________")
os1 = Osoba("Feliks","Kot",31,74,176)
os1.print_osoba()

print(f'czy osoba jest trenerem? ({os1.czytrener()})')

print("___________________ Sport ______________________")
sp1 = Sport("Biegi Ultra",7,"50km 7h 23min 34s")
print(sp1.infosport())
