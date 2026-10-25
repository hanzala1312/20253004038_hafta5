KOMUTLAR = {}

def komut(ad, aciklama=""):
    def decorator(func):
        if ad in KOMUTLAR:
            raise ValueError(f"'{ad}' adında bir komut zaten kayıtlı.")
        KOMUTLAR[ad] = (func, aciklama)
        return func
    return decorator

@komut("yardim", "komutları listeler")
def yardim(durum):
    for k_ad, (_, k_aciklama) in KOMUTLAR.items():
        print(f"{k_ad}\n{k_aciklama}")

@komut("envanter", "envanter eşyalarını gösterir")
def envanter(durum):
    print(", ".join(durum.get("envanter", [])))

@komut("harita", "gidebileceğin gezegenleri gösterir")
def harita(durum):
    print(", ".join(durum.get("baglantilar", [])))
