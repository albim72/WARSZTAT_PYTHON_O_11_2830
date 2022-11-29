from oldresistor import OldResistor
from resistor import Resistor

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
