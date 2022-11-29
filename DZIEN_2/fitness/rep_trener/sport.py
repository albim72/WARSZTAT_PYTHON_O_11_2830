class Sport:
    def __init__(self,dyscyplina,lata_upr,zyciowka):
        self.dyscyplina = dyscyplina
        self.lata_upr = lata_upr
        self.zyciowka = zyciowka
        self.sport_przypisanie()

    def infosport(self):
        return f'{self.dyscyplina}, czas uprawiania[lata]: {self.lata_upr}, ' \
               f'życiówka: {self.zyciowka}'

    def sport_przypisanie(self):
        print(f'przypisanie do dyscypliny: {self.dyscyplina}')
