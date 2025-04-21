class Cokgen:
    def __init__(self,adi,kenarsayisi):
        self.adi=adi
        self.kenarsayi=kenarsayisi
        self.icacitoplamı=180*(kenarsayisi-2)
    def bilgi(self):
        print(self.adi)
        print(self.kenarsayi)
        print(self.icacitoplamı)
        
obj1=Cokgen("Üçgen",3)
obj1.bilgi()


