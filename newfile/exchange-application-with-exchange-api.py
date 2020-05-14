import json
import requests


api = "https://api.exchangeratesapi.io/latest?base="
bozulacakdöviz= input("bozulacak dövix türünü giriniz:")
alinacakdöviz = input("alınacak döviz türü")
miktar = int(input(f"ne kadar {bozulacakdöviz} bozulacak"))

result = requests.get(api+bozulacakdöviz)
result = json.loads(result.text) #json bilgiyi çevirdik
print(result)

print(" 1 {0} = {1} {2} ".format(bozulacakdöviz,result["rates"][alinacakdöviz],alinacakdöviz))
print("{0} {1} = {2} {3}".format(miktar,bozulacakdöviz,miktar*result["rates"][alinacakdöviz],alinacakdöviz))


