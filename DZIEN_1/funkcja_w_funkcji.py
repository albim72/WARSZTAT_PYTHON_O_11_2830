#przykład 1

def witaj(imie):
    return f"Miło Cię widzieć {imie}"

def konkurs(imie,punkty):
    return f"uczestnik {imie}, liczba punktów = {punkty}"

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Leon"))
print(osoba(konkurs,"Olga",67))

#przykład 2

def rejestracja(oplata):
    def lista():
        return "jesteś na liście zawodników"
    def brak():
        return "jeśli chcesz znależć się na liście zawodników, dokonaja wpłaty"
    def error():
        return "podaj 1 - wpłata, 0 - brak wpłaty"

    if oplata == 1:
        return lista
    elif oplata == 0:
        return brak
    else:
        return error


print(rejestracja(1)())
print(rejestracja(0)())
print(rejestracja(13)())

#przykład 3

def startstop(funkcja):
    def wrapper(*args):
        print("startowanie procesu")
        funkcja(*args)
        print("kończenie procesu...")
    return wrapper

def zawijanie():
    print(f"zawijanie czekoladek w sreberka")
print("____________________________________")
zw = startstop(zawijanie)
zw()

@startstop
def dmuchanie(czego):
    print(f"dmuchanie {czego} na imprezę")

dmuchanie("baloników")

print("____________________________________")
@startstop
def fx(n):
    print(f"wynik = {n*1.67888}")

fx(5.66)
