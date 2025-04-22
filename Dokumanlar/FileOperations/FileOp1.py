# os , pathlib
from pathlib import Path
import random
import datetime
from string import ascii_letters,punctuation,digits
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent / 'Egzersizler'

print(BASE_DIR)

# relative path 
# ---- Dokumanlar/FileOperations/FileOp1.py
# abs path
# ---- /workspace/DVA_Python2104/Dokumanlar/FileOperations/FileOp1.py

## open
# r+
# a+
# w+
# x+

dosya = open(r"Dokumanlar/FileOperations/ornek.csv","w+")
for i in range(100):
    liste = []
    kayit = [random.choice(random.choice([ascii_letters,punctuation,digits])) for i in range(20)]
    kayit = "".join(kayit)
    liste.append(kayit)
    liste.append(random.randint(1,100000))
    liste.append(datetime.datetime.now().year)
    liste.append(datetime.datetime.now().month)
    liste = map(str,liste)
    print(";".join(liste),file=dosya)
# dosya.seek(0)
# print(r"C:\talat\nalan\biricik.html")