
# ekrana yansıtılan diagram dosyasında yer alan 
# sınıf isimlerini kullanarak hiyerarşiyi oluşturalım

from abc import abstractclassmethod

class Arac:
    def __init__(self):
        self.arac = "Arac"
        self.kara = "Kara Araçları"
        self.deniz = "Deniz Araçları"
        self.araba = "Araba"
    def yaz1(self):
        print(self.arac)

class Kara(Arac):
    def __init__(self):
        super().__init__()
    self.k
    

class Deniz(Arac):
    self.deniz = "Deniz araçları"

class Araba(Kara):
    pass