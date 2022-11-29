#przygotuj klasę twworzącą krotkę z wartościami dodatnimi ma bazie dowolnej listy wartości,
#tak aby dodatkowo zliczała wszystkie wartości odrzucone
class PositiveTuple(tuple):
    def __new__(cls, *numbers):
        skipped_values = 0
        pos_numbers = []
        for x in numbers:
            if x>=0:
                pos_numbers.append(x)
            else:
                skipped_values += 1
        instance = super().__new__(cls,tuple(pos_numbers))
        instance.skipped_values = skipped_values
        return instance

pints = PositiveTuple(-3,5,6,10,5,5,5,0,-23,1,888,0,67,-8,2334,5,5,5,5)
print(pints)
print(type(pints))
print(f'liczba odrzuconych wartości: {pints.skipped_values}')
print(f'ile razy występuje 5? -> {pints.count(5)}')
