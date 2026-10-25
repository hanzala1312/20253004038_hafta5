# Fibonacci Çağrı Sayıları ve Nedenleri

1. **Yalnızca `@say` (21891 çağrı):**
Fibonacci fonksiyonu her özyinelemeli adımda iki kez kendini çağırır ve bu çağrıların hiçbir sonucu önbelleğe alınmadığı için toplam hesaplama ağacındaki tüm düğümler sayılır.

2. **`@say` üstte, `@lru_cache` altta (39 çağrı):**
`lru_cache`, `say` dekoratörünün sardığı fonksiyonun üzerinde çalışır. Fonksiyon her çağrıldığında önce sayılır, sonra önbelleğe gidilir. Önbellekte olmayan (hesaplanan) değerler ve önbellekten dönen değerler için wrapper tetiklendiğinden sadece gerekli ardışık çağrılar ve cache isabetleri sayılır.

3. **`@lru_cache` üstte, `@say` altta (21 çağrı):**
En dışta `lru_cache` olduğu için aynı argümanla yapılan bir çağrı önbellekte varsa, fonksiyon (`say` dekoratörüne) hiç gitmeden sonuç döndürülür. Böylece sayaç yalnızca önbellekte olmayan ve gerçekten hesaplama yapılan eşsiz `fib(n)` çağrıları için artar (0'dan 20'ye kadar toplam 21 çağrı).
