
# with open("ornek.csv","r+") as d1,#     open("ornek2.csv","w+") as d2:
# yukarıda dosyalardan yola çıkarak d1 dosyası içerisinde yer alan
# ilk bölümdeki kayıttan noktalama işaretlerini temizleyelim.temiz kaydı d2 dosyasına kaydedelim.


# with open("ornek.csv","r+") as d1,#     open("ornek2.csv","w+") as d2:
# yukarıda dosyalardan yola çıkarak d1 dosyası içerisinde yer alan
# ilk bölümdeki kayıttan noktalama işaretlerini temizleyelim.temiz kaydı d2 dosyasına kaydedelim.


import csv 
import string

with open("ornek.csv", "r", encoding="utf-8") as d1, open("ornek2.csv", "w", newline='', encoding="utf-8") as d2:
    reader = csv.reader(d1)
    writer = csv.writer(d2)

    first_row = next(reader)
    cleaned_row = [cell.translate(str.maketrans('', '', string.punctuation)) for cell in first_row]

    writer.writerow(cleaned_row)

