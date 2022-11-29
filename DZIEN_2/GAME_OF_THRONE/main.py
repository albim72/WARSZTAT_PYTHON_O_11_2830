from tywin import Tywin
from tyrion import Tyrion
from cersei import Cersei

tyw = Tywin("Lannister","Lord","m",9,8,7)
tyr = Tyrion("Lannister","Lord","m",3,9,9)
cer = Cersei("Lannister","Queen","k",5,9,9)

print("___________ Lord Tywin ______________")
tyw.walka()
tyw.negocjacja()
tyw.uczta()
print("___________ Lord Tyrion ______________")
tyr.walka()
tyr.negocjacja()
tyr.uczta()
print("___________ Królowa Cersei ______________")
cer.walka()
cer.negocjacja()
cer.uczta()
