class NegativeValueException(Exception):
    def __init__(self,value):
        self.value = value
        
    def __str__(self):
        return f'wartość która wynosi {self.value} jest ujemna. Silnia nie jest ' \
               f'zdefiniowana dla liczb ujemnych'
