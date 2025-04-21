
# bir veteriner için OOP temelinde gelen misafirin kayıt edilebildiği 
# en az 2 attr ve 2 methoda sahip bir sınıf oluşturalım.
# Misafirlerden her birine gizli bir ID numarası verelim
# Yazılımcının istediğinde buna erişilebilmesini ve değiştirilebilmesini sağlayalım
import random

class Guest:
    def __init__(self, name, animal_type):
        self.name = name  # Misafirin ismi
        self.animal_type = animal_type  # Hayvanın türü
        self._id = random.randint(1000, 9999)  # Gizli ID numarası

    @property
    def id(self):
        # Gizli ID'ye sadece okuma erişimi sağlar
        return self._id

    @id.setter
    def id(self, new_id):
        # ID'nin değiştirilebilmesi için setter metodu
        self._id = new_id

    def register(self):
        """Misafiri sisteme kaydeder"""
        print(f"{self.name} ({self.animal_type}) kaydedildi. ID: {self._id}")

    def update_info(self, new_name, new_animal_type):
        """Misafirin bilgilerini günceller"""
        self.name = new_name
        self.animal_type = new_animal_type
        print(f"Bilgiler güncellendi: {self.name} - {self.animal_type}")


guest_1 = Guest("Köpek", "Golden Retriever")
guest_1.register()

# ID'yi değiştirelim
guest_1.id = 5678
print(f"Misafirin yeni ID'si: {guest_1.id}")

# Misafirin bilgilerini güncelleyelim
guest_1.update_info("Kedim", "British Shorthair")
