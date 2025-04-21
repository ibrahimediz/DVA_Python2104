
# bir veteriner için OOP temelinde gelen misafirin kayıt edilebildiği 
# en az 2 attr ve 2 methoda sahip bir sınıf oluşturalım.
# Misafirlerden her birine gizli bir ID numarası verelim
# Yazılımcının istediğinde buna erişilebilmesini ve değiştirilebilmesini sağlayalım
"""
class VET():
    def __init__(self):
        self.__clients = {}
    
    def addClient(self, fullName, *args):
        self.__clients.pop(fullName)
        self.__clients[fullName] = { id: uuid.uuid4(), args: args }
    
    def getClient(self, fullName):
        return self.__clients[fullName]

    def removeClient(self, fullName):
        del sef.__clients[fullName]
"""
class Client:
    def __init__(self, id, name, surname):
        self.__id, self.__name, self.__surname = id, name, surname
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def setId(self, value):
        self.__id = value

c = Client("123","Name", "Surname")
print(c.id)