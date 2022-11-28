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
