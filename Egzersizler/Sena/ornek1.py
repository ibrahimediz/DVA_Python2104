
# bir veteriner için OOP temelinde gelen misafirin kayıt edilebildiği 
# en az 2 attr ve 2 methoda sahip bir sınıf oluşturalım.
# Misafirlerden her birine gizli bir ID numarası verelim
# Yazılımcının istediğinde buna erişilebilmesini ve değiştirilebilmesini sağlayalım
class Misafir:
    liste = []
    idList=[]
    def __init__(self,ad,soyad):
        self.adi=ad
        self.soyadi=soyad
        Misafir.liste.append(ad)
        self.__ID=len(Misafir.liste)
        Misafir.idList.append(self.__ID)
    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self,param):
        if param in Misafir.idList:
            raise ValueError("ID var")
        else:
            Misafir.idList.remove(param)
            self.__ID=param
            Misafir.idList.append(self.__ID)
    def misafir_info(self):
        print(self.adi,self.soyadi)
    

obj=Misafir("s","n")
#obj.ID=1
obj.misafir_info()