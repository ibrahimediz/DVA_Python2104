# bir veteriner için OOP temelinde gelen misafirin kayıt edilebildiği 
# en az 2 attr ve 2 methoda sahip bir sınıf oluşturalım.
# Misafirlerden her birine gizli bir ID numarası verelim
# Yazılımcının istediğinde buna erişilebilmesini ve değiştirilebilmesini sağlayalım

class Sinif:
    liste = []
    idList = []
    def __init__(self,isim,cins,yas):
        self.isim = isim
        self.cins = cins
        self.yas = yas
        Sinif.liste.append(isim)
        self.__id = len(Sinif.liste)
        Sinif.idList.append(self.id)

    def bilgi(self):
        print(self.isim)

    @property
    def id(self):
        return self.__id,

    @id.setter
    def id(self,param):
        if param in Sinif.idList:
            raise ValueError("ID var")
        else:
            Sinif.idList.remove(param)
            self.__id = param
            Sinif.idList.append(self.__id)

pet1 = Sinif("Bulut","Kedi",2)
pet2 = Sinif("Karabaş","Köpek",6)
#pet1.bilgi
#pet2.bilgi
print(pet1.id)
print(pet2.id)
