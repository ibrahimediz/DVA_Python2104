import os
import csv
from pathlib import Path


print(pathlib.posixpath.abspath("."))

with open('nisa.csv', 'a+') as dosya:
    dosya.write("Nisa")