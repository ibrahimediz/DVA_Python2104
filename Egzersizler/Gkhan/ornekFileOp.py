
# with open("ornek.csv","r+") as d1,#     open("ornek2.csv","w+") as d2:
# yukarıda dosyalardan yola çıkarak d1 dosyası içerisinde yer alan
# ilk bölümdeki kayıttan noktalama işaretlerini temizleyelim.temiz kaydı d2 dosyasına kaydedelim.


# with open("ornek.csv","r+") as d1,#     open("ornek2.csv","w+") as d2:
# yukarıda dosyalardan yola çıkarak d1 dosyası içerisinde yer alan
# ilk bölümdeki kayıttan noktalama işaretlerini temizleyelim.temiz kaydı d2 dosyasına kaydedelim.

import csv
import re
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent.parent / 'Egzersizler'
# Noktalama işaretlerini temizlemek için bir regex
def temizle_ilk_bolum(satir):
    bolumler = satir.split(";")
    ilk_bolum = re.sub(r'[^\w\s]', '', bolumler[0])  # Noktalama işaretlerini kaldır
    bolumler[0] = ilk_bolum
    return ";".join(bolumler)

# Girdi ve çıktı dosyaları
with open("worksdfsdfsdfsing="utf-8") as infile, \
     open("ornek2.csv", "w", encoding="utf-8", newline="") as outfile

    reader = csv.reader(infile, delimiter=';')
    writer = csv.writer(outfile, delimiter=';')

    for row in reader:
        # Satırı birleştirip ilk bölümü temizleyip tekrar ayır
        tam_satir = ";".join(row)
        temiz_satir = temizle_ilk_bolum(tam_satir).split(";")
        writer.writerow(temiz_satir)
