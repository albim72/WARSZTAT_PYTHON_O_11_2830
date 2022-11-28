liczby = [56,9009,345,678,-987,0,98,7,6,12,3,4,145,122,-133,9,10]

def pokaz_statystyki(dane):
    minimum = min(dane)
    maksimum = max(dane)
    rozstep = maksimum - minimum
    suma_danych = sum(dane)
    le = len(dane)
    avg = suma_danych/le
    return minimum,maksimum,rozstep,suma_danych,avg

wynik = pokaz_statystyki(liczby)
print(wynik)

mini,maxi,roz,sm,avg = pokaz_statystyki(liczby)
print(f"wartość najmniejsza: {mini}, wartość największa: {maxi}, rozstęp: {roz}, suma danych: {sm}, "
      f"średnia arytmetyczna :{avg}")
