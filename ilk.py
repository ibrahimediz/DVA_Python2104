import os
liste = ['Ibrahim', 'mss', 'eren', 'nisa', 'ilker',
 'onur', 'ahmet', 'sultan', 'sefa', 'Sena', 'baris',
  'efe', 'furkanunsal', 'furkan_topaloglu', 'alperen', 'Gkhan',"ogun"]
dosyaismi = "ornek2.py"
sorumex"tni = """
# ekrana yansıtılan diagram dosyasında yer alan 
# sınıf isimlerini kullanarak hiyerarşiyi oluşturalım
"""
for item in liste:
    if not os.path.exists(f"Egzersizler/{item}"):
      os.mkdir(f"Egzersizler/{item}")
    with open(f"Egzersizler/{item}/{dosyaismi}","a+") as dosya:
      dosya.write(sorumetni)


