
# with open("ornek.csv","r+") as d1,#     open("ornek2.csv","w+") as d2:
# yukarıda dosyalardan yola çıkarak d1 dosyası içerisinde yer alan
# ilk bölümdeki kayıttan noktalama işaretlerini temizleyelim.temiz kaydı d2 dosyasına kaydedelim.


# with open("ornek.csv","r+") as d1,#     open("ornek2.csv","w+") as d2:
# yukarıda dosyalardan yola çıkarak d1 dosyası içerisinde yer alan
# ilk bölümdeki kayıttan noktalama işaretlerini temizleyelim.temiz kaydı d2 dosyasına kaydedelim.

from string import punctuation
with open("/workspace/DVA_Python2104/Egzersizler/Ibrahim/ornek.csv","r+") as d1,\
    open("/workspace/DVA_Python2104/Egzersizler/Ibrahim/ornek2.csv","w+") as d2:
    for item in d1.readlines():
        kayit = item[:item.index(";")]
        # print(kayit[0])
        # print("".join([kar for kar in kayit[0] if kar not in punctuation]))
        kayit = "".join([kar for kar in kayit if kar not in punctuation])
        print(";".join(kayit),end="",file=d2)


# # E029R94%5y0p"9Wo-(3{
# E029R945y0p9Wo3
# # ^>[vWA<^!3F4hDa255P2
# vWA3F4hDa255P2
# # >kF6W.<-f54>5[90/x06
# kF6Wf54590x06
