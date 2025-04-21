
# bir veteriner için OOP temelinde gelen misafirin kayıt edilebildiği 
# en az 2 attr ve 2 methoda sahip bir sınıf oluşturalım.
# Misafirlerden her birine gizli bir ID numarası verelim
# Yazılımcının istediğinde buna erişilebilmesini ve değiştirilebilmesini sağlayalım

class Hayvan:
    def __init__(self, isim, tur, yas):
        self.isim = isim
        self.tur = tur
        self.yas = yas

    def __str__(self):
        return f"Hayvan İsmi: {self.isim}, Tür: {self.tur}, Yaş: {self.yas}"


class Sahip:
    def __init__(self, ad, telefon):
        self.ad = ad
        self.telefon = telefon
        self.hayvanlar = []

    def hayvan_ekle(self, hayvan):
        self.hayvanlar.append(hayvan)

    def __str__(self):
        hayvan_listesi = "\n  ".join(str(h) for h in self.hayvanlar)
        return f"Sahip: {self.ad}, Telefon: {self.telefon}\n  {hayvan_listesi}"


class Veteriner:
    def __init__(self, isim):
        self.isim = isim
        self.misafirler = []

    def misafir_ekle(self, sahip):
        self.misafirler.append(sahip)

    def misafir_listesi(self):
        print(f"Veteriner {self.isim} için misafir listesi:")
        for idx, sahip in enumerate(self.misafirler, 1):
            print(f"\nMisafir #{idx}:\n{str(sahip)}")
       