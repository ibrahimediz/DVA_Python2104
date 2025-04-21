class Misafir:
    def __init__(self, isim, hayvan_türü):
        self.isim = isim
        self.hayvan_türü = hayvan_türü
        self.__id = self.__id_olustur()  # Gizli (private) ID

    def bilgileri_goster(self):
        print(f"İsim: {self.isim}, Tür: {self.hayvan_türü}")

    def ses_cikar(self):
        if self.hayvan_türü.lower() == "kedi":
            print("Miyav")
        elif self.hayvan_türü.lower() == "köpek":
            print("Hav hav")
        else:
            print("Hayvan sesi bilinmiyor.")

    # Private metot: ID üretimi
    def __id_olustur(self):
        import random
        return f"ID-{random.randint(1000, 9999)}"

    # Getter (ID'yi öğrenmek için)
    def get_id(self):
        return self.__id

    # Setter (ID'yi değiştirmek için)
    def set_id(self, yeni_id):
        if isinstance(yeni_id, str) and yeni_id.startswith("ID-"):
            self.__id = yeni_id
        else:
            print("Geçersiz ID formatı. 'ID-' ile başlamalı.")

# Örnek kullanım:
misafir1 = Misafir("Pamuk", "Kedi")
misafir2 = Misafir("Karabas", "Köpek")

misafir1.bilgileri_goster()
misafir1.ses_cikar()

print("Gizli ID:", misafir1.get_id())  # ID'ye erişim
misafir1.set_id("ID-1234")            # ID'yi değiştirme
print("Yeni ID:", misafir1.get_id())
