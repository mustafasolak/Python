
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
