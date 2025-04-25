# Mock ve monkeypatch örnekleri

import pytest
from unittest.mock import MagicMock, patch
from hesap_islemleri import topla_ve_kaydet, cikar_ve_kaydet
from veritabani import Veritabani, islem_kaydet

# unittest.mock ile mock kullanma
def test_islem_kaydet_mock():
    # islem_kaydet fonksiyonunu mock ile değiştiriyoruz
    with patch('hesap_islemleri.islem_kaydet') as mock_kaydet:
        # Mock'un dönü5 değerini ayarlama
        mock_kaydet.return_value = True
        
        # Fonksiyonu çağırma
        sonuc = topla_ve_kaydet(5, 3)
        
        # Beklenen sonucu kontrol etme
        assert sonuc == 8
        
        # Mock fonksiyonun çağrıldığını kontrol etme
        mock_kaydet.assert_called_once()
        
        # Mock fonksiyonun doğru parametrelerle çağrıldığını kontrol etme
        mock_kaydet.assert_called_once_with(5, 3, "toplama", 8)

# pytest.monkeypatch kullanma
def test_islem_kaydet_monkeypatch(monkeypatch):
    # Çağrılan fonksiyonu takip etmek için mock
    kayit_verileri = []
    
    # Mock fonksiyon
    def mock_islem_kaydet(a, b, islem_turu, sonuc):
        kayit_verileri.append({"a": a, "b": b, "islem": islem_turu, "sonuc": sonuc})
        return True
    
    # Orijinal fonksiyonu geçici olarak değiştirme
    monkeypatch.setattr('hesap_islemleri.islem_kaydet', mock_islem_kaydet)
    
    # Test edilen fonksiyonu çağırma
    sonuc = cikar_ve_kaydet(10, 4)
    
    # Sonucu kontrol etme
    assert sonuc == 6
    assert len(kayit_verileri) == 1
    assert kayit_verileri[0] == {"a": 10, "b": 4, "islem": "cikarma", "sonuc": 6}

# Veritabani sınıfını mock'lama
class TestVeritabaniMock:
    def test_veritabani_baglanti(self, monkeypatch):
        # Veritabani sınıfının baglan metodunu mock'lama
        mock_baglan = MagicMock(return_value=True)
        monkeypatch.setattr(Veritabani, 'baglan', mock_baglan)
        
        # Veritabani sınıfının kaydet metodunu mock'lama
        mock_kaydet = MagicMock(return_value=True)
        monkeypatch.setattr(Veritabani, 'kaydet', mock_kaydet)
        
        # Veritabani sınıfının kapat metodunu mock'lama
        mock_kapat = MagicMock(return_value=True)
        monkeypatch.setattr(Veritabani, 'kapat', mock_kapat)
        
        # islem_kaydet fonksiyonunu çağırma
        sonuc = islem_kaydet(5, 3, "toplama", 8)
        
        # Beklenen sonucu kontrol etme
        assert sonuc is True
        
        # Mock metodların çağrıldığını kontrol etme
        mock_baglan.assert_called_once()
        mock_kaydet.assert_called_once()
        mock_kapat.assert_called_once()