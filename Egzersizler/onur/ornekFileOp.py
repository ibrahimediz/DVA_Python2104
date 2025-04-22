
# with open("ornek.csv","r+") as d1,#     open("ornek2.csv","w+") as d2:
# yukarıda dosyalardan yola çıkarak d1 dosyası içerisinde yer alan
# ilk bölümdeki kayıttan noktalama işaretlerini temizleyelim.temiz kaydı d2 dosyasına kaydedelim.


# with open("ornek.csv","r+") as d1,#     open("ornek2.csv","w+") as d2:
# yukarıda dosyalardan yola çıkarak d1 dosyası içerisinde yer alan
# ilk bölümdeki kayıttan noktalama işaretlerini temizleyelim.temiz kaydı d2 dosyasına kaydedelim.

from string import punctuation

with open('ornek.csv', 'r+', newline='') as d1, \
    open("ornek2.csv","w+") as d2:
    for row in d1.readlines():
        record = row[:row.index(";")]
        record = "".join([item for item in record if item not in punctuation])
        record = [record] + row.split(";")[1:]
        print(";".join(record), end="", file=d2)