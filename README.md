# İleri Python Programlama - Hafta 5 Lab: Dekoratörler

Bu proje, İleri Python Programlama dersi 5. hafta laboratuvar ödevini içermektedir. Mevcut metin tabanlı uzay oyunu projesine, Python'ın güçlü özelliklerinden olan **dekoratörler (decorators)** kullanılarak yeni yetenekler eklenmiştir.

## Proje İçeriği ve Görevler

Bu ödev kapsamında aşağıdaki dekoratörler geliştirilmiştir:

### Özel Dekoratörler (`uzay_oyunu/dekoratorler.py`)

Oyun içindeki fonksiyonların davranışlarını değiştirmeden onlara ekstra özellikler katan dekoratörler yazılmıştır:

* **`@sure_olc`**: Uygulandığı fonksiyonun ne kadar sürede çalıştığını (`time.perf_counter()` ile) ölçer ve ekrana yazdırır.

* **`@say`**: Bir fonksiyonun kaç kez çağrıldığını sayar. Özellikle özyinelemeli (recursive) fonksiyonların (örn. Fibonacci) çalışma mantığını ve önbellekleme (`lru_cache`) ile olan ilişkisini analiz etmek için kullanılmıştır. (Detaylı analiz `dekorator_sirasi.md` dosyasındadır).

* **`@log_cagri`**: Fonksiyon çağrılarını (aldığı konumsal ve adlı argümanlarla birlikte) ve fonksiyonun dönüş değerini loglar.

* **`@sinirla(alt, ust)`**: Argüman alan bir dekoratördür. Fonksiyona gönderilen ilk değerin belirtilen `[alt, ust]` aralığında olup olmadığını denetler, dışındaysa `ValueError` fırlatır (Örn: Yakıt harcama kontrolü).

* **`@hafiza(maxsize)` (Bonus)**: `functools.lru_cache` modülüne alternatif olarak, closure (kapanış) mantığıyla çalışan özel bir önbellekleme (caching) dekoratörüdür.
