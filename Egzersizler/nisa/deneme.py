class Cokgen:
    def __init__(self,adi,kenarsayisi):
        self.adi = adi
        self.kenarsayi = kenarsayisi
        self.aci = 180*(kenarsayisi-2)
    def bilgi(self):
        print("Adi:", self.adi)
        print("Kenar sayisi:", self.kenarsayi)
        print(self.aci)
ucgen = Cokgen("nisa",3) 
ucgen.bilgi()
