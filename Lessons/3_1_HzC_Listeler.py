"""
# Örneğin sınıfınızda 25 öğrenci var ve her  bir öğrencinin isimlerini tutacaksınız.

# Boş bir liste aşağıdaki 2 yolla tanımlanabilir.
isimler = []
print(isimler)
isimler = list()
print(isimler)

#Listeye veri eklemek
isimler.append("Ali")
print(isimler)

isimler.append("Veli")
print(isimler)

isimler.append("Hasan")
isimler.append("Muhsin")
isimler.append("Mualla")
print(isimler)

# Listenin elemanlarına ulaşmak
# listeadi[eleman_sira_numarasi]
# isimler listesinin 2 sıra numarasına sahip elemanı yazdıralım
print( isimler[2] )

# Mualla değerini ekrana yazdıralım
print( "isimler[4] :", isimler[4] )
print( "isimler[-1] :",isimler[-1] )

# Ali ismine tersten ulaşalım
print("isimler[-5]) :", isimler[-5])


# Başlangıç değeri olan liste tanımlama
renkler = ["Kırmızı","Mavi","Sarı","Yeşil"]
print(renkler)
renkler.append("Bordo")
print(renkler)


ogrenciler = ["Ali", "Ahmet", "Hasan"]
print(ogrenciler)

# Listeyi ekrana yazdırma
# for eleman in  liste_adi :
for ogrenci in ogrenciler:
    print(ogrenci)

sayilar = [45, 48, 19, 33, 63, 34]
for x in sayilar:
    print(x)

numbers = [ 1, 2, 3, 4, 5 ]
for eleman in numbers:
    print( eleman * eleman)

meyveler = ["elma", "armut", "elma", "üzüm","karpuz", "kavun","muz"]
for meyve in meyveler:
    print(meyve)

# Listenin belirli bir aralığını seçmek
# Seçilen aralık yeni bir liste meydana getirir.
# liste_adi[baslangicSiraNo:bitisSiraNo]
print(meyveler[0:3])
print(meyveler[2:5])

# bitiş indexini vermezsek verilen başlangıç indexinden listenin sonuna kadar olan tüm elemanları seçer
print( meyveler[3:] )
print( meyveler[1:] )

# başlangıç indexini vermezsek varsayılan olarak listenin başından başlar
print( meyveler[:3] )
print( meyveler[:5])

liste = meyveler[0:4]
for meyve in liste:
    print(meyve)

#Listenin elemanını değiştirmek
# Kullanımı: listeAdi[elemanSiraNo] = yeni_deger
cicekler = ["Gül", "Papatya", "Sardunya", "Orkide", "Kasımpatı", "Hanımeli"]
print(cicekler)

cicekler[2] = "Zakkum"
print(cicekler)

cicekler[4] = "Küpeli"
print(cicekler)

cicekler[-1] = "Kedi Tırnağı"
print(cicekler)



#Listenin içindeki belirli bir aralığı değiştirme
arabalar = ["Polo", "Golf", "Passat", "BMW" , "Audi", "Serçe"]
print(arabalar)
# BMW ve Audi markalarını, Clio ve Jeep ile değiştirelim
arabalar[3:5] = [ "Clio", "Jeep"]
print(arabalar)
arabalar[3:5] = [ "Laguna", "Q7", "Bora", "Anadol"]
print(arabalar)
arabalar[3:5] = [ "Amarok"]
print(arabalar)

# listede belirli bir sıraya eleman eklemek
ulkeler = ["Ergenekon", "Türkiye", "Libya", "Arnavutluk"]
print(ulkeler)

ulkeler.insert(2, "Almanya")
print(ulkeler)

ulkeler.insert(4,"Bosna Hersek")
print(ulkeler)

# extend metodu ile iki liste birleştirilebilir
sayilar1 = [1,2,3,4]
sayilar2 = [5,6,7,8]
sayilar1.extend(sayilar2)
print(sayilar1)

# listeden eleman silme
# Kullanımı : listeAdi.remove(elemanAdi)
donanim =["Klavye", "Fare", "Monitör", "İşlemci", "RAM", "SSD",14]
print(donanim)

donanim.remove("Fare")
print(donanim)

donanim.remove("SSD")
print(donanim)

donanim.remove(14)
print(donanim)

# pop() fonksiyonu
# parametre olarak bir değer verilmez ise en sondaki elemanı siler
donanim =["Klavye", "Fare", "Monitör", "İşlemci", "RAM", "SSD",14]
print(donanim)

donanim.pop()
print(donanim)

donanim.pop()
print(donanim)

donanim.pop()
print(donanim)

# parametre verilirse o sıradaki elemanı siler
donanim.pop(2)
print(donanim)

donanim.pop(0)
print(donanim)

donanim.pop(-2)
print(donanim)

# del ile donanim listesini sildik, yok artık bu liste.
del donanim
#print("Donanım listesi :",donanim)

# listeyi temizleme
bocekler = ["Hamam böceği", "Salyangoz", "Kara Fatma","Geyik Böceği"]
print(bocekler)

bocekler.clear()
print(bocekler)



eski_yerlesimler = ["Göbeklitepe","Piramitler", "Stonehenge", "Mayalar", "Aztekler" , "İnkalar", "Machu Pichu"]
for yer in eski_yerlesimler :
    print(yer)


print("Listenin uzunluğu :", len(eski_yerlesimler) )
for index in range( len(eski_yerlesimler) ):
    print( eski_yerlesimler[index] )

aranan = input("ne aradınız  = ")
if aranan in eski_yerlesimler:
    print("Evet var")
else:w
    print("yok")

# 8.	LİSTENİN ELEMANLARINI YAZDIRMA
# a.	for in döngüsü ile listenin elemanlarını yazdırma
# Kullanımı :
# for degiskenAdi in listeAdi:
#    print(degiskenAdi)

print("-"*10, "LİSTENİN ELEMANLARINI YAZDIRMA")
sayilar = [1,3,15,0,6]

# Örnek: sayilar listesinin elemanlarını for .. in döngüsü ile ekrana yazdırın
print("\n--> sayilar listesi for in döngüsü ile >>>>>")
for sayi in sayilar:
    print(sayi)

isimler = ["ali", "veli" , "hasan","nuri"]
# Örnek: isimler listesinin elemanlarını for .. in döngüsü ile ekrana yazdırın
print("\n--> isimler listesi for in döngüsü ile >>>>>")
for isim in isimler:
    print(isim)

# 8-b.	Liste elemanlarının sıra numarasıyla elemanları yazdırma(for in range len )

print("-"*30)
print( isimler[0] )
print( isimler[1] )
print( isimler[2] )

print("-"*30)
# Örnek : for döngüsü ile 0-5 arası sayıları ekrana yazdırın
for sayi in range(3):
    print(sayi)

print("-"*30)
for sayi in range(3):
    print( isimler[sayi] )

print("isimler listesinde {} tane eleman var".format(len(isimler)))
print("-"*30)
print("\n--> sayilar listesi for sayac in range(len(listeAdi)) döngüsü ile >>>>>")
for sayi in range( len(isimler) ):
    print( isimler[sayi] )

# 8-c.	while döngüsü ile listenin elemanlarını yazdırma
# Örnek : while döngüsü ile 0'dan 5'e kadar olan sayıları ekrana yazdırın
print("-"*30)

sayi = 0
while sayi < 6:
    print(sayi)
    sayi += 1
print("-"*30)

meyveler = ["elma", "armut", "erik", "mango","çilek","muz"]
# Örnek : meyveler listesinin elemanlarını while döngüsü ile ekrana yazdırın
sayac = 0
while sayac < len(meyveler):
    print( meyveler[sayac] )
    sayac += 1


print("-"*10, "9. LİSTELERİ SIRALAMA")
# sort() metodu ile sıralama
# Parametre almaz ise varsayılan olarak küçükten büyüğe sıralar.
# reverse=True parametresi ile büyükten küçüğe sıralar.
# Kullanımı : listeAdi.sort()

sayilar = [14,3,-5,45,8]

# Örnek : sayilar listesini küçükten büyüğe sıralayınız
print("\nsayilar listesi küçükten büyüğe sıralama")
print("Sıralamadan önce :", sayilar)
sayilar.sort()
print("Sıralamadan sonra :", sayilar)

# Örnek : sayilar listesini küçükten büyüğe sıralayınız
print("\nsayilar listesi büyükten küçüğe sıralama")
print("Sıralamadan önce :", sayilar)
sayilar.sort(reverse=True)
print("Sıralamadan sonra :", sayilar)

# Örnek : isimler listesini küçükten büyüğe sıralayınız
isimler = ["ali", "veli", "emir" , "engin", "emre", "zafer"]
print("\nisimler listesi büyükten küçüğe sıralama")
print("Sıralamadan önce :", isimler)
isimler.sort()
print("Sıralamadan sonra :", isimler)


print("-"*10, "10.LİSTELERİ KOPYALAMA")

# a. copy() metodu ile liste kopyalama
sayilar1 = [3,5,15,43]
sayilar2 = sayilar1.copy()

print("\nsayilar1 listesi :",sayilar1)
print("sayilar2 listesi :",sayilar2)

sayilar1[0] = 67
sayilar2[2] = 39

print("\nsayilar1 listesi :",sayilar1)
print("sayilar2 listesi :",sayilar2)

# b. list() metodu ile
kuslar1 = ["kartal","şahin", "leylek"]
kuslar2 = list(kuslar1)

print("\nkuslar1 listesi :",kuslar1)
print("kuslar2 listesi :",kuslar2)


print("-"*10, "11. LİSTELERİ BİRLEŞTİRME")
# 11-a.	+ operatörü ile
sayilar1 = [1,2,3,4,5]
sayilar2 = [6,7,8,9]
sayilar3 = sayilar1 + sayilar2
print("sayilar1 listesi :",sayilar1)
print("sayilar2 listesi :",sayilar2)
print("sayilar3 listesi :",sayilar3)


# 11-b.	append() ile listenin elemanlarını diğer listenin sonuna ekleme
sayilar1 = [1,2,3,4,5]
sayilar2 = [34, 45]
print("\nsayilar1 listesi :",sayilar1)
print("sayilar2 listesi :",sayilar2)
# Örnek : sayilar2 listesinin sonuna sayilar1 listesini ekleyiniz
for eleman in sayilar1:
    sayilar2.append(eleman)

print("\nsayilar1 listesi :",sayilar1)
print("sayilar2 listesi :",sayilar2)

# 11-c.	extend() metodu ile
sayilar1 = [0,2,4,6]
sayilar2 = [1,3]
print("\nsayilar1 listesi :",sayilar1)
print("sayilar2 listesi :",sayilar2)

sayilar1.extend(sayilar2)
#sayilar2.extend(sayilar1)

print("\nsayilar1 listesi :",sayilar1)
print("sayilar2 listesi :",sayilar2)


# Kullanımı : count(arananEleman)
sayilar = [1,2,3,4,1,2,15,30,1,8]
print( "sayilar listesinde 65 rakamı",sayilar.count(65),"kez geçiyor" )

# Bir elemanın listede olup olmadığını nasıl öğreniriz ?
# if arananEleman in listeAdi:  yapısı ile yapabiliriz.
# Eğer arananEleman değişkeninin içindeki değer listede mevcutsa True,
# yok ise False değeri döner

isimler =  ["ali", "veli", "hasan"]
arananEleman = "veli"
if arananEleman in isimler:
    print(arananEleman, "listede bulundu...")
else:
    print(arananEleman, "listede yok !!!!")
"""

# Listedeki elemanın sıra numarasını bulma
# Kullanımı : listeAdi.index(arananEleman)
# !!! Eğer aranan eleman listede yok ise hata verir.
# eğer aranan eleman listede ise o elemanın sıra numarasını verir.
isimler =  ["ali", "veli", "hasan"]
arananEleman = "ahmet"
#konum = isimler.index(arananEleman)
#print("Aranan eleman {}, listede {}. sırada.".format(arananEleman, konum))

if arananEleman in isimler:
    konum = isimler.index(arananEleman)
    print("Aranan eleman {}, listede {}. sırada.".format(arananEleman, konum))
else:
    print("!!! aranan eleman listede yok...")

# listeyi tersine çevirme
# reverse() fonksiyonu ile
# Kullanımı : listeAdi.reverse()
print(isimler)
isimler.reverse()
print(isimler)

sayilar = [1,15,3,54]
print(sayilar)
sayilar.reverse()
print(sayilar)
