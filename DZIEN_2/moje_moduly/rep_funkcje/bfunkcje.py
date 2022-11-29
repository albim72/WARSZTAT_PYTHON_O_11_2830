def czytaj_liste(lista):
    for i,j in enumerate(lista):
        print(f'-> element listy br {i+1} -> {j}')
        
        
def czytaj_dict(slownik):
    for x,y in slownik.items():
        print(f'klucz -> {x}: wartość -> {y}.')
