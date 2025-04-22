
# with open("ornek.csv","r+") as d1,#     open("ornek2.csv","w+") as d2:
# yukarıda dosyalardan yola çıkarak d1 dosyası içerisinde yer alan
# ilk bölümdeki kayıttan noktalama işaretlerini temizleyelim.temiz kaydı d2 dosyasına kaydedelim.


# with open("ornek.csv","r+") as d1,#     open("ornek2.csv","w+") as d2:
# yukarıda dosyalardan yola çıkarak d1 dosyası içerisinde yer alan
# ilk bölümdeki kayıttan noktalama işaretlerini temizleyelim.temiz kaydı d2 dosyasına kaydedelim.

from string import punctuation

with open("/workspace/DVA_Python2104/Egzersizler/furkan_topaloglu/ornek.csv", "r") as d1, \
     open("/workspace/DVA_Python2104/Egzersizler/furkan_topaloglu/ornek2.csv", "w") as d2:
    for item in d1.readlines():
        kayit = item.split(";")
        
        # İlk alanı (isim) noktalama işaretlerinden temizle
        kayit[0] = "".join([kar for kar in kayit[0] if kar not in punctuation])
        
        # Düzeltilmiş kaydı hedef dosyaya yaz
        print(";".join(kayit), end="", file=d2)

print("İşlem tamamlandı.")
