
"""
sayilar = [1, 3, 5, 7]
#          0. 1. 2. 3.
print(sayilar)
print(sayilar[3])

sayilar = [ [15, 35, 10], [45, 56], [38, 3, 27, 47] ]
#               0.         1.         2.
#            0.  1.  2.    0.  1.    0.  1. 2.  3.

print(sayilar)
print("sayilar[0] :",sayilar[0])
print("sayilar[1] :",sayilar[1])
print("sayilar[2] :",sayilar[2])

# 35'i ekrana yazın
print("sayilar[0][1] :",sayilar[0][1])

# 10'u ekrana yazın
print("sayilar[0][2] :",sayilar[0][2])

#56'yı ekrana yazın
print("sayilar[1][1] :",sayilar[1][1])

#47'yi ekrana yazdır
print("sayilar[2][3] :",sayilar[2][3])

# 45'i 68 ile değiştirin
sayilar[1][0] = 68
print("sayilar[1][0] = 68 işleminden sonra sayilar listesi")
print(sayilar)


urunler = [ ["Elma", 10, 7.75], ["Armut",40,3], ["Muz",80,13] ]
#                  0.                  1.             2.
#             0.     1.  2.       0.     1. 2.    0.   1.  2.
print(urunler)

urun = ["Portakal", 15, 6]
urunler.append(urun)
print(urunler)

for sayac in range(len(urunler)):
   if urunler[sayac][0] == "Muz":
       print("Buldum,konum :", sayac)
"""












# Ürünleri tutacak olan listeyi tanımladık
urunler = []

def menu():
    print("""
        ----------------------
        > ÜRÜN TAKİP SİSTEMİ <
        ----------------------
        ### MENÜ ###
        1- ÜRÜN EKLE
        2- ÜRÜN LİSTELE
        3- ÜRÜN DÜZENLE
        4- ÜRÜN SİL
        5- ÇIKIŞ
    """)

def menu_secim():
    secim = int(input("Yapacağınız işlemin numarasını giriniz :"))
    return secim

def urun_ekle():
    # ürün adı, miktarı, fiyatı bilgilerini alalım
    urun_adi = input("Ürün adı = ")
    miktar = int(input("Miktar = "))
    fiyat = float(input("Fiyat = "))
    urun = [urun_adi, miktar, fiyat]
    urunler.append(urun)
    #print(urunler)

def urun_listele():
    print("-" * 35)
    print("{:<4}{:<15}{:<10}{:<10}".format("#", "Ürün Adı","Miktar", "Fiyat"))
    print("-"*35)
    sayac =1
    for urun in urunler:
        print("{:<4}{:<15}{:<10}{:<10}".format(sayac,urun[0], urun[1], urun[2]))
        sayac += 1

# eğer ürün listede bulunursa konumu
# bulunamazsa -1 gelecek
def urun_ara(gelenUrunAdi):
    for sayac in range(len(urunler)):
        if urunler[sayac][0] == gelenUrunAdi:
            return sayac
    return -1

def urun_duzenle(urun_konumu):
    # ürün adı, miktarı, fiyatı bilgilerini alalım
    urun_adi = input("Ürün adı = ")
    miktar = int(input("Miktar = "))
    fiyat = float(input("Fiyat = "))
    urun = [urun_adi, miktar, fiyat]
    urunler[urun_konumu] = urun
    print("Ürün bilgileri düzenlendi.")

while True:
    menu()
    islem = menu_secim()
    if islem == 1:
        print("Ürün Ekleme İşlemi")
        urun_ekle()
    elif islem == 2:
        print("Ürün Listeleme İşlemi")
        urun_listele()
    elif islem == 3:
        print("Ürün Düzenleme İşlemi")
        aranan = input("Aradığınız ürünün adı = ")
        konum = urun_ara(aranan)
        if konum != -1:
            print("Ürün bulundu")
            urun_duzenle(konum)
        else:
            print("Ürün bulunamadı.")

    elif islem == 4:
        print("Ürün Silme İşlemi")
    elif islem == 5:
        print("Programdan çıkılıyor..")
        break







