import functools
import time

def sure_olc(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        baslangic = time.perf_counter()
        sonuc = func(*args, **kwargs)
        bitis = time.perf_counter()
        print(f"{func.__name__}: {bitis - baslangic:.4f} sn")
        return sonuc
    return wrapper

def say(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.cagri += 1
        return func(*args, **kwargs)
    wrapper.cagri = 0
    return wrapper

def log_cagri(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ", ".join(repr(a) for a in args)
        kwargs_str = ", ".join(f"{k}={repr(v)}" for k, v in kwargs.items())
        all_args = ", ".join(filter(None, [args_str, kwargs_str]))
        print(f"-> {func.__name__}({all_args})")
        sonuc = func(*args, **kwargs)
        print(f"<<- {func.__name__} {repr(sonuc)}")
        return sonuc
    return wrapper

def sinirla(alt, ust):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if args:
                deger = args[0]
                if not (alt <= deger <= ust):
                    raise ValueError(f"{func.__name__}: {deger} değeri {alt}-{ust} aralığında değil")
            return func(*args, **kwargs)
        return wrapper
    return decorator

def hafiza(maxsize=None):
    def decorator(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
            if args in cache:
                return cache[args]
            sonuc = func(*args)
            if maxsize is not None and len(cache) >= maxsize:
                ilk_anahtar = next(iter(cache))
                del cache[ilk_anahtar]
            cache[args] = sonuc
            return sonuc
        return wrapper
    return decorator
