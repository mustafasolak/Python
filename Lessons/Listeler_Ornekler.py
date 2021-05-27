urunler = []
#urunler = list()
def menu():
    print("""
    --- MENÜ ---
    1-ÜRÜN EKLE
    2-ÜRÜN LİSTELE
    3-ÜRÜN DÜZENLE
    4-ÜRÜN SİL
    5-ÇIKIŞ
    """)

def islemSectir():
    secim = int(input("Yapmak istediğiniz işlem numarasını giriniz : "))
    return secim

def urunGirisi():
    print("ÜRÜN EKLEME İŞLEMİ")
    adi = input("Ürün adı = ")
    miktar = int(input("Miktar = "))
    fiyat = int(input("Fiyat = "))
    urun = [adi, miktar, fiyat]
    urunler.append(urun)
    print("\nÜrün eklendi.")

def urunListele():
    print("\nÜrünler Listesi")
    print("-" * 15)
    for urun in urunler:
        print("Ürün Adı :", urun[0])
        print("Miktarı :", urun[1])
        print("Fiyatı :", urun[2])
        print("-"*15)


while True:
    menu()
    islem = islemSectir()
    if islem == 1:
        urunGirisi()
    elif islem == 2:
        urunListele()
    elif islem == 5:
        print("Programdan çıkılıyor")
        break




# sayilar = [1,2,3,[14,65]]
# print(sayilar)
# print(sayilar[0])
# print(sayilar[1])
# print(sayilar[2])
# print(sayilar[3])
# print( sayilar[3][0] )
# print( sayilar[3][1] )

#
# isimler = [ ["ali","veli"], ["Hasan","Ahmet","Nuri"] , ["Kamil"] ]
#               #     0                 1                     2
#               # 0       1         0       1      2          0
# # Hasan ismini ekrana yazdırın
# print( isimler[1][0]  )
#
# # Kamil
# print( isimler[2][0] )
#
# sayilar = [ [ [15, 65], 18 ], 27 ]
#                 #  0            1
#                 # 0        1
#                 # 0   1
#
# # 65'i ekrana yazın
# print(sayilar[0][0][1])
# #18
# print(sayilar[0][1])
#
