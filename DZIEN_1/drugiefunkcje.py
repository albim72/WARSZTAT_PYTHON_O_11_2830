import math

def zewnetrzna():
    x = "lokalnie"
    def wewnetrzna():
        nonlocal x
        x = "nielokalnie"
        print(f"wewnętrzne x: {x}")
    wewnetrzna()
    print(f"zewnętrzne x: {x}")


#kolejna funkcja

def gx(n,m=4,k=3,b=7):
    return math.sqrt(n+m)*k-b

#W Pythonie nie klasycznego przeciążania fukcji
# def gx(n,m=4):
#     return math.sqrt(n+m)

# ranking

def ranking(r1,r2,r3):
    print(f'ranking języków programowania -> piwerwsze miejsce:{r1},drugie miejsce: {r2},'
          f'trzecie miejsceL {r3}')

