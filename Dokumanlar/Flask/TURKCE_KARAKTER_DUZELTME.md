# Türkçe Karakter Düzeltme

Bu projede oluşturulan dosyalarda Türkçe karakterlerde kodlama sorunu bulunmaktadır. Bu sorunu çözmek için aşağıdaki adımları izleyebilirsiniz:

## Yöntem 1: Python Script Kullanma

Proje klasöründe bulunan `fix_encoding.py` dosyasını çalıştırarak tüm dosyalardaki Türkçe karakter sorunlarını otomatik olarak düzeltebilirsiniz:

```bash
python fix_encoding.py
```

Bu script, projedeki tüm `.py`, `.md` ve `.ini` dosyalarını tarayacak ve Unicode escape dizilerini (u00f6 gibi) doğru Türkçe karakterlere (ö gibi) dönüştürecektir.

## Yöntem 2: Manuel Düzeltme

Eğer script çalışmazsa, dosyaları manuel olarak düzeltebilirsiniz. Bunun için:

1. Dosyayı bir metin editöründe açın
2. Aşağıdaki değişimleri yapın:
   - `u00e7` → `ç` (ç)
   - `u00f6` → `ö` (ö)
   - `u00fc` → `ü` (ü)
   - `u011f` → `ğ` (ğ)
   - `u0131` → `ı` (ı)
   - `u015f` → `ş` (ş)
   - `u00c7` → `Ç` (Ç)
   - `u00d6` → `Ö` (Ö)
   - `u00dc` → `Ü` (Ü)
   - `u011e` → `Ğ` (Ğ)
   - `u0130` → `İ` (İ)
   - `u015e` → `Ş` (Ş)

Bu değişiklikleri yaptıktan sonra, dosyaları UTF-8 kodlamasıyla kaydedin.