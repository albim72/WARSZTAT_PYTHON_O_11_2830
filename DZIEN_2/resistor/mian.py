from oldresistor import OldResistor
from resistor import Resistor
from voltage import VoltageResistance
from bounded import BoundedResistance

print("________________klasa OldResistor____________________")
r0 = OldResistor(10.22E2)
print(r0)
print(r0._ohms)
r0.set_ohms(2.88E3)
print(r0.get_ohms())
print("________________klasa Resistor____________________")
r1 = Resistor(50E3)
r1.ohms = 10E3
print(f'układ elektryczny:\noporność: {r1.ohms} om\nnapięcie prądu:'
      f' {r1.voltage} V\nnatężenie prądu: {r1.current} A')

print("________________klasa VoltageResistance____________________")
r2 = VoltageResistance(1E3)
print(f'natężenie początkow prądu: {r2.current} A')
r2.voltage = 35
print(f'natężenie końcowe prądu: {r2.current} A')
print(f'napięcie końcowe prądu: {r2.voltage} V')

print("________________klasa BoundedResistance____________________")
try:
      r3 = BoundedResistance(1E2)
      r3.ohms = -20
except ValueError as ve:
      print(ve)
except Exception as e:
      print(type(e))
      print(e)
else:
      print(f'oporność wynosi: {r3.ohms}')
finally:
      print(f'używasz klasy: {r3.__class__.__name__}')


