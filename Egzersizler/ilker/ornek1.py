
# bir veteriner için OOP temelinde gelen misafirin kayıt edilebildiği 
# en az 2 attr ve 2 methoda sahip bir sınıf oluşturalım.
# Misafirlerden her birine gizli bir ID numarası verelim
# Yazılımcının istediğinde buna erişilebilmesini ve değiştirilebilmesini sağlayalım


class Vet:
    liste = []
    idList = []
    def __init__(self, isim, cins, yas):
        self.isim= isim
        self.cins= cins
        self.yas = yas
        Vet.liste.append(isim)
        self.__id = len(Vet.liste)
        Vet.idList.append(self.__id)

    def bilgi(self):
        print(self.isim)
    

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self,param):
        if param in Vet.idList:
            raise ValueError("ID var")
        else:
            Vet.idList.remove(param)
            self.__id = param
            Veto.idList.append(self.__id)


pet1 = Vet("Duman1","Kedi1",23)
pet2 = Vet("Duman2","Kedi2",24)


pet1.bilgi()
pet2.bilgi()
print(pet1.id) # 1
print(pet2.id) # 2
pet1.id = 2 # HATA VERECEK