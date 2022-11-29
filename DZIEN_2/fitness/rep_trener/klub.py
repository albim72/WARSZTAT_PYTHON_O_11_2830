class Klub:
    def __init__(self,nr_kb,nazwa,adres):
        self.nr_kb = nr_kb
        self.nazwa = nazwa
        self.adres = adres
        self.przypisanie()
        
    def infoklub(self):
        return f'klub {self.nazwa}, numer filii: {self.nr_kb}'
    
    def przypisanie(self):
        print(f"przypisanie do klubu {self.nazwa} {self.nr}")
