#with open("ornek.csv","r+") as d1,#     open("ornek2.csv","w+") as d2:
#yukarıda dosyalardan yola çıkarak d1 dosyası içerisinde yer alan
#ilk bölümdeki kayıttan noktalama işaretlerini temizleyelim.temiz kaydı d2 dosyasına kaydedelim.

import csv
import re
from string import punctuation
liste = []
with open("Egzersizler/nisa/ornek.csv", "r+") as d1:
    satirlar = d1.readlines()
    for satir in satirlar:
        kayit = satir.split(";")
        yeni = re.sub(r"[^\w\s]", "", kayit[0])
        liste.append(yeni)
with open("Egzersizler/nisa/ornek2.csv","w+") as d2:
    for yazi in liste:
        d2.write(yazi)


