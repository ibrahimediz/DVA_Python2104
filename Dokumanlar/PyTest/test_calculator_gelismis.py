# Pytest'in gelişmiş özellikleri

import pytest
from calculator import topla, cikar, carp, bol

# Parametrize kullanarak birden fazla test senaryosu
@pytest.mark.parametrize("a, b, beklenen", [
    (3, 5, 8),      # Pozitif sayılar
    (-1, 1, 0),     # Bir negatif, bir pozitif
    (-1, -1, -2),   # İki negatif sayı
    (0, 0, 0)       # Sıfırlar
])
def test_topla_parametrize(a, b, beklenen):
    assert topla(a, b) == beklenen

# Hata testleri için
def test_bol_sifira_bolme_hatasi():
    # ValueError beklendiğini belirtiyoruz
    with pytest.raises(ValueError):
        bol(10, 0)

# Fixture kullanımı - test öncesi hazırlık için
@pytest.fixture
def ornek_sayilar():
    return {"a": 10, "b": 5}

def test_tum_islemler_fixture(ornek_sayilar):
    a = ornek_sayilar["a"]
    b = ornek_sayilar["b"]
    
    assert topla(a, b) == 15
    assert cikar(a, b) == 5
    assert carp(a, b) == 50
    assert bol(a, b) == 2

# Belirli testleri işaretleme
@pytest.mark.yavaş
def test_buyuk_sayilar_carpimi():
    # Bu test yavaş olarak işaretlendi
    assert carp(1000, 1000) == 1000000