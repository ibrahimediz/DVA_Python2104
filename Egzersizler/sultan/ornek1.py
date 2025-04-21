
# bir veteriner için OOP temelinde gelen misafirin kayıt edilebildiği 
# en az 2 attr ve 2 methoda sahip bir sınıf oluşturalım.
# Misafirlerden her birine gizli bir ID numarası verelim
# Yazılımcının istediğinde buna erişilebilmesini ve değiştirilebilmesini sağlayalım


class Veto:
    liste = []
    idList = []
    def __init__ (self, isim,cins, yas):
        self.isim = isim
        self.cins = cins
        self.yas = yas
        Veto.liste.append(isim)
        self.__id = lend (Veto.liste)

    def bilgi (self):
        print(self.isim)

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,param):
        if param in Veto.idList:
            raise ValueError("ID var")
        else:
            Veto.idList.remove(param)
            self.__id = param
            Veto.idList.append(self.__id)

pet1 = Veto("Duman","Kedi",23)
pet1 = Veto("Pamuk","Kedi",23)

pet1.bilgi()
pet2.bilgi()
print(pet1.id) # 1
print(pet2.id) # 2
pet1.id = 2 # HATA VERECEK