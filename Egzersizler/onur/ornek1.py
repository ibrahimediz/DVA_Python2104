
# bir veteriner için OOP temelinde gelen misafirin kayıt edilebildiği 
# en az 2 attr ve 2 methoda sahip bir sınıf oluşturalım.
# Misafirlerden her birine gizli bir ID numarası verelim
# Yazılımcının istediğinde buna erişilebilmesini ve değiştirilebilmesini sağlayalım

class Animal:
    animal_list = []
    id_list = []
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Animal.animal_list.append(name)
        self.__id = len(Animal.animal_list)
        Animal.id_list.append(self.__id)

    # name property
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @name.getter
    def name(self):
        return self.__name

    # age property
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @age.getter
    def age(self):
        return self.__age


cat = Animal('Cat', 2)
print(cat.name)
cat.name = 'Luna'
print(cat.name)