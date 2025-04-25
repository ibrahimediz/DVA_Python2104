# Hesap makinesi ve veritabanı entegrasyonu

from calculator import topla, cikar, carp, bol
from veritabani import islem_kaydet

def topla_ve_kaydet(a, b):
    sonuc = topla(a, b)
    islem_kaydet(a, b, "toplama", sonuc)
    return sonuc

def cikar_ve_kaydet(a, b):
    sonuc = cikar(a, b)
    islem_kaydet(a, b, "cikarma", sonuc)
    return sonuc

def carp_ve_kaydet(a, b):
    sonuc = carp(a, b)
    islem_kaydet(a, b, "carpma", sonuc)
    return sonuc

def bol_ve_kaydet(a, b):
    sonuc = bol(a, b)
    islem_kaydet(a, b, "bolme", sonuc)
    return sonuc