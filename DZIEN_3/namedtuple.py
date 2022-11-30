from collections import namedtuple

pracownik = namedtuple('Pracownik',['imie','nazwisko','stanowisko','wynagrodzenie'])
p = pracownik('Olga','Nowak','dyrektor',10700)

print(f"imię pracownika o indeksie 0: {p[0]}")
print(f"imię pracownika o indeksie 0: {p.imie}")
print(getattr(p,'stanowisko'))

pli = ['Jan','Kowal','kierowca',5500]

pdi = {'imie':'Nadia','nazwisko':'Maj','stanowisko':'sekretarka','wynagrodzenie':5400}

print(pracownik._make(pli))
print(p._asdict())

print(pracownik(**pdi))

print(p._fields)
print(p._replace(nazwisko='Kowalik'))
print(p)
