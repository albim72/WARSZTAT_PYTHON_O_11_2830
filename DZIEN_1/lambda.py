import math

print((lambda e:e**2)(56))

b = lambda u,m:u+202-m
print(b(6,2))

def func_t(u,m):
    return u+202-m

print(func_t(6,7))

def ob(k):
    return lambda a,n:a*k+2*n

print(ob(2)(n=6, a=2))

num = [67,2,5,177,-99,0,9,12,7,1,-4,0,5,7,18,2,2,2,0]
zn = {6,7,99,-5,0,34,2,67,88,0,88,2,6,2,2,0}

#stwórz listę liczbyparz i przekaż do niej wszystkie wartości parzyste z listy num
#użyj funkcji filter, która jest funcją standardową wyższego rzędu(parametr zerowy funkcji jest funckją,
# paramietr pierwszy jest kolekcją danych

liczbyparz = list(filter(lambda x:x%2==0,num))
print(liczbyparz)

def warunek(x):
    return x%2==0

liczbyparz_2 = list(filter(warunek,num))
print(liczbyparz_2)

#stwórz listę cube i przekaż do niej wszystkie wartości z listy num podniesione do potęgi 3
#użyj funkcji standardowej wyższego rzędu map()

cube = list(map(lambda x:x**3,num))
print(cube)

cube = list(map(lambda x:x**3,zn))
print(cube)


#własne funkcje wyższego rzędu
def filtruj(dane,test):
     plus = []
     for element in dane:
         if (test(element)):
             plus.append(element)
     return plus

def ekstra_liczba(n):
    return n>=100

lb = [119,8,10,-189,23,445,45,67,99,101]
print(filtruj(lb,ekstra_liczba))

def mapowanie(dane,transformacja):
    mapa=[]
    for element in dane:
        mapa.append(transformacja(element,(element/3)))
    return mapa

def addfive(n,k=0):
    return n+5

def licz(k,m):
    return k*m/4

def piwerw(k,m):
    return k*math.sqrt(abs(m))

print(mapowanie(lb,addfive))
print(mapowanie(lb,licz))
print(mapowanie(lb,piwerw))
