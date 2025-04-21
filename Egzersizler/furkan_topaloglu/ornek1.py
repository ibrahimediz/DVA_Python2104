
# bir veteriner için OOP temelinde gelen misafirin kayıt edilebildiği 
# en az 2 attr ve 2 methoda sahip bir sınıf oluşturalım.
# Misafirlerden her birine gizli bir ID numarası verelim
# Yazılımcının istediğinde buna erişilebilmesini ve değiştirilebilmesini sağlayalım



class Veto:
    liste = []
    idList = []
    def __init__(self,*args,**kwargs):
        self.isim = args[0]
        for key,value in kwargs.items():
            if key == "cins":
                self.cins = value 
            if key == "yas":
                self.yas = value 
        Veto.liste.append(self.isim)
        self.__id = len(Veto.liste)
        Veto.idList.append(self.__id)

    def bilgi(self):
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

pet1 = Veto("Duman",cins="Kedi",yas=23)
pet2 = Veto("Pamuk",cins="Kedi",yas=20)

pet1.bilgi()
pet2.bilgi()
print(pet1.id) # 1
print(pet2.id) # 2
pet1.id = 2 # HATA VERECEK
