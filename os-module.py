import os

xx = os.name
print(xx) #işletim sistemini söyler
hangidizin = os.getcwd()
print(hangidizin)
#os.chdir("yol belirtir ve dizin oluşturur")
#os.mkdir("newfile")
print(os.listdir('C:\\')) #bize klasördekileri listeler

os.system("notepad.exe")
yy = os.path.abspath("C:\\") #tam dosyanın isminin yerini alırız
sx= os.path.dirname("C://") #dosya yolunu verir
#dizin ismini almak için
dizin = os.path.dirname(os.path.abspath("newfile"))
#os.path.exist ile dosya veya klasör sorgulayabiliriz.

konumyap = os.path.join("c:\\","deneme")
#splitext isim dosya uzantısını ayırır
