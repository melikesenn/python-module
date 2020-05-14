# JSON cihazlar arasında veri taşıma yapısı sağlar
#json verileri bize string şekilde gelir biz orada dictionaryi işlemleri yapmaya çalışırız.

import json

metin = '{"name":"meli", "city" :["ist","ank"]}'

json1 = json.loads(metin)  #dictionarye çevrildi
print(json1["name"])

"""
with open("person.json") as f:
    result = json.load(f)
    print(result)
"""

#metin elemanını jsona çevirme

xx = json.dumps(metin)
print(type(xx))

"""
DOSYAYA YAZMA
"""
with open("sss.json","w") as f:
    json.dump("metin",f)
json.dumps("metin",indent =2, sort_keys = True) #her alt eleamnda boşluk sayısını belirtir

print(json.__file__) #dosya konumu