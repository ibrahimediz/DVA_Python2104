# with open("Dokumanlar/FileOperations/ornek.csv","r+") as d1,\
#     open("Dokumanlar/FileOperations/ornek2.csv","r+") as d2:
    
# import os
# import shutil
# from pathlib import Path
# BASE_DIR = Path(__file__).resolve().parent.parent.parent / 'Egzersizler'
# liste = ['Ibrahim', 'mss', 'eren', 'nisa', 'ilker',
#  'onur', 'ahmet', 'sultan', 'sefa', 'Sena', 'baris',
#   'efe', 'furkanunsal', 'furkan_topaloglu', 'alperen', 'Gkhan',"ogun"]
# for item in liste:
#     if not os.path.exists(BASE_DIR / item):
#       os.mkdir(BASE_DIR / item)
#     shutil.copy("/workspace/DVA_Python2104/Dokumanlar/FileOperations/ornek.csv",BASE_DIR / item)
