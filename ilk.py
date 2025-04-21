import os
liste = ['Ibrahim', 'mss', 'eren', 'nisa', 'ilker',
 'onur', 'ahmet', 'sultan', 'sefa', 'Sena', 'baris',
  'efe', 'furkanunsal', 'furkan_topaloglu', 'alperen', 'Gkhan',"ogun"]
dosyaismi = "ornek1.py"
sorumetni = """
# bir veteriner için OOP temelinde gelen misafirin kayıt edilebildiği 
# en az 2 attr ve 2 methoda sahip bir sınıf oluşturalım.
# Misafirlerden her birine gizli bir ID numarası verelim
# Yazılımcının istediğinde buna erişilebilmesini ve değiştirilebilmesini sağlayalım
"""
for item in liste:
    if not os.path.exists(f"Egzersizler/{item}"):
      os.mkdir(f"Egzersizler/{item}")
    with open(f"Egzersizler/{item}/{dosyaismi}","a+") as dosya:
      dosya.write(sorumetni)


