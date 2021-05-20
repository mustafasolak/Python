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
sayilar = [ 1,3,5,7,9,11,13,15 ]
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
print("\narabalar[2:4] = [1,2,3,4,5]")
print(arabalar)

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
# print(arabalar) # bu satır hata verir. çünkü arabalar listesini hafızadan kaldırdık

# Listenin elemanlarını yazdırma
eski_yerlesimler = ["Göbeklitepe","Piramitler", "Stonehenge", "Mayalar", "Aztekler" , "İnkalar", "Machu Pichu"]
# for eleman in listeAdi:
#    print(eleman)

for isim in eski_yerlesimler:
    print(isim)