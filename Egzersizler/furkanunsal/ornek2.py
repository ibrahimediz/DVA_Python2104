 
# ekrana yansıtılan diagram dosyasında yer alan 
# sınıf isimlerini kullanarak hiyerarşiyi oluşturalım


class Araclar:
    def __init__(self, marka, model, yakit_turu):
        self.marka = marka
        self.model = model
        self.yakit_turu = yakit_turu

    def bilgi_ver(self):
        return f"Marka: {self.marka}, Model: {self.model}, Yakıt Türü: {self.yakit_turu}"







