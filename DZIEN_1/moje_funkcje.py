from drugie_funkcje import zewnetrzna
#funkcja 1

def k(j):
    return j**5

n = 18
def policz(a,b,c,y):
    global n
    n = (a+b)*y - c + n + k(b)
    return n

print(policz(5,7,2,2))
print(n)

zewnetrzna()

