print((lambda e:e**2)(56))

b = lambda u,m:u+202-m
print(b(6,2))

def func_t(u,m):
    return u+202-m

print(func_t(6,7))

def ob(k):
    return lambda a,n:a*k+2*n

print(ob(2)(n=6, a=2))
