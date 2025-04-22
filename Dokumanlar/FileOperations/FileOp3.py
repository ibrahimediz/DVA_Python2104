import json

dosya = json.load(open("Dokumanlar/FileOperations/ornek.json"))
sozluk = dosya[0]
print(sozluk["name"])
json.dump()