import os
liste = ['Ibrahim', 'mss', 'eren', 'nisa', 'ilker',
 'onur', 'ahmet', 'sultan', 'sefa', 'Sena', 'baris',
  'efe', 'furkanunsal', 'furkan_topaloglu', 'alperen', 'Gkhan',"ogun"]
dosyaismi = "ornekFileOp.py"
sorumetni = """
# with open("ornek.csv","r+") as d1,\
#     open("ornek2.csv","w+") as d2:
# yukarıda dosyalardan yola çıkarak d1 dosyası içerisinde yer alan
# ilk bölümdeki kayıttan noktalama işaretlerini temizleyelim.temiz kaydı d2 dosyasına kaydedelim.

"""
for item in liste:
    if not os.path.exists(f"Egzersizler/{item}"):
      os.mkdir(f"Egzersizler/{item}")
    with open(f"Egzersizler/{item}/{dosyaismi}","a+") as dosya:
      dosya.write(sorumetni)


