
# ekrana yansıtılan diagram dosyasında yer alan 
# sınıf isimlerini kullanarak hiyerarşiyi oluşturalım


class Arac(ABC):
    def __init__(self,arac):
        self.arac = "Araç Sınıfı"
        pass

    def aracSinif(self):
        print(self.arac)
    
    

class KaraAraclari(Arac):
    def __init__(self,karaAraclari):
        super().__init__()
        self.karaAraci = karaAraclari
        
    def karaArac(self):
        print(self.karaAraci)


class Araba(KaraAraclari):
    def __init__(self,araba):
        super().__init__()
        self.araba = araba
    
    def araba(self):
        print(self.araba)


class DenizAraclari(Arac):
    def __init__(self, denizAraci):
        super().__init__()
        self.denizAraci = denizAraci

    def denizAraci(self):
        print(self.denizAraci)
    