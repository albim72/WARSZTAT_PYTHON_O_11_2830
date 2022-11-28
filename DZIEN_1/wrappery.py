import math
import time

def pomiarczasu(funkcja):
    def wrapper():
        starttime = time.perf_counter()
        funkcja()
        endtime = time.perf_counter()
        print(f'czas wykonania funkcji: {endtime-starttime} s')
    return wrapper

def sleep(funkcaimport math
import time

def pomiarczasu(funkcja):
    def wrapper():
        starttime = time.perf_counter()
        funkcja()
        endtime = time.perf_counter()
        print(f'czas wykonania funkcji: {endtime-starttime} s')
    return wrapper

def sleep(funkcja):
    def wrapper():
        time.sleep(4)
        return funkcja()
    return wrapper



@pomiarczasu
@sleep
def big_lista():
    sum([i**2 for i in range(10000000) if i%2==0])

big_lista()

lt = [i**2 for i in range(10000000) if i%2==0]
@pomiarczasu
def drugalista():
    sum(lt)

drugalista()

@pomiarczasu
def trzecialista():
    sum([math.pow((i+4)**2,4) for i in range(10000000)])

trzecialista()


#dekorator z funkcją magiczną  __name__

def debug(funkcja):
    def wrapper(*args,**kwargs):
        print(f"wołana funkcja to: {funkcja.__name__}")
        funkcja(*args)
    return wrapper


@debug
def info(i):
    print(f"informacja: {i}")

info("blok nr 324567")ja):
    def wrapper():
        time.sleep(4)
        return funkcja()
    return wrapper



@pomiarczasu
@sleep
def big_lista():
    sum([i**2 for i in range(10000000) if i%2==0])

big_lista()

lt = [i**2 for i in range(10000000) if i%2==0]
@pomiarczasu
def drugalista():
    sum(lt)

drugalista()

@pomiarczasu
def trzecialista():
    sum([math.pow((i+4)**2,4) for i in range(10000000)])

trzecialista()
