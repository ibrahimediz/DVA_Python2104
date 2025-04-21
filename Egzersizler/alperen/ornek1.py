
# bir veteriner için OOP temelinde gelen misafirin kayıt edilebildiği 
# en az 2 attr ve 2 methoda sahip bir sınıf oluşturalım.
# Misafirlerden her birine gizli bir ID numarası verelim
# Yazılımcının istediğinde buna erişilebilmesini ve değiştirilebilmesini sağlayalım

a = 1

class VetClass:
    instances = []
    def __init__(self,name:str,surname:str,number):
        global a
        self.id = a
        self.name = name
        self.surname = surname
        self.number = number
        a = a+1
        VetClass.instances.append(self)

    @classmethod
    def GetNumberWithId(cls,id):
        for instance in cls.instances:
            if instance.id == id:
                print("id=",instance.id,"\nnumber:",instance.number)
                return

    @classmethod
    def GetAllDataFromId(cls,id):
        for instance in cls.instances:
            if instance.id == id:
                print("id=",instance.id,"\nnumber:",instance.number,
                "Name:",instance.name,"Surname:",instance.surname)
                return

user1 = VetClass("alp","akr","5555555555");
VetClass.GetNumberWithId(1)
VetClass.GetAllDataFromId(1)