
# with open("ornek.csv","r+") as d1,#     open("ornek2.csv","w+") as d2:
# yukarıda dosyalardan yola çıkarak d1 dosyası içerisinde yer alan
# ilk bölümdeki kayıttan noktalama işaretlerini temizleyelim.temiz kaydı d2 dosyasına kaydedelim.


# with open("ornek.csv","r+") as d1,#     open("ornek2.csv","w+") as d2:
# yukarıda dosyalardan yola çıkarak d1 dosyası içerisinde yer alan
# ilk bölümdeki kayıttan noktalama işaretlerini temizleyelim.temiz kaydı d2 dosyasına kaydedelim.

import string

with open("Egzersizler/alperen/ornek.csv", "r") as dosya:
    satirs = dosya.readlines()

temiz = []

for satir in satirs:
    temizsatir = ''.join(char for char in satir if char not in string.punctuation)
    temiz.append(temizsatir)

with open("Egzersizler/alperen/ornek2.csv", "w") as dosya:
    dosya.writelines(temiz)