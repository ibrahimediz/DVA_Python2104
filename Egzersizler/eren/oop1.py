class Cokgen:
    def __init__(self,*args):
        self.isim, self.kenar_sayisi = args
        self.ic_acilar = (self.kenar_sayisi-2)*180

    def bilgi(self):
        print(self.isim)
        print(self.kenar_sayisi)
        print(self.ic_acilar)

cokgen1 = Cokgen("kare", 4)
cokgen1.bilgi()