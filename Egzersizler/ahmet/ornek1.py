
# bir veteriner için OOP temelinde gelen misafirin kayıt edilebildiği 
# en az 2 attr ve 2 methoda sahip bir sınıf oluşturalım.
# Misafirlerden her birine gizli bir ID numarası verelim
# Yazılımcının istediğinde buna erişilebilmesini ve değiştirilebilmesini sağlayalım
class veteriner:
    def __init__(self,isim):
        self.__isim=isim
        self.__id=id
        
    def kayit(self,cls):
        list=[]
        input("Müşteri İsmi:",self.__isim)
    def get_isim(self):
        return self.__isim

    def set_isim(self, yeni_isim):
        self.__isim= yeni_isim
isim=input("Müşteri ismi girin:")
v1=veteriner(isim)
v1.kayit()                   
      

     
     
