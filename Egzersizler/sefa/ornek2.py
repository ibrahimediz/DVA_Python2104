
# ekrana yansıtılan diagram dosyasında yer alan 
# sınıf isimlerini kullanarak hiyerarşiyi oluşturalım

from abc import ABC, abstractmethod
class Arac(ABC):
    @abstractmethod
    def yakitAl(self):
        pass



class KaraAraclari(Arac):
    def __init__(self,tekerlekSayisi = 4,arabaYasi= 0):
            self.tekerlek_sayisi = tekerlekSayisi   
            self.arabaYasi = arabaYasi
    def yakitAl(self):
        print("Kara araci yakit alma.")



class DenizAraclari(Arac):
    def yakitAl(self):
        print("Deniz araci yakit alma.")



class Araba(KaraAraclari):
    def __init__(self):
        super().__init__()

    def yakitAl(self):
        print("Yakit alma Araba classi içinden")

denizaraci = DenizAraclari()
denizaraci.yakitAl()
karaaraclari = KaraAraclari()
karaaraclari.yakitAl()
araba1 = Araba()
araba1.yakitAl()