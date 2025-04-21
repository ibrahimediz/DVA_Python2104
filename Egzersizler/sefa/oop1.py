class Cokgen:
    def __init__(self, adi,kenarSayisi):
        self.adi = adi
        self.kenarSayisi = kenarSayisi
    
    def getInfo(self):
        print(f"{self.adi}, {self.kenarSayisi}")


ucgen = Cokgen("ucgen",3)
ucgen.getInfo()
