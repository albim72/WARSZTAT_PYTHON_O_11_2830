from dataclasses import dataclass
from datetime import datetime

@dataclass
class Person:
    name:str
    surname:str
    year_of_birth:int

    @property
    def age(self):
        return datetime.now().year - self.year_of_birth

p = Person('Janusz','Gierej',1968)
print(p)
print(p.age)

# ze zwykłą klasą takie rzeczy nie przejdą!!!

# class Dog:
#     name:str
#     age:int
#     
# dg = Dog("Olo",2)
# print(dg)
