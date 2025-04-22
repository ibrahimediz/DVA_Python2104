
# with open("ornek.csv","r+") as d1,#     open("ornek2.csv","w+") as d2:
# yukarıda dosyalardan yola çıkarak d1 dosyası içerisinde yer alan
# ilk bölümdeki kayıttan noktalama işaretlerini temizleyelim.temiz kaydı d2 dosyasına kaydedelim.


# with open("ornek.csv","r+") as d1,#     open("ornek2.csv","w+") as d2:
# yukarıda dosyalardan yola çıkarak d1 dosyası içerisinde yer alan
# ilk bölümdeki kayıttan noktalama işaretlerini temizleyelim.temiz kaydı d2 dosyasına kaydedelim.

import string

with open("ornek.csv", "r") as d1, open("ornek2.csv", "w") as d2:
    for satir in d1:
        alanlar = satir.strip().split(";")  # Satırı parçalara ayır
        if alanlar:  # boş satır kontrolü
            # İlk alanı al ve noktalama işaretlerini çıkar
            temiz_alan = ''.join(c for c in alanlar[0] if c not in string.punctuation)
            alanlar[0] = temiz_alan  # ilk alanı temiz haliyle değiştir
            print(";".join(alanlar), file=d2)  # yeni dosyaya yaz
