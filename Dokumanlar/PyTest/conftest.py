# conftest.py - Paylaşılan fixture'lar için

import pytest
from calculator import topla, cikar, carp, bol

# Tüm testlerde kullanılabilecek fixture'lar
@pytest.fixture
def temel_sayilar():
    return {"a": 10, "b": 5}

@pytest.fixture
def buyuk_sayilar():
    return {"a": 1000, "b": 500}

@pytest.fixture
def negatif_sayilar():
    return {"a": -10, "b": -5}

# Otomatik olarak her testten önce çalışan setup fixture
@pytest.fixture(autouse=True)
def setup_teardown():
    # Setup - test öncesi çalışır
    print("\nTest başlıyor...")
    
    # Testin çalışmasına izin ver
    yield
    
    # Teardown - test sonrası çalışır
    print("Test tamamlandı.")

# Parametrize edilmiş fixture
@pytest.fixture(params=[(3, 5), (10, 2), (-3, -2)])
def sayi_cifti(request):
    return request.param
