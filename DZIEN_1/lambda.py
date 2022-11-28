print((lambda e:e**2)(56))

b = lambda u,m:u+202-m
print(b(6,2))

def func_t(u,m):
    return u+202-m

print(func_t(6,7))

def ob(k):
    return lambda a,n:a*k+2*n

print(ob(2)(n=6, a=2))

num = [67,2,5,177,-99,0,9,12,7,1,-4,0,5,7,18]

#stwórz listę liczbyparz i przekaż do niej wszystkie wartości parzyste z listy num
#użyj funkcji filter, która jest funcją standardową wyższego rzędu(parametr zerowy funkcji jest funckją,
# paramietr pierwszy jest kolekcją danych

liczbyparz = list(filter(lambda x:x%2==0,num))
print(liczbyparz)

def warunek(x):
    return x%2==0

liczbyparz_2 = list(filter(warunek,num))
print(liczbyparz_2)

