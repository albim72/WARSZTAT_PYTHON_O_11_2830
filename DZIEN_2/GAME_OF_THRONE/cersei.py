from rod import CzlonekRodu

class Cersei(CzlonekRodu):

    def walka(self):
        if self.punkty_walki == 10:
            print("Królowa dowodzi na polu walki...")
        else:
            print("Królowa pozostaje w pałacu....")

    def negocjacja(self):
        if self.punkty_palacowe >=8 and self.doswiadczenie >= 7:
            print("Królowa wysłana do negocjacji...")
        else:
            print("Królowa pozostaje w pałacu....")

    def uczta(self):
        if self.punkty_palacowe >= 6 and self.doswiadczenie >=8:
            print("Królowa jedzie na ucztę....")
        else:
            print("Królowa zostaje w pałacu.....")
