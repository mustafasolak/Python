"""
    15-06-2021 14:00 - Mustafa SOLAK
    İTÜ MTAL Hazırlık B - SÖZLÜKLER(DICTIONARIES)
"""

# Boş bir sözlük oluşturma
ogrenciler = {}   # Alt Gr + 7 = {     Alt Gr + 0 = }
print(ogrenciler)

# İçinde veri olan bir sözlük oluşturalım
ogrenciler = {
    'adi' : "Mustafa",
    "soyadi" : "SOLAK",
    "sinif" : "9/A",
    "numara":170,
    # "sinif" : "9/B"  # pyton does not allow duplicate keys
}
print(ogrenciler)

# -------------------  Sözlük elemanlarına ulaşma
# Kullanımı : sozlukAdi[anahtar_adi]
# Örnek : adi anahtarının değerini ekrana yazdırın
print("-"*30)
print("Sözlük elemanlarına ulaşma\n")
print(ogrenciler["adi"])
print(ogrenciler["soyadi"])
print(ogrenciler["sinif"])
print(ogrenciler["numara"])

#print( ogrenciler["ismi"] ) # KeyError meydana gelir eğer aranan anahtar değeri sözlükte yok ise

# -------------------  get() metodu ile sözlük elemanlarına erişme
# Kullanımı : sozlukAdi.get(anahtar_adi,  None)
# Syntax : sozlukAdi.get(keyname, value)
# keyname	Required. The keyname of the item you want to return the value from
# value	Optional. A value to return if the specified key does not exist.
# Default value None

print( ogrenciler.get("ismi") )
print( ogrenciler.get("ismi", "Aranan anahtar sözlükte yok !") )


# Sözlüğün eleman sayısını bulma
# len() fonksiyonu
# Kullanımı : len(sozlukAdi)
print("-"*30)
print("Sözlüğün eleman sayısını bulma\n")
print( "Sözlüğün içindeki eleman sayısı :",len(ogrenciler) )


# Sözlük içinde farklı veri tipleri kullanılabilir
print("-"*30)
print("Sözlük içinde farklı veri tipleri kullanılabilir\n")

print("-"*10)
print("Sözlük içinde sözlük kullanımı\n")

urunler = {
    "MS4534" : {
        "urun_adi" : "Arduino UNO",
        "miktar":15,
        "fiyat" : 37.5
    },
    "KE1105" : {
        "urun_adi" : "Raspberry PI 4",
        "miktar" : 3,
        "fiyat" : 485
    }
}
print(urunler)
# MS4534 stok koduna sahip anahtarın değerini yazdıralım
print( urunler["MS4534"] )

# KE1105 stok koduna sahip anahtarın değerini yazdıralım
print( urunler["KE1105"] )

# MS4534 stok koduna sahip ürünün adını yazdırın
print( urunler["MS4534"]["urun_adi"] )

# KE1105 stok koduna sahip ürünün fiyatını yazdırın
print( urunler["KE1105"]["fiyat"] )

print("-"*10)
print("Sözlük içinde liste kullanımı\n")

# ------------------- sözlük içinde liste kullanımı
ogrenciler = {
    101 : [ "Burak BERBER", "Bay", 15 ],
    105 : ["Emir TUNAHAN ALİM", "Bay", 16],
    85  : ["Firdevs HANDAN AŞIK", "Bayan", 17 ]
}
print(ogrenciler)

# 101 numaralı öğrencinin adını yazdırın
print( ogrenciler[101][0] )

# 105 numaralı öğrencinin cinsiyetini yazdırın
print( ogrenciler[105][1] )

# ------------------- Sözlüğe eleman ekleme
# Kullanımı : sozlukAdi[anahtar_adi] = degeri
print("-"*30)
print("Sözlüğe eleman ekleme\n")


kelimeler = {}
print("kelimeler sözlüğü :", kelimeler)

# Örnek : kelimeler sözlüğüne car : araba değerini ekleyin
kelimeler["car"] = "araba"
print("kelimeler sözlüğü :", kelimeler)

# Örnek : kelimeler sözlüğüne window : pencere değerini ekleyin
kelimeler["window"] = "pencere"
print("kelimeler sözlüğü :", kelimeler)

kelimeler["computer"] = "bilgisayar"
kelimeler["line"] = "sınır, çizgi"
kelimeler["turtle"] = "kaplumbağa"
kelimeler["daisy"] = "papatya"
print("kelimeler sözlüğü :", kelimeler)


# ------------------- Sözlük elemanları üzerinde değişiklik yapma
# Kullanımı : sozluk_adi[anahtar_adi] = yeni_deger
print("-"*30)
print("Sözlük elemanları üzerinde değişiklik yapma\n")

# Örnek : car anahtarının değerini taşıt olarak değiştirin
kelimeler["car"] = "taşıt"
print("kelimeler sözlüğü :", kelimeler)

# SÖZLÜKLERİN FONKSİYONLARI
# keys() fonksiyonu -> Sözlüğün anahtarlarını getirir
# Kullanımı : sozlukAdi.keys()
print("-"*30)
print("keys() fonksiyonu\n")
print( kelimeler.keys() )

# values() fonksiyonu -> Sözlüğün değerlerini getirir
# Kullanımı : sozlukAdi.values()
print("-"*30)
print("values() fonksiyonu\n")
print( kelimeler.values() )

# items() fonksiyonu -> Sözlüğün anahtar ve değerlerini verir
# Kullanımı : sozlukAdi.items()
print("-"*30)
print("items() fonksiyonu\n")
print( kelimeler.items() )

