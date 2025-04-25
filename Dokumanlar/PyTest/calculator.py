# Basit hesap makinesi fonksiyonları

def topla(a, b):
    """İki sayıyı toplar"""
    return a + b

def cikar(a, b):
    """İlk sayıdan ikinci sayıyı çıkarır"""
    return a - b

def carp(a, b):
    """İki sayıyı çarpar"""
    return a * b

def bol(a, b):
    """İlk sayıyı ikinci sayıya böler"""
    if b == 0:
        raise ValueError("Sıfıra bölme hatası!")
    return a / b