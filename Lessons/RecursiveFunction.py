# Recursive = Rekürsif Fonksiyon
# Belirli şartlar dahilinde kendi kendini çağıran fonksiyondur.
# Fonksiyonun bitişi için bir sınır belirlemek gereklidir. Yoksa sonsuza kadar çalışır.

# Rekürsif olarak faktöriyel hesabı yapan fonksiyon
def faktoriyelR(gelenSayi):
    if gelenSayi < 1:
        return 1
    return gelenSayi * faktoriyelR(gelenSayi-1)

sonuc = faktoriyelR(4)
print(sonuc)
print("-"*30)

# 1'den 10'a kadar olan sayıların toplamını rekürsif olarak bulan program
def toplaR(sayi):
    if sayi < 1:
        return 0
    return sayi + toplaR(sayi-1)
print(toplaR(5))
print("-"*30)

# 1'den 10'a kadar olan sayıların toplamını bulan program
def topla(sayi):
    toplam = 0
    for sayi in range(1,sayi+1):
        toplam += sayi
    return toplam
print(topla(5))
print("-"*30)

# 1'den 10'a kadar sayıları ekrana yazan program
# for sayi in range(1,11):
#     print(sayi)

# Gelen sayıdan 1'e kadar ekrana yazdırır.
def yazdirRAsagi(sayi):
    if sayi < 1:
        return 0
    print(sayi)
    yazdirRAsagi(sayi-1)

yazdirRAsagi(5)
print("-"*30)

# 1'den gelen sayıya kadar ekrana yazdırır.
def yazdirRYukari(sayi):
    if sayi < 1:
        return 0
    print(sayi)
    yazdirRYukari(sayi-1)

yazdirRYukari(5)
print("-"*30)