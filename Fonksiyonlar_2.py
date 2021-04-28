# MUSTAFA SOLAK / 28-04-2021
# FONKSİYONLAR
# ÖNCE FONKSİYON TANIMLANIR ARDINDAN FONKSİYON ÇAĞIRILIR.


def ogrenciler(**isimler):
    print(isimler)

ogrenciler(isim1="Ali",isim2="Veli",isim3="Talat",isim4="Fitnat", sayi=12)


# parametrenin başına * koymak istediğimiz kadar isimsiz değer
# gönderebilmemizi sağlar
def yazBakalim(*sayilar, isim="Kamil"):
    print("Gelen isim : {}".format(isim))
    print(sayilar)

yazBakalim("ali","veli",1,2,True,3,4,5,6,7,8,9,isim="Ali")
yazBakalim("ali","veli",1,2,True,3,4,5,6,7,8,9)



"""
# Varsayılan parametre kullanımı
# Örnek : Kullanıcıdan alınan başlangıç, bitiş ve miktar
# değerlerine göre ekrana çıktı veren program.

def yazdir(baslangic, bitis, miktar=1 ):
    while bitis >= baslangic:
        print(baslangic)
        baslangic += miktar

#yazdir(1,10,3)
yazdir(0,15)


# bas = int(input("Başlangıç = "))
# son = int(input("Bitiş = "))
# adet = int(input("Artış miktarı = "))
#
# yazdir(bas, son, adet)


def ogrenci_kaydet(isim, numara, yas, sehir):
    print("İsim   :", isim)
    print("Numara :", numara)
    print("Yaş    :", yas)
    print("Şehir  :", sehir)
    print( "." * 30 )
#Eğer isimsiz parametre kullanımı var ise;
#  fonksiyon tanımında kaç tane parametre var ise, o kadar
#  değer göndermek zorundayız

#İSİMSİZ parametre kullanımı
ogrenci_kaydet("Mustafa SOLAK",45, 25, "İstanbul")

#İSİMLİ parametre kullanımı
ogrenci_kaydet(isim="Ahmet KURAL", numara=88, yas=40, sehir="İzmir")
#isimli parametre kullanımında sıra önemsizdir.
ogrenci_kaydet(sehir="Şanlıurfa", isim="Ömer", yas=28, numara=47)


# built-in dahili, yerleşik bir fonksiyon
print("Ali","Kerem","Hakan","Bülent" , sep="-")
print("Öğrenciler")
print("1-Kaan", end=",")
print("2-Mustafa")
print("3-Oğuz")
"""