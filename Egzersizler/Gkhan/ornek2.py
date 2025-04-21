
# ekrana yansıtılan diagram dosyasında yer alan 
# sınıf isimlerini kullanarak hiyerarşiyi oluşturalım

from abc import ABC, abstractmethod

class Arac(ABC):
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    @abstractmethod
    def hareket_et(self):
        pass

    @abstractmethod
    def dur(self):
        pass


class KaraAraci(Arac):
    def __init__(self, marka, model, teker_sayisi):
        super().__init__(marka, model)
        self.teker_sayisi = teker_sayisi

    def hareket_et(self):
        print(f"{self.marka} {self.model} karada hareket ediyor.")

    def dur(self):
        print(f"{self.marka} {self.model} karada durdu.")

    def korna_cal(self):
        print(f"{self.marka} {self.model} kornayı çalıyor! Bip bip!")


class DenizAraci(Arac):
    def __init__(self, marka, model, uzunluk):
        super().__init__(marka, model)
        self.uzunluk = uzunluk  # metre cinsinden

    def hareket_et(self):
        print(f"{self.marka} {self.model} denizde hareket ediyor.")

    def dur(self):
        print(f"{self.marka} {self.model} denizde durdu.")

    def demir_at(self):
        print(f"{self.marka} {self.model} demir attı.")


araba = KaraAraci("Toyota", "Corolla", 4)
araba.hareket_et()
araba.korna_cal()
araba.dur()

tekne = DenizAraci("Yamaha", "WaveRunner", 3.5)
tekne.hareket_et()
tekne.demir_at()
tekne.dur()