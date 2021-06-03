"""
renkler = []
renkler = list()

sayilar = [45, 48, 19, 63, 34, 99]
#          0.  1.  2.  3.  4.  5.
print(sayilar)

# 63'ü ekrana yazın
print(sayilar[3])

# 48'i ekrana yazın
print(sayilar[1])

# 19'u 39 olarak değiştirin
sayilar[2] = 39
print(sayilar)

# 63'ü 73 olarak değiştirin
sayilar[3] = 73
print(sayilar)

# 34'ü 64 olarak değiştirin
sayilar[4] = 64
print(sayilar)

# 18'i sayilar listesinin sonuna ekleyin
sayilar.append(18)
print(sayilar)

# 87'yi sayilar listesinin sonuna ekleyin
sayilar.append(87)
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


sayilar1 = [45,48,19,63,34,99]

#sayilar2 = [ [45, 15], [48,34,17], 19, 63, [34, 4, 8, 16, 24], 99 ]
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


urunler = [ ["E12", "Elma", 10, 6.5], ["A45","Armut", 20, 7.75] ]
print(urunler)


urunler = [
            ["AR1500","Arduino UNO",10,35],  #0. index
            ["MO3215","DC MOTOR 6V", 60, 5], #1. index
            ["IR114", "IR ALICI", 15, 9],    #2. index
          ]

print(urunler)

print(urunler[1][1])
"""






urunler = [
            ["AR1500","ARDUİNO UNO", 10, 35],
            ["ST600","LEHİM TELİ", 50, 7.75],
            ["JK400", "DC MOTOR 6V", 30, 3],
          ]

urun_baslik = ["Stok Kodu","Ürün Adı","Miktar", "Fiyat"]

def menu():
    print("""
               **********************
               > DEPO STOK PROGRAMI <
               **********************
               ### MENÜ ###
               1- ÜRÜN EKLE
               2- ÜRÜN LİSTELE
               3- ÜRÜN DÜZENLE
               4- ÜRÜN SİL
               5- ÇIKIŞ
       """)

def menu_secim():
    secim = int(input("Yapacağınız işlem numarasını giriniz : "))
    return secim

def urun_ekle():
    # Ürün bilgileri şunlardır : Stok kodu, ürün adı, miktar, fiyat
    stok_kodu = input(urun_baslik[0] + " = ")
    urun_adi = input(urun_baslik[1] + " = ")
    miktar = int(input(urun_baslik[2] + " = "))
    fiyat = float(input(urun_baslik[3] + " = "))

    urun = [ stok_kodu, urun_adi, miktar, fiyat ]
    urunler.append(urun)
    print("\n  > Ürün eklendi. \n")


def urun_listele():
    print("-" * 49)
    print("{:<4}{:<10}{:>15}{:>10}{:>10}".format("#", urun_baslik[0], urun_baslik[1], urun_baslik[2], urun_baslik[3] ))
    print("-"*49)
    sayac = 1
    for urun in urunler:
        print("{:<4}{:<10}{:>15}{:>10}{:>10}".format(sayac, urun[0], urun[1], urun[2], urun[3] ))
        sayac += 1

def urun_ara(gelenStokKodu):
    for sayac in range( len(urunler) ):
        if urunler[sayac][0] == gelenStokKodu:
            return sayac
    return -1 # demek ki ürün bulunamadı

def urun_duzenle(urun_konumu):
    stok_kodu = input(urun_baslik[0] + " = ")
    urun_adi = input(urun_baslik[1] + " = ")
    miktar = int(input(urun_baslik[2] + " = "))
    fiyat = float(input(urun_baslik[3] + " = "))

    urun = [stok_kodu, urun_adi, miktar, fiyat]

    urunler[urun_konumu] = urun

    print("\n   --> Ürün bilgileri güncellendi.\n")

def urun_sil(urun_konumu):
    urunler.pop(urun_konumu)
    print("\n   --> Ürün silindi.\n")

while True:
    urun_listele()
    menu()
    islem = menu_secim()
    if islem == 1:
        print("\nÜrün Ekleme İşlemi\n", "-"*30)
        urun_ekle()
    elif islem == 2:
        print("\nÜrün Listeleme İşlemi\n")
        urun_listele()
    elif islem == 3:
        print("\nÜrün Düzenleme İşlemi\n", "-"*30)

        arananStokKodu = input("Aradığınız ürüne ait stok kodunu giriniz  = ")
        konum = urun_ara(arananStokKodu)
        if konum != -1:
            print("\nÜrün bulundu, yeni ürün bilgilerini giriniz...\n")
            urun_duzenle(konum)
        else:
            print("Düzenlemek istedğiniz ürün bulunamadı..")
    elif islem == 4:
        print("\nÜrün Silme İşlemi\n", "-"*30)
        arananStokKodu = input("Aradığınız ürüne ait stok kodunu giriniz  = ")
        konum = urun_ara(arananStokKodu)
        if konum != -1:
           urun_sil(konum)
        else:
            print("Silmek istediğiniz ürün bulunamadı..")
    elif islem == 5:
        print("\nProgramdan çıkılıyor..\n", "-"*30)
        break
    else:
        print("\n1-5 arasında bir sayı giriniz..\n")









