
# with open("ornek.csv","r+") as d1,#     open("ornek2.csv","w+") as d2:
# yukarıda dosyalardan yola çıkarak d1 dosyası içerisinde yer alan
# ilk bölümdeki kayıttan noktalama işaretlerini temizleyelim.temiz kaydı d2 dosyasına kaydedelim.


# with open("ornek.csv","r+") as d1,#     open("ornek2.csv","w+") as d2:
# yukarıda dosyalardan yola çıkarak d1 dosyası içerisinde yer alan
# ilk bölümdeki kayıttan noktalama işaretlerini temizleyelim.temiz kaydı d2 dosyasına kaydedelim.


import csv
import string
noktalama = list(str(punctuation))
noktalama.remove(";")
with open("ornek.csv","r+") as d1,\
    open("ornek2.csv","w+") as d2:
    pass
csv=d1.readline()
print(csv)


with open("ornek.csv","r+") as d1,\
    open("ornek2.csv","w+") as d2:
    for item in d1.readlines():