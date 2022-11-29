class MojeSlowniki(dict):
    def __missing__(self, key):
        return 'taki klucz nie istnieje!'

konkurs = {'Henryk':67,'Olaf':78,'Monika':90,"Romek":82}
print(konkurs["Henryk"])
#print(konkurs["Marek"])

mkonkurs = MojeSlowniki(konkurs)
print(mkonkurs["Henryk"])
print(mkonkurs["Marek"])
