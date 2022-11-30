from dataclasses import dataclass

@dataclass
class Article:
    title:str
    content:str
    author:str

@dataclass(init=False)
class PyArticle(Article):
    language:str
    author:str
    price:int = 0

    def __init__(self,title,price):
        self.title = title
        self.price = price
        self.language = "Python 3"
        self.author = "Marcin Albiniak"
        self.content = "opis wybranych aspektów użycia języka Python"

    def rabat(self):
        print(f"Publikacja -> tytul: {self.title}, autor: {self.author}, "
              f"cena bazowa: {self.price} zł, cena po rabacie: {0.9*self.price} zł")

art1 = PyArticle("Algorytmiczna teoria gier w Pythonie",120)
print(art1)
art1.rabat()


