"""
# Boş bir liste 2 yolla oluşturulabilir.
# 1.yol []
print("-"*10, "[] İLE BOŞ LİSTE OLUŞTURMAK")
isimler = []
print(isimler)

# 2.yol list()
print("-"*10, "list() FONKSİYONU İLE BOŞ LİSTE OLUŞTURMAK")
arabalar = list()
print(arabalar)

# Boş olmayan bir liste nasıl oluşturulur ?
print("-"*10, "Boş olmayan bir liste nasıl oluşturulur ?")
sayilar = [1,3,5,15,45]
print(sayilar)

# LİSTELERE ELEMAN EKLEME
# append() metodu ile listenin sonuna eleman eklenir.
# Kullanımı : listeAdi.append(eklenecekDeger)

print("-"*10, "LİSTELERE ELEMAN EKLEME")

arabalar.append("Passat")
print(arabalar)

arabalar.append("Golf")
arabalar.append("Amarok")
arabalar.append("Şahin")
arabalar.append("Ferrari 430")
print(arabalar)

# LİSTEDE İSTEDİĞİMİZ SIRAYA ELEMAN EKLEME
# insert() fonksiyonu ile listenin istediğimiz sırasına eleman ekleriz.
# Kullanımı : listeAdi.insert(sıraNo, eklenecekDeger)

print("-"*10, "LİSTEDE İSTEDİĞİMİZ SIRAYA ELEMAN EKLEME")

arabalar.insert(2, "Murat 124")
print("\n--> arabalar.insert(2, 'Murat 124')")
print(arabalar)

arabalar.insert(0, "Beetle")
print("\n--> arabalar.insert(0, 'Beetle')")
print(arabalar)

arabalar.insert(-1, "Polo")
print("\n--> arabalar.insert(-1, 'Polo')")
print(arabalar)


    # LİSTENİN ELEMAN SAYISINI BULMAK
# len() fonksiyonu bize listenin eleman sayısını verir.
# Kullanımı : len(listeAdi)
print("-"*10, "LİSTENİN ELEMAN SAYISINI BULMAK")
print( "\narabalar listesinin eleman sayısı :", len(arabalar))

# LİSTENİN ELEMANLARINA ERİŞMEK
# Kullanımı : listeAdi[elemanSiraNo]

print("-"*10, "LİSTENİN ELEMANLARINA ERİŞMEK")
# Örnek: Golf modelini ekrana yazdırın
print( "\narabalar[2] :", arabalar[2] )

# Örnek: Şahin modelini ekrana yazdırın
print( "\narabalar[5] :", arabalar[5] )

# Örnek: Polo modelini listenin başından sıra numarası kullanarak ekrana yazdırın
print( "\narabalar[6] :", arabalar[6] )

# Örnek: Polo modelini listenin sonundan sıra numarası kullanarak(Negative indexing) ekrana yazdırın
print( "\narabalar[-2] :", arabalar[-2] )

# Listenin belirli bir aralığına erişmek
# Kullanımı : listeAdi[aralikBaslangic : aralikBitis]
print("\narabalar listesi şu anki hali")
print(arabalar)

# Örnek : Golf ile Şahin dahil bu aralıktaki değerleri alalım
print("\n--> arabalar[2:6]")
print( arabalar[2:6])

# Örnek : Amarok'tan itibaren arabalar listesinin tüm elemanlarını seçelim
# 1.yol
print("\n--> arabalar[4:8]")
print( arabalar[4:8] )
# 2.yol
print("\n--> arabalar[4:]")
print( arabalar[4:] )

# Örnek : arabalar listesinde listenin başından Şahin(dahil) değerine kadar olan aralığı seçelim
# 1.yol
print("\n--> arabalar[0:6]")
print( arabalar[0:6] )

# 2.yol
print("\n--> arabalar[:6]")
print( arabalar[:6] )


# LİSTENİN ELEMAN(LAR)INI DEĞİŞTİRMEK
# Kullanımı : listeAdi[elemanSiraNo] = yeniDeger
print("-"*10, "LİSTENİN ELEMAN(LAR)INI DEĞİŞTİRMEK")

# Örnek : arabalar listesi içerisindek Passat değerini Bora ile değiştirin
arabalar[1] = "Bora"
print( "\narabalar[1] = 'Bora' > ", arabalar )

# Örnek : arabalar listesi içerisindek Murat 124 değerini Citroen ile değiştirin
arabalar[3] = "Citroen"
print( "\narabalar[3] = 'Citroen' > ", arabalar )

# Örnek : arabalar listesi içerisindek Şahin değerini Negative İndexing ile Anadol değeriyle değiştirin
arabalar[-3] = "Anadol"
print( "\narabalar[-3] = 'Anadol' > ", arabalar )

# Listenin içindeki birden fazla elemanı değiştirmek
# Kullanımı : listeAdi[baslangic:bitis] = [yeni_Deger(ler)]
print("\narabalar listesi şu anki hali")
print(arabalar)

# Örnek : arabalar listesindeki Citroen ve Amarok değerlerini Renault ve Dacia ile değiştiriniz
arabalar[3:5] = ["Renault", "Dacia"]
print("\narabalar[3:5] = ['Renault', 'Dacia']")
print(arabalar)

# Örnek : arabalar listesinin 1:6 aralığını kendi belirlediğiniz yeni değerler ile değiştiriniz.
arabalar[1:6] = ["a","b","c","d","e"]
print("\narabalar[1:6] = ['a','b','c','d','e']")
print(arabalar)

# Örnek : arabalar listesindeki a,b,c değerlerinin hepsinin yerine sadece X değeri koyunuz
arabalar[1:4] = ["X"]
print("\narabalar[1:4] = ['X']")
print(arabalar)

arabalar[2:4] = [1,2,3,4,5]
print("\n", arabalar)

# LİSTEDEN ELEMAN SİLME
# remove() fonksiyonu ile listeden belirttiğimiz elemanı silebiliriz
# Kullanımı : listeAdi.remove(silinecekEleman)
print("-"*10, "LİSTEDEN ELEMAN SİLME")

# Örnek : arabalar listesindeki X değerini silelim
arabalar.remove("X")
print("\narabalar.remove('X')")
print(arabalar)

# Örnek : arabalar listesindeki 5 değerini silelim
arabalar.remove(5)
print("\narabalar.remove(5)")
print(arabalar)

# pop() fonksiyonu ile listeden eleman silme 2 şekilde olur.
# 1. listeAdi.pop() şeklinde kullanırsak listenin en sonundaki elemanı siler
# 2. listeAdi.pop(elemanSiraNo) şeklinde kullanırsak listenin belirttiğimiz sırasındaki elemanı siler

# Örnek : arabalar listesindeki son elemanı pop() fonksiyonu ile silelim
arabalar.pop()
print("\narabalar.pop()")
print(arabalar)

# Örnek : arabalar listesindeki son elemanı pop() fonksiyonu ile silelim
arabalar.pop()
print("\narabalar.pop()")
print(arabalar)

# Örnek : arabalar listesindeki 2 sıra numarasına sahip elemanını silelim
arabalar.pop(2)
print("\narabalar.pop(2)")
print(arabalar)

# Örnek : arabalar listesindeki 3 sıra numarasına sahip elemanını silelim
arabalar.pop(3)
print("\narabalar.pop(3)")
print(arabalar)

# Listeyi Temizleme
# clear() fonksiyonu listeyi tamamen boşaltır.
# Kullanımı : listeAdi.clear()

# Örnek : arabalar listesinin içindeki tüm elemanları clear() fonksiyonu ile silelim
arabalar.clear()
print("\narabalar.clear()")
print(arabalar)

# arabalar listesine örnek veri ekleyelim
arabalar.append("Polo")
arabalar.append("Tuarek")
print(arabalar)
# del ile Listeyi Silme, yok etme
# Dikkat ediniz!!! del ile bir liste silindikten sonra, silindiği satırdan itibaren artık o liste tanınmaz. Yani yorumlayıcı artık o listeyi yok etmiştir, kaldırmıştır.
del arabalar
# print(arabalar) # Bu satır hata verdiği için yorum satırı yaptık


# Listenin elemanlarını yazdırma
eski_yerlesimler = ["Göbeklitepe","Piramitler", "Stonehenge", "Mayalar", "Aztekler" , "İnkalar", "Machu Pichu"]
# 8- a.	for in döngüsü ile listenin elemanlarını yazdırmaa.
# Kullanımı
# for degiskenAdi in listeAdi:
#    print(eleman)

for yerlesim_yeri in eski_yerlesimler:
    print(yerlesim_yeri)

meyveler = ["elma", "armut","erik", "kayısı" , "çilek"]
# Örnek: meyveler listesinin elemanlarını for in döngüsü ile ekrana yazdırınız
for meyve in meyveler:
    print(meyve)

sayilar = [ 1, 3, 5, 7, 9, 11]
# Örnek : sayilar listesinin içindeki elemanların karesini alıp for in döngüsü ile ekrana yazdırın
for sayi in sayilar:
    print( "{}'in karesi = {}".format(sayi, sayi ** 2 ) )

print( sayilar[0] )
print( sayilar[1] )
print( sayilar[2] )
print( sayilar[3] )
print( sayilar[4] )
print( sayilar[5] )

# 8-b.	Liste elemanlarının sıra numarasıyla elemanları yazdırma(for in range len )
# Kullanımı :
# for sayac in range(len(listeAdi)):
#    print( listeAdi[sayac] )
# Örnek : sayilar listesinin elemanlarını, elemanların sıra numarasını kullanarak for in döngüsü ile ekrana yazdırınız
for sayac in range( len(sayilar) ):
    print( sayilar[sayac])

# Örnek : meyveler listesinin elemanlarını, elemanların sıra numarasını kullanarak for in döngüsü ile ekrana yazdırınız
for siraNo in range( len(meyveler) ):
    print( meyveler[siraNo])

# 8-c.	while döngüsü ile listenin elemanlarını yazdırma
# Örnek : 0'dan 5'e kadar olan sayıları while döngüsü ile ekrana yazdırın
sayac = 0
while sayac < 6:
    print( sayac )
    sayac += 1

sayilar = [ 1, 3, 5, 7, 9, 11]
# Örnek : sayilar listesinin içindeki elemanları while döngüsü ile ekrana yazdırın
sayac = 0
while sayac < len(sayilar):
    print( sayilar[sayac])
    sayac += 1

# 9.	LİSTELERİ SIRALAMA
# sort() metodu ile sıralama
# Parametre almaz ise varsayılan olarak küçükten büyüğe sıralar.
# reverse=True parametresi ile büyükten küçüğe sıralar.

sayilar = [35, 15, 45, 3, -5, 68, 0]
print("-"*30)
# Örnek: sayilar listesini küçükten büyüğe sıralayınız
print("Sıralamadan  önce sayilar listesi -> ", sayilar)
sayilar.sort()
print("Sıralamadan sonra sayilar listesi -> ", sayilar)

print("-"*30)
# Örnek: sayilar listesini büyükten küçüğe sıralayınız
print("Sıralamadan  önce sayilar listesi -> ", sayilar)
sayilar.sort(reverse=True)
print("Sıralamadan sonra sayilar listesi -> ", sayilar)

print("-"*30)
meyveler = ["elma", "armut","erik", "kayısı" , "çilek", "ergin"]
# Örnek: meyveler listesini büyükten küçüğe sıralayınız
print("Sıralamadan  önce meyveler listesi -> ", meyveler)
meyveler.sort(reverse=True)
print("Sıralamadan sonra meyveler listesi -> ", meyveler)


# 10.	LİSTELERİ KOPYALAMA
# a.	copy() metodu ile
print("-"*10, "LİSTELERİ KOPYALAMA")
sayilar1 = [1,2,3,4,5]
sayilar2 = sayilar1.copy()
print("sayilar1 listesi :", sayilar1)
print("sayilar2 listesi :", sayilar2)
sayilar1[0] = 15
sayilar2[3] = 45
print("\nsayilar1 listesi :", sayilar1)
print("sayilar2 listesi :", sayilar2)


# DİKKAT. LİSTE KOPYALAMAK İÇİN BU YÖNTEM KULLANILMAZ. HATALIDIR.
# ogrenciler1 = ["ali", "veli" ,"hasan"]
# ogrenciler2 = ogrenciler1
# print("\nogrenciler1 listesi :", ogrenciler1)
# print("ogrenciler2 listesi :", ogrenciler2)
#
# ogrenciler1[0] = "nuri"
# ogrenciler1[1] = "metin"
# ogrenciler2[0] = "Mehmet"
#
# print("\nogrenciler1 listesi :", ogrenciler1)
# print("ogrenciler2 listesi :", ogrenciler2)


# DOĞRUSU BUDUR
ogrenciler1 = ["ali", "veli" ,"hasan"]
ogrenciler2 = ogrenciler1.copy()
print("\nogrenciler1 listesi :", ogrenciler1)
print("ogrenciler2 listesi :", ogrenciler2)

ogrenciler1[0] = "nuri"
ogrenciler2[1] = "kamil"

print("\nogrenciler1 listesi :", ogrenciler1)
print("ogrenciler2 listesi :", ogrenciler2)

# 10-b.	list() metodu ile
sehirler1 = ["izmir"," ankara"," istanbul"]
sehirler2 = list(sehirler1)

print("\nsehirler1 listesi :", sehirler1)
print("sehirler2 listesi :", sehirler2)

sehirler1[0] = "manisa"
sehirler2[2] = "kayseri"

print("\nsehirler1 listesi :", sehirler1)
print("sehirler2 listesi :", sehirler2)

print("-"*10, "11-LİSTELERİ BİRLEŞTİRME")
# 11-a.	+ operatörü ile
sayilar1 = [1,2,3,4,5]
sayilar2 = [6,7,8,9,10]
sayilar3 =  sayilar1 + sayilar2
print("sayilar1 listesi :",sayilar1)
print("sayilar2 listesi :",sayilar2)
print("sayilar3 listesi :",sayilar3)


# 11-b.	append() ile listenin elemanlarını diğer listenin sonuna ekleme
sayilar1 = [2,4,6,8]
sayilar2 = [1,3,5,7]

# Örnek : append() metodu ile sayilar1 listesinin sonuna sayilar2 listesini ekleyin yani birleştirin
for eleman in sayilar2:
    sayilar1.append(eleman)
print("\nsayilar1 listesi :",sayilar1)
print("sayilar2 listesi :",sayilar2)

# 11-c.	extend() metodu ile  listeleri birleştirme
sayilar1 = [0,2,4,6]
sayilar2 = [1,3]
print("\nsayilar1 listesi :",sayilar1)
print("sayilar2 listesi :",sayilar2)

sayilar1.extend(sayilar2)
sayilar2.extend(sayilar1)

print("\nsayilar1 listesi :",sayilar1)
print("sayilar2 listesi :",sayilar2)
"""

