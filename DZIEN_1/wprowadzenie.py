print("pierwsza linia na dobre otwarcie...")
#komentarz standardowy
"""
komentarz dokumentacyjny
wieloliniowy
"""

'''
wieloliniowy
druga linia
'''

#CTRL+D - powielenie linii/bloku
#CTRL+/ - komentowanie/odkomentowanie wielu linii kodu

imiona = ["Jan","Piotr","Paweł","Klaudia","Olga","Anna","Leon","Aneta"]

print(imiona)
print(type(imiona))
print(imiona[2:5])
print(imiona[:3])
print(imiona[2:])
print(imiona[-3])
#dodaj imiona z pozycji parzystch listy imiona
imionaparz = imiona[::2]
print(imionaparz)

im1 = "Jacek"
im2 = "Urszula"

print("imię:",im1,"odwrtonie:",im1[::-1].lower())
print("imię:",im2,"odwrtonie:",im2[::-1].upper())

im_s = imiona
im_e = list(imiona)
im_w = imiona[:]

print(type(im_s))

print(imiona)
print(im_s)
print(im_e)
print(im_w)

imiona[:]=[3,5,6,7,8,9]

print(imiona)
print(im_s)
print(im_e)
print(im_w)

assert imiona == im_s
assert imiona != im_w

h:float
h = 4.567
print(h)
print(type(h))

h = "pogoda"
print(h)
print(type(h))

im_w.sort()
print(im_w)

mlista = ["Kraków",67,0.55,True]

#krotka

miasto = ("Kraków","Lublin","Kielce","Rzeszów","Kalisz","Gdańsk","Kraków")

df = miasto.index("Kielce")
print(df)
print(miasto.count("Kraków"))

lmiasto = list(miasto)
print(lmiasto)

lmiasto.insert(2,"Zamość")
print(lmiasto)

miasto = tuple(lmiasto)
print(miasto)

