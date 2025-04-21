
# ekrana yansıtılan diagram dosyasında yer alan 
# sınıf isimlerini kullanarak hiyerarşiyi oluşturalım
from abc import ABC, abstractmethod

class Arac: 
    pass

class KaraAraclari(Arac):
    pass

class DenizAraclari(Arac):
    pass

class Araba(KaraAraclari):
    pass



print(type(DenizAraclari()) is Arac)