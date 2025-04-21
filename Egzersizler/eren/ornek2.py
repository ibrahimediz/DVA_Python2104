
# ekrana yansıtılan diagram dosyasında yer alan 
# sınıf isimlerini kullanarak hiyerarşiyi oluşturalım

class Arac():
    def __init__(self,hiz):
        self.hiz = hiz
    def getSpeed(self):
        print(self.hiz)

class KaraAraclari(Arac,hiz):
    def __init__(self):
        super().__init__()
        self.hiz = hiz

class DenizAraclari(Arac):
    pass

class Araba(KaraAraclari):
    pass


Ferrari = KaraAraclari(10)