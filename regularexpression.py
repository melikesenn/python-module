#arama sonucunda sonuç döndürmeyi sağlar

import re

metin = "melii ppp"

print(re.findall("meli",metin))

parca = re.search(" ",metin)
print(parca)

yenisonuc = re.sub(" ", "**",metin)
print(yenisonuc)

ara = re.search("meli",metin)
print(ara.span())
print(ara.start())
print(ara.end())

result = re.findall("[a-e]",metin) #a dan e ye kadar arar [sde,a-5]
print(result)

result1 = re.findall("[^e]",metin) #e hariç arar [^0-9]
print(re.findall("...",metin))
print(re.findall("i$",metin))