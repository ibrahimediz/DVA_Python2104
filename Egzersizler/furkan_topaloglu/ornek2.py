
# ekrana yansıtılan diagram dosyasında yer alan 
# sınıf isimlerini kullanarak hiyerarşiyi oluşturalım


class Araclar:
    def __init__(self, ad, tip, yakit):
        self.ad = ad
        self.tip = tip
        self.yakit = yakit

    def arac_adi(self):
        print("Araç Adı:", self.ad)

    def arac_tipi(self):
        print("Araç Tipi:", self.tip)
    
    def yakit_turu(self):
        print("Yakıt Türü:", self.yakit)


class Kara_Araclari(Araclar):
    def __init__(self, ad, tip, yakit, teker_sayisi):
        super().__init__(ad, tip, yakit)
        self.teker_sayisi = teker_sayisi

    def teker_sayisi_goster(self):
        print("Tekerlek Sayısı:", self.teker_sayisi)



class Deniz_Araclari(Araclar):
    def __init__(self, ad, tip, yakit, guverte_uzunlugu):
        super().__init__(ad, tip, yakit)
        self.guverte_uzunlugu = guverte_uzunlugu

    def guverte_uzunlugu_goster(self):
        print("Güverte Uzunluğu:", self.guverte_uzunlugu)


def araclari_listele(arac_listesi):
    for arac in arac_listesi:
        arac.arac_adi()
        arac.arac_tipi()
        arac.yakit_turu()
        
        if isinstance(arac, Kara_Araclari):
            arac.teker_sayisi_goster()
        elif isinstance(arac, Deniz_Araclari):
            arac.guverte_uzunlugu_goster()

araba = Kara_Araclari("Toyota Corolla", "Otomobil", "Benzin", 4)
motosiklet = Kara_Araclari("Yamaha R25", "Motosiklet", "Benzin", 2)

tekne = Deniz_Araclari("Sea Ray", "Tekne", "Dizel", 12.5)
yat = Deniz_Araclari("Azimut Grande", "Yat", "Benzin", 25.0)


tum_araclar = [araba, motosiklet, tekne, yat]

araclari_listele(tum_araclar)