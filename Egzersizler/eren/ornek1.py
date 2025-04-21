
# bir veteriner için OOP temelinde gelen misafirin kayıt edilebildiği 
# en az 2 attr ve 2 methoda sahip bir sınıf oluşturalım.
# Misafirlerden her birine gizli bir ID numarası verelim
# Yazılımcının istediğinde buna erişilebilmesini ve değiştirilebilmesini sağlayalım

class Customer:
    liste = []
    idList = []
    def __init__(self,isim,cins,yas):
        self.isim = isim
        self.cins = cins
        self.yas = yas
        Customer.liste.append(isim)
        self.__id = len(Customer.liste)
        Customer.idList.append(self.__id)

    def bilgi(self):
        print(self.isim)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self,id):
        if id in Customer.idList:
            raise ValueError("ID var")
        else:
            Customer.idList.remove(id)
            self.__id = id
            Customer.idList.append(self.__id)


pet1 = Customer("Duman","Kedi",23)
pet2 = Customer("Pamuk","Kedi",20)

pet1.bilgi()
pet2.bilgi()
print(pet1.id) # 1
print(pet2.id) # 2
pet1.id = 2 # HATA VERECEK