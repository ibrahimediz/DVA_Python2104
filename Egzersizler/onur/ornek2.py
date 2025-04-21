
# ekrana yansıtılan diagram dosyasında yer alan 
# sınıf isimlerini kullanarak hiyerarşiyi oluşturalım

class Arac:
    def __init__(self):
        self.gas = 0
    
    def add_gas(self, gas_amount):
        self.gas += gas_amount
    
    def run(self):
        print('Araç hareket etti')

class KaraAraclari(Arac):
    def __init__(self):
        super().__init__()

class DenizAraclari(Arac):
    def __init__(self):
        super().__init__()

class Araba(KaraAraclari):
    def __init__(self, marka):
        super().__init__()
        self.marka = marka

araba = Araba('Citroen')
araba.add_gas(5)
print(araba.gas)
print(araba.marka)
araba.run()