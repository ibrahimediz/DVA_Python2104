
# ekrana yansıtılan diagram dosyasında yer alan 
# sınıf isimlerini kullanarak hiyerarşiyi oluşturalım
from abc import ABC,abstractclassmethod,abstractmethod
class Arac(ABC):
    @abstractmethod
    def yakital(self):
        pass
class KaraAraclari(Arac,Araba):
    def yakital(self):
        pass

class Araba:
    def __init__(self):
        pass
class DenizAraclari(Arac):
    def yakital(self):
        pass
