# conftest.py'daki fixture'ları kullanma

import pytest
from calculator import topla, cikar, carp, bol

# conftest.py'daki fixture'ları kullanma
def test_temel_islemler(temel_sayilar):
    a = temel_sayilar["a"]  # 10
    b = temel_sayilar["b"]  # 5
    
    assert topla(a, b) == 15
    assert cikar(a, b) == 5
    assert carp(a, b) == 50
    assert bol(a, b) == 2

def test_buyuk_sayilarla_islemler(buyuk_sayilar):
    a = buyuk_sayilar["a"]  # 1000
    b = buyuk_sayilar["b"]  # 500
    
    assert topla(a, b) == 1500
    assert cikar(a, b) == 500

# Parametrize edilmiş fixture kullanma
def test_parametrize_fixture_toplama(sayi_cifti):
    a, b = sayi_cifti
    assert topla(a, b) == a + b

# Birden fazla fixture kullanma
def test_coklu_fixture(temel_sayilar, negatif_sayilar):
    assert topla(temel_sayilar["a"], negatif_sayilar["a"]) == 0  # 10 + (-10) = 0
    assert carp(temel_sayilar["b"], negatif_sayilar["b"]) == -25  # 5 * (-5) = -25