
# with open("ornek.csv","r+") as d1,#     open("ornek2.csv","w+") as d2:
# yukarıda dosyalardan yola çıkarak d1 dosyası içerisinde yer alan
# ilk bölümdeki kayıttan noktalama işaretlerini temizleyelim.temiz kaydı d2 dosyasına kaydedelim.


# with open("ornek.csv","r+") as d1,#     open("ornek2.csv","w+") as d2:
# yukarıda dosyalardan yola çıkarak d1 dosyası içerisinde yer alan
# ilk bölümdeki kayıttan noktalama işaretlerini temizleyelim.temiz kaydı d2 dosyasına kaydedelim.

from pathlib import Path
from string import punctuation
BASE_DIR = Path(__file__).resolve().parent

print(BASE_DIR)
with open(fr"{BASE_DIR}/ornek.csv","r+") as d1, \
    open(fr"{BASE_DIR}/ornek2.csv","w+") as d2:
     for x in d1.readlines():
        map(x.split(";"))
