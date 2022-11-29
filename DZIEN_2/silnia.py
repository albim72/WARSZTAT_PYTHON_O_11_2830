#n! = 1*2*3*....*n, n>=0
#double max-> 1.8E308, min 2.4E-324
#n?? 171!
import sys

sys.set_int_max_str_digits(100000000)
sys.setrecursionlimit(0x1000000)

print(sys.getrecursionlimit())

def silnia(n):
    if n<0:
        raise ValueError("silnia nie jest zdefiniowana dla liczb ujemnych!")
    wynik=1
    for i in range(1,n+1):
        wynik*=i
    return wynik

def silnia_rek(n):
    if n<0:
        raise ValueError("silnia nie jest zdefiniowana dla liczb ujemnych!")
    if n==0:
        return 1
    else:
        return n*silnia_rek(n-1)

try:
    n = int(input("podaj wartość atrybutu n funkcji silnia: "))
    print(f'silnia z {n} wynosi: {silnia(n)}')
    print(f'silnia rekurencyjna z {n} wynosi: {silnia_rek(n)}')
except ValueError as d:
    print(d)
