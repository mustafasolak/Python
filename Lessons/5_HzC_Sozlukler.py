
"""
# Boş bir sözlük oluşturma
ogrenciler = {}
print(ogrenciler)

# İçerisinde veri olan sözlük oluşturalım
ogrenciler = { "adi" : "Mustafa", "soyadi" : "SOLAK", "sinif" : "9/A" }
print(ogrenciler)

# Eleman sayısını bulma  len() fonksiyonu ile
print(len(ogrenciler))

# Sözlüğün elemanlarına erişmek
#Örneğin adi anahtarinin değerini yazdiralim
print( ogrenciler["adi"] )

#Örneğin soyadi anahtarinin değerini yazdiralim
print( ogrenciler["soyadi"] )

#Örneğin sinif anahtarinin değerini yazdiralim
print( ogrenciler["sinif"] )

# Değer olarak farklı veri tipleri kullanma
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

print(sayilar["yedi"])

# Sözlük içerisinde farklı türde veri tipleri kullanılabilir

ogrenciler = {
    154 : ["Osman Ahmet ALTINORDU", "Hazırlık C", "15"],
    109 : ["Eren Muhammed TURHAN" , "Hazırlık C", "16"],
    118 : ["Emre AĞRI", "Hazırlık C", "17"]
}

# Örnek : 154 numaralı öğrencinin bilgilerini getirin
bilgi = ogrenciler[154]
print(bilgi)
print( bilgi[0] )
print( bilgi[1] )
print( bilgi[2] )

# Sözlük içinde sözlük kullanımı
urunler = {
    "MS4534" : {
        "urun_adi" : "Arduino UNO",
        "miktar"   : 15,
        "fiyat"    : 45.50,
    } ,
    "HŞ3334" : {
        "urun_adi" : "Raspberry PI 4 Model B",
        "miktar"   : 3,
        "fiyat"    : 500
    }
}
print(urunler)

print( urunler["HŞ3334"]["urun_adi"])


stok_kodu = input("Ürün stok kodu = ")
urun = urunler[stok_kodu]
print(urun)

# Aranan ürünün bilgileri ayrı ayrı yazdırın
print("Ürün adı : {}".format( urun["urun_adi"] ))
print("Miktarı  : {}".format( urun["miktar"] ))
print("Fiyatı   : {}".format( urun["fiyat"] ))
"""

# Sözlüğe eleman ekleme
kelimeler = {}
print(kelimeler)

kelimeler["car"] = "araba"
print(kelimeler)

kelimeler["book"] = "kitap"
print(kelimeler)

print(kelimeler["book"])
print(kelimeler["car"])

kelimeler["computer"] = "bilgisayar"
kelimeler["line"] = "sınır, çizgi"
kelimeler["turtle"] = "kaplumbağa"
kelimeler["daisy"] = "papatya"
print(kelimeler)

# Sözlük elemanları üzerinde değişiklik yapma
# Kullanımı : sozluk_adi[anahtar_adi] = yeni_deger
# Örnek : car anahtarının değerini taşıt olarak değiştirin

kelimeler["car"] = "taşıt"
print(kelimeler)


# !!! Dikkat: Sözlükte aynı anahtar ismine sahip başka bir anahtar OLAMAZ
kelimeler["book"] = "kamil"
print(kelimeler)

kelimeler["travel"] = "seyahat"
print(kelimeler)
kelimeler["travel"] = "gezi"
print(kelimeler)

# SÖZLÜKLERİN FONKSİYONLARI
# keys() fonksiyonu -> Sözlüğün anahtarlarını getirir
print( kelimeler.keys() )

# values() fonksiyonu -> Sözlüğün değerlerini getirir
print( kelimeler.values() )

# items metodu -> Sözlüğün anahtar ve değerlerini verir
print( kelimeler.items() )

# get() metodu kullanımı    dictionary.get(keyname, value)
# keyname	Required. The keyname of the item you want to return the value from
# value	Optional. A value to return if the specified key does not exist.
# Default value None
#print( kelimeler["printer"])

print(  kelimeler.get("printer") )
print(  kelimeler.get("printer", "Aranan değer bulunamadı !") )

# clear() metodu
print(kelimeler)
kelimeler.clear()
print(kelimeler)

# copy() fonksiyonu
ogrenciler1 = { "adi" : "Mustafa", "soyadi" : "SOLAK", "sinif" : "9/A" }
print(ogrenciler1)

ogrenciler2 = ogrenciler1.copy()
print(ogrenciler2)

deger = ogrenciler1.pop("adi")
print(deger, " sözlükten silindi.")
print(ogrenciler1)
print("-"*30)
print(ogrenciler1)
print(ogrenciler2)
print( ogrenciler1.pop("ccc","Aranan eleman yok") )


bilgiler = {
    170 : "Mustafa"
}
print(bilgiler)

bilgiler[181] = "Okhan BAŞTAN"
bilgiler[169] = "Yakup Yasin YILMAZ"
print(bilgiler)

print( bilgiler.popitem() )
print(bilgiler)

print( bilgiler.popitem() )
print(bilgiler)

bilgiler.update({171 : "Zafer İNAN"})
#bilgiler[171] = "Zafer İNAN"
print(bilgiler)