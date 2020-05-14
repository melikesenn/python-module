"""
Bu modül ile web üzerindeki isteklerinizi yöneteceksiniz. Mesela bu modül ile API entpointlerine PUT, DELETE, POST gibi istekler atabilirsiniz.
"""
import requests
import json

cevap = requests.get("https://jsonplaceholder.typicode.com/todos")

print(cevap.text)
print(type(cevap))

metin = json.loads(cevap.text)
print(metin[5]["title"])