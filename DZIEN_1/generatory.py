#przykład 1

def liczby():
    for i in range(16):
        yield i*2

for p in liczby():
    print(p)

#przykład 2

def wznowienie(n,k):
    print("wstrzymanie działania...")
    yield 1001
    print("wznowienie działania...")

    print("wstrzymanie działania...")
    yield n+k
    print("wznowienie działania...")

    print("wstrzymanie działania...")
    yield n*k
    print("wznowienie działania...")

    print("wstrzymanie działania...")
    yield n**k
    print("wznowienie działania...")

for i in wznowienie(5,8):
    print(f"zwrócono wartość -> {i}")

#przykład 3
import time
def genret():
    for i in range(7):
        if i==5:
            print("Przerwanie")
            return
        else:
            time.sleep(2)
            yield i

for t in genret():
    if t==2:
        continue
    print(t)
