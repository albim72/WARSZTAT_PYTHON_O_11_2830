from xml.etree.ElementTree import Element,SubElement,Comment
import xml.etree.ElementTree as ET
from prettyfy import pretty

top = Element('autokomis')

sam1 = SubElement(top,'samochod')

id=SubElement(sam1,'id')
id.text = 's1'

marka=SubElement(sam1,'marka')
marka.text = 'Subaru'

model=SubElement(sam1,'model')
model.text = 'Impreza'

poj=SubElement(sam1,'pojemnosc')
poj.text = '2.0'

rok=SubElement(sam1,'rocznik')
rok.text = '1999'

cena=SubElement(sam1,'cena')
cena.text = '56000'

wyp_dod = SubElement(sam1,'wyposazenie_dod')

pod=SubElement(wyp_dod,'pod')
pod.text = '4'

kolor=SubElement(wyp_dod,'kolor')
kolor.text = 'czarna perła'
