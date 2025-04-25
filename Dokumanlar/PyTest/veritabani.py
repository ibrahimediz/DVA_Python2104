# Veritabanı işlemleri simulasyonu

class Veritabani:
    def __init__(self):
        self.baglanti = False
    
    def baglan(self):
        # Gerçek bir veritabanına bağlanma işlemi
        # Bu örnekte sadece simulasyon yapıyoruz
        print("Veritabanına bağlanılıyor...")
        self.baglanti = True
        return True
    
    def kapat(self):
        # Veritabanı bağlantısını kapatma
        if self.baglanti:
            print("Veritabanı bağlantısı kapattılıyor...")
            self.baglanti = False
            return True
        return False
    
    def kaydet(self, veri):
        # Veriyi veritabanına kaydetme
        if not self.baglanti:
            raise ConnectionError("Veritabanı bağlantısı yok!")
        print(f"{veri} veritabanına kaydediliyor...")
        return True

# Hesap makinesi sonuçlarını veritabanına kaydeden fonksiyon
def islem_kaydet(a, b, islem_turu, sonuc):
    vt = Veritabani()
    vt.baglan()
    veri = {"a": a, "b": b, "islem": islem_turu, "sonuc": sonuc}
    kayit_basarili = vt.kaydet(veri)
    vt.kapat()
    return kayit_basarili