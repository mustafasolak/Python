"""
sayilar = [45,48,19,63,34,99]
print(sayilar)

# 63'ü ekrana yazın
print(sayilar[3])

# 48'i ekrana yazın
print(sayilar[1])

# 19'u 39 olarak değiştirin
sayilar[2] = 39
print(sayilar)

# 34'ü 64 olarak değiştirin
sayilar[4] = 64
print(sayilar)

# 18'i sayilar listesinin sonuna ekleyin
sayilar.append(18)
print(sayilar)

# 15'i sayilar listesinin 3.sırasına ekleyin
sayilar.insert(3,15)
print(sayilar)

# 48'i sayilar listesinden silin
sayilar.remove(48)
print(sayilar)

# sayilar listesinin son elemanını silin
sayilar.pop()
print(sayilar)

# sayilar listesinin 2.indexinde yer alan elemanı silin
sayilar.pop(2)
print(sayilar)

# sayilar listesini boşaltın, temizleyin
sayilar.clear()
print(sayilar)

# 15 ve 35'i sayilar listesine ekleyin
sayilar.append(15)
sayilar.append(35)
print(sayilar)

# sayilar listesini yok edin
del sayilar
#print(sayilar)

sayilar2 = [ [45, 15], [48, 34, 17], 19, 63, [34, 4, 8, 16, 24], 99 ]
#               0.          1.       2.  3.        4.            5.
#             0.  1.    0.  1.  2.            0.  1. 2.  3. 4.

print(sayilar2)

# 48'i ekrana yazdırın
print( "sayilar2[1][0] :", sayilar2[1][0] )

# 16'yı ekrana yazdırın
print("sayilar2[4][3] :", sayilar2[4][3] )

# 19'u 49 olarak değiştirin
sayilar2[2] = 49
print(sayilar2)

# 24'ü 104 olarak değiştirin
sayilar2[4][4] = 104
print(sayilar2)



urunler = [ ["AR1500","Arduino UNO",10,35], ["MO3215","DC MOTOR 6V", 60, 5], ["IR114", "IR ALICI", 15, 9], ]
print(urunler)
"""





# Ürünlerin tutulduğu liste
#urunler = []
urunler = [
            ["AR1500","ARDUİNO UNO", 10, 35],
            ["ST600","LEHİM TELİ", 50, 7.75],
            ["JK400", "DC MOTOR 6V", 30, 3]
          ]

urun_baslik = ["Stok Kodu","Ürün Adı","Miktar", "Fiyat"]
def menu():
    print("""
            ----------------------
            > DEPO STOK PROGRAMI <
            ----------------------
            ### MENÜ ###
            1- ÜRÜN EKLE
            2- ÜRÜN LİSTELE
            3- ÜRÜN DÜZENLE
            4- ÜRÜN SİL
            5- ÇIKIŞ
    """)

def menu_secim():
    secim = int(input("Yapacağınız işlemi giriniz :"))
    return secim

def urun_ekle():
    # Ürün bilgileri şunlardır : Stok kodu, ürün adı, miktar, fiyat
    stok_kodu = input(urun_baslik[0] + " = ")
    urun_adi = input(urun_baslik[1] + " = ")
    miktar = int(input(urun_baslik[2] + " = "))
    fiyat = float(input(urun_baslik[3] + " = "))
    urun = [stok_kodu, urun_adi, miktar, fiyat]
    urunler.append(urun)
    print("\n   --> Yeni ürün eklendi.\n")
    urun_listele()

def urun_listele():
    print()
    print("-" * 19, "ÜRÜN LİSTESİ", "-"*20)
    print("{:<4}{:<10}{:<15}{:<10}{:<10}(TL)".format(
                            "#",urun_baslik[0],urun_baslik[1],urun_baslik[2], urun_baslik[3])
                                                    )
    print("-" * 53)
    sayac = 1
    for urun in urunler:
        print("{:<4}{:<10}{:<15}{:<10}{:<10}".format(sayac, urun[0], urun[1], urun[2], urun[3]))
        sayac += 1

#Stok koduna göre arama yapar ve geriye ürünün listedeki sırasını döndürür
def urun_ara(stok_kodu):
    for index in range( len(urunler) ):
        if (urunler[index][0] == stok_kodu):
            return index
    return -1

def urun_duzenle(konum):
    stok_kodu = input(urun_baslik[0] + " = ")
    urun_adi = input(urun_baslik[1] + " = ")
    miktar = int(input(urun_baslik[2] + " = "))
    fiyat = float(input(urun_baslik[3] + " = "))
    urun = [stok_kodu, urun_adi, miktar, fiyat]
    urunler[konum] = urun
    print("\n   --> Ürün bilgileri güncellendi.\n")
    urun_listele()

def urun_sil(konum):
    urunler.pop(konum)
    print("\n   --> Ürün silindi.\n")
    urun_listele()

while True:
    menu()
    islem = menu_secim()
    if islem == 1:
        print("Ürün Ekleme İşlemi")
        urun_ekle()
    elif islem == 2:
        #print("Ürün Listeleme İşlemi")
        urun_listele()
    elif islem == 3:
        print("Ürün Düzenleme İşlemi")
        aranan_stok_kodu = input("Aradığınız ürünün stok kodunu giriniz : ")
        konum = urun_ara(aranan_stok_kodu)
        if (konum != -1):
            urun_duzenle(konum)
        else:
            print("Aranan stok koduna ait ürün bulunamadı..")

    elif islem ==  4:
        print("Ürün Silme İşlemi")
        aranan_stok_kodu = input("Aradığınız ürünün stok kodunu giriniz : ")
        konum = urun_ara(aranan_stok_kodu)
        if (konum != -1):
            urun_sil(konum)
        else:
            print("Aranan stok koduna ait ürün bulunamadı..")
    elif islem == 5:
        print("Programdan çıkılıyor..")
        break
    else:
        print("Lütfen 1-5 arası değer giriniz")