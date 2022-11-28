import math
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