# Sözlükte elemanın olup olmadığını kontrol etme
# Kullanımı :
# if anahtar_adi in sozlukAdi:
#   print("evet sözlükte mevcut")
# else:
#   print("anahtar sözlükte yok !")
print("-"*30)
print("Sözlükte elemanın olup olmadığını kontrol etme, if .. in \n")

if "window" in kelimeler:
    print("Anahtar, sözlükte mevcut")
else:
    print("Anahtar yok !")

if "kapı" in kelimeler:
    print("Anahtar, sözlükte mevcut")
else:
    print("kapı anahtarı sözlükte  yok !")


# copy() fonksiyonu -> Bir sözlüğü başka bir sözlüğe kopyalar
print("-"*30)
print("copy() fonksiyonu\n")
kelimeler_yeni = kelimeler.copy()
print("kelimeler sözlüğü :", kelimeler)
print("kelimeler_yeni sözlüğü :", kelimeler_yeni)

# pop() fonksiyonu -> Sözlükten belirtilen anahtar değerine sahip olan anahtar değer çiftini çıkarır
# Kullanımı :  sozlukAdi.pop(anahtar_adi, varsayilanDeger)

print("-"*30)
print("pop() fonksiyonu\n")
# Örnek : kelimeler_yeni sözlüğünden line anahtarını ve değerini çıkarın
print("önce kelimeler_yeni sözlüğü :", kelimeler_yeni)
deger = kelimeler_yeni.pop("line")
print(deger, " kelimesi silindi")
print("sonra kelimeler_yeni sözlüğü :", kelimeler_yeni)

# Örnek : kelimeler_yeni sözlüğünden fire anahtarını silin
#kelimeler_yeni.pop("fire")
print( kelimeler_yeni.pop("fire", "Aranan anahtar sözlükte yok !") )


# popitem() fonksiyonu -> Sözlüğe en son eklenen anahtar değer çiftini sözlükten çıkartır
# Kullanımı : sozlukAdi.popitem()
print("-"*30)
print("popitem() fonksiyonu\n")
ogrenciler = {"adi" : "Mustafa"}
ogrenciler["soyadi"] = "SOLAK"
ogrenciler["sinif"] = "9/A"
print(ogrenciler)


cikarilan_eleman = ogrenciler.popitem()
print("Sözlükten çıkarılan anahtar değer çifti :", cikarilan_eleman)
print("ogrenciler.popitem() ->", ogrenciler)

cikarilan_eleman = ogrenciler.popitem()
print("\nSözlükten çıkarılan anahtar değer çifti :", cikarilan_eleman)
print("ogrenciler.popitem() ->", ogrenciler)

# update() fonksiyonu -> Sözlüğe eleman ekler
# Kullanımı : sozlukAdi.update( { anahtar_adi : deger } )
print("-"*30)
print("update() fonksiyonu\n")

# Örnek : kelimeler sözlüğüne update fonksiyonu ile
# mouse : fare anahtar değer çiftini ekleyin
print("kelimeler sözlüğü :", kelimeler)
kelimeler.update( { "mouse" : "fare" } )  # kelimeler["mouse"] = "fare"
print("kelimeler sözlüğü :", kelimeler)

#--------------------------
# Az sonra clear() fonksiyonunu kullanacağımız için kelimeler listesini
# başka bir listeye kopyalayacağım
yedek_kelimeler = kelimeler.copy()
#--------------------------

# clear() fonksiyonu -> Sözlüğün içindeki tüm elemanları siler,
# sözlüğü boşaltır.
# Kullanımı : sozlukAdi.clear()
print("-"*30)
print("clear() fonksiyonu\n")

# Örnek : kelimeler sözlüğünün içindeki herşeyi siliniz
kelimeler.clear()
print("kelimeler sözlüğü :", kelimeler)

#--------------------------
# Yukarıda clear() fonksiyonunu kullandığımız için kelimeler listesini
# boşalttık ve yedek_kelimeler listesinden bir kopya oluşturup
# kelimeler listesine atalım
kelimeler = yedek_kelimeler.copy()
#--------------------------

# SÖZLÜĞÜN İÇİNDEKİ ELEMANLARI YAZDIRMA
print("-"*30)
print("SÖZLÜĞÜN İÇİNDEKİ ELEMANLARI YAZDIRMA\n")
for anahtar in kelimeler:
    print("{:>15} > {:<15}".format(anahtar, kelimeler[anahtar]))

print("-"*10)
sayilar = {
    "sıfır" : 0,
    "bir" : 1,
    "iki" : 2,
    "üç" : 3,
    "dört" : 4,
    "beş" : 5,
    "altı" : 6,
    "yedi" : 7,
    "sekiz" : 8,
    "dokuz" : 9
}

print( sayilar["altı"] )
print( sayilar["yedi"] )
print( sayilar["sekiz"] )
print("-"*10)
for anahtar in sayilar :
    print("{:>15} > {:<15}".format(anahtar, sayilar[anahtar]))

print("-"*10)
for deger in sayilar.values():
    print(deger)
print("-"*10)
for deger in kelimeler.values():
    print(deger)
print("-"*10)
for anahtar in kelimeler.keys():
    print(anahtar)
print("-"*10)

print("kelimeler :", kelimeler)
print("kelimeler.items() :", kelimeler.items())
for anahtar,deger in kelimeler.items():
    print("Anahtar :{}, değeri :{}".format(anahtar, deger))