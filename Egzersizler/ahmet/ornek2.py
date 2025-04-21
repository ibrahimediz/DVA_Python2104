
# ekrana yansıtılan diagram dosyasında yer alan 
# sınıf isimlerini kullanarak hiyerarşiyi oluşturalım
class Arac:
    def __init__(self):
        self.a = "Arac"
    def soyle(self):
        print("Araç")
    
class KaraAraclari(Arac):
    def __init__(self):
        super().__init__()
        self.b = "Kara Aracı"
    def soyle(self):
        print("Kara Aracı")
class Araba(KaraAraclari):
    def __init__(self):
                
        self.d = "Araba"
    def soyle(self):
        print("Araba")  
class DenizAraclari(Arac):
    def __init__(self):
            
        self.c = "Deniz Aracı"
    def soyle(self):
        print("Deniz Aracı")
          



