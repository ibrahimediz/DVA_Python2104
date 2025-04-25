# Pytest Öğretici

Bu proje, pytest kütüphanesini aşama aşama öğrenmek için örnek kodlar içerir.

## Öğrenme Adımları

### 1. Temel Pytest Kullanımı
- `test_calculator_basit.py` - Basit test fonksiyonları ve assert kullanımı

### 2. Gelişmiş Özellikler
- `test_calculator_gelismis.py` - Parametrize, fixture ve marker kullanımı

### 3. Test Sınıfları
- `test_calculator_sinif.py` - Test sınıfları ile testleri organize etme

### 4. Mock ve Monkeypatch
- `test_mock_monkeypatch.py` - Dış bağımlılıkları mock'lama

### 5. Paylaşılan Fixture'lar
- `conftest.py` - Paylaşılan fixture'ları tanımlama
- `test_conftest_kullanimi.py` - Paylaşılan fixture'ları kullanma

## Testleri Çalıştırma

Tüm testleri çalıştırmak için:
```
pytest
```

Belirli bir test dosyasını çalıştırmak için:
```
pytest test_calculator_basit.py
```

Belirli bir test fonksiyonunu çalıştırmak için:
```
pytest test_calculator_basit.py::test_topla
```

Belirli bir marker ile işaretlenmiş testleri çalıştırmak için:
```
pytest -m yavaş
```

Belirli bir marker ile işaretlenmiş testleri hariç tutmak için:
```
pytest -m "not yavaş"
```

## Pytest Komut Satırı Seçenekleri

- `-v` veya `--verbose`: Ayrıntılı çıktı gösterir
- `-s`: print ifadelerinin çıktısını gösterir
- `-k "ifade"`: Belirli bir ifadeyi içeren testleri çalıştırır
- `--collect-only`: Testleri çalıştırmadan sadece toplar ve gösterir
- `--cov=paket_adi`: Test kapsamı raporlaması yapar (pytest-cov eklentisi gerektirir)