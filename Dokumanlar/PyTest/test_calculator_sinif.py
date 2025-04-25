# Test sınıfları ile testleri organize etme

import pytest
from calculator import topla, cikar, carp, bol

# Test sınıfı 'Test' öneki ile başlamalıdır
class TestHesapMakinesi:
    # Sınıf seviyesinde fixture
    @pytest.fixture
    def sayilar(self):
        return {"a": 10, "b": 5}
    
    def test_topla(self, sayilar):
        assert topla(sayilar["a"], sayilar["b"]) == 15
    
    def test_cikar(self, sayilar):
        assert cikar(sayilar["a"], sayilar["b"]) == 5
    
    def test_carp(self, sayilar):
        assert carp(sayilar["a"], sayilar["b"]) == 50
    
    def test_bol(self, sayilar):
        assert bol(sayilar["a"], sayilar["b"]) == 2
    
    # Nested test sınıfı
    class TestOzelDurumlar:
        def test_sifira_bolme(self):
            with pytest.raises(ValueError, match="Sıfıra bölme hatası!"):
                bol(10, 0)
        
        def test_negatif_sayilar(self):
            assert topla(-5, -3) == -8
            assert cikar(-5, -3) == -2