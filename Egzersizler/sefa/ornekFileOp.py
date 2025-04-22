
# with open("ornek.csv","r+") as d1,#     open("ornek2.csv","w+") as d2:
# yukarıda dosyalardan yola çıkarak d1 dosyası içerisinde yer alan
# ilk bölümdeki kayıttan noktalama işaretlerini temizleyelim.temiz kaydı d2 dosyasına kaydedelim.

import csv
from string import ascii_letters,punctuation,digits
# from pathlib import Path
# BASE_DIR = Path(__file__).resolve().parent.parent.parent
# print(BASE_DIR)
# print(type(punctuation))
print(punctuation)
with open("ornek.csv","r+") as d1, open("ornek2.csv","w+") as d2:
    for line in d1.readlines():
        line = line.split(";")
        line[0] = "".join([kar for kar in line[0] if kar not in punctuation])
        # for i in line[0]:
        #     if i in punctuation:
        #         # print(i)
        #         line[0].replace(i)
        print(";".join(line), end="", file=d2)