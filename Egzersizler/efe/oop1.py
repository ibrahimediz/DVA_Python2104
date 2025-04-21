class Cokgen:
    def __init__(self,adi, kenarsayisi):
        self.kenarSay = kenarSayisi
        selfaciToplam = 180*(kenarSayisi-2)


    def bilgi(self):
        print("#"*30)
        print("Adı:",self.adi)
        print("Kenar Sayısı:",self.kenarSay)
        print("Açı Toplam:",self.aciToplam)
        print("#"*30)

ucgen = Cokgen("Üçgen",3)
ucgen.bilgi()
