
# bir veteriner için OOP temelinde gelen misafirin kayıt edilebildiği 
# en az 2 attr ve 2 methoda sahip bir sınıf oluşturalım.
# Misafirlerden her birine gizli bir ID numarası verelim
# Yazılımcının istediğinde buna erişilebilmesini ve değiştirilebilmesini sağlayalım


import random
misafir_listesi = []
class Misafir:
    def __init__(self):
        self.name = "hayvan"
        self.__id = random.randint(1,1000)
    # @property
    # def isim():
    #     return self.__name 
    @property
    def ID(self):
        return self.__id

    @ID.setter
    def ID(self,ssid):
        self.__id = id
        


for i in range(10):
    misafir_listesi.append(Misafir())

for i in range(len(misafir_listesi)):
    print(misafir_listesi[i].name, misafir_listesi[i].ID)


misafir1 = Misafir()
print(misafir1.ID)
misafir1.ID = 10
print(misafir1.ID)
