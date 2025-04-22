import os
import csv
import pathlib


print(pathlib.posixpath.abspath("."))

with open('nisa.csv', 'a+') as dosya:
    dosya.write("Nisa")