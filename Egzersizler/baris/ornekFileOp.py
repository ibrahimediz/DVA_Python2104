
# with open("ornek.csv","r+") as d1,#     open("ornek2.csv","w+") as d2:
# yukarıda dosyalardan yola çıkarak d1 dosyası içerisinde yer alan
# ilk bölümdeki kayıttan noktalama işaretlerini temizleyelim.temiz kaydı d2 dosyasına kaydedelim.


from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent / 'baris'
print(BASE_DIR)
d1 = open("/workspace/DVA_Python2104/baris/ornek.csv","r+")
#d2 = "".join(list(d1).remove(";"))