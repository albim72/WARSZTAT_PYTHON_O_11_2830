import json

jsonbook = '{"tytul":"Hobbit","autor":"J.R.R. Tolkien","oprawa":"twarda","lstron":288,"cena":32.66}'

print(jsonbook)
print(type(jsonbook))

book = json.loads(jsonbook)
print(book)
print(type(book))
print(f"tytul: {book['tytul']}, cena: {book['cena']} zł")

kolor = {
    "id":2354365,
    "nazwa_koloru":"żółty ciemny",
    "paleta":"UHK56333",
    "lodcieni":12
}

jsonkolor = json.dumps(kolor, indent=4)
print(jsonkolor)


with open("kolor.json","w",encoding="utf-8") as f:
    f.write(jsonkolor)

with open("kolor.json","r",encoding="utf-8") as f:
    kolor_dict = json.load(f)

print(kolor_dict)

print("*********************************************")

infofund = '{"organizacja":"Fundacja Biotech","miasto":"Krosno","kraj":"Polska"}'

ekstra = {"id_proj":4345345,"zakres":"algorytmy AI"}

z = json.loads(infofund)
z.update(ekstra)
info_new = json.dumps(z)
print(info_new)