# Kullanımı : count(arananEleman)
sayilar = [1,2,3,4,1,2,15,30,1,8]
print( "sayilar listesinde 1 rakamı",sayilar.count(1),"kez geçiyor" )

# if ... in ile listede bir elemanın olup olmadığını sorgulama
# Kullanımı :  if arananEleman in listeAdi: şeklinde
# Eğer arananEleman değişkeni içindeki değer belirtilen listede mevcut ise True döner, yok ise False döner.
isimler = ["ali" ,"veli", "hasan", "nuri"]
arananEleman = "veli"
if arananEleman in isimler:
    print("Aranan değer listede mevcut.")
else:
    print("!!! Aranan değer listede mevcut değil !!!")

# Listedeki elemanın sıra numarasını bulma
# Kullanımı : listeAdi.index(arananEleman)
# !!! Eğer aranan eleman listede yok ise hata verir.
# eğer aranan eleman listede ise o elemanın sıra numarasını verir.
konum = isimler.index(arananEleman)
print("Aranan eleman {}, listede {}. sırada.".format(arananEleman, konum))


# örnek : Kamil ismini isimler listesinde aratın ve konumunu ekrana yazdırın
arananEleman = "nuriş"
if arananEleman in isimler:
    konum = isimler.index(arananEleman)
    print("Aranan eleman {}, listede {}. sırada.".format(arananEleman, konum))
else:
    print(arananEleman, "değeri listede yok !!!")


# listeyi ters çevirme
# Kullanımı : listeAdi.reverse()
sayilar = [1,15,3,58,5,4]
print(sayilar)
sayilar.reverse()
print(sayilar)











