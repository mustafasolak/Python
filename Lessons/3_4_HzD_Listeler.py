# 8.	LİSTENİN ELEMANLARINI YAZDIRMA
# a.	for in döngüsü ile listenin elemanlarını yazdırma
"""
print("-"*30, "for .. in döngüsü ile listenin elemanlarını yazdırma")
isimler = ["ali", "veli", "hasan"]
# Kullanımı :
# for eleman in listeAdi:
#   print(eleman)
# Örnek: isimler listesinin içeriğini for .. in döngüsü ile ekrana yazdıralım
for isim in isimler:
    print(isim)

sayilar = [1,3,4,65]
# Örnek : sayilar listesinin içeriğindeki her elemanın karesini for .. in döngüsü ile ekrana yazdıralım
for sayi in sayilar:
    print(sayi ** 2)


# b.	Liste elemanlarının sıra numarasıyla elemanları yazdırma(for in range len )
print("-"*30, "Liste elemanlarının sıra numarasıyla elemanları yazdırma(for in range len )")
meyveler = ["elma","armut", "erik", "kiraz", "çilek"]

print("Meyveler listesinde {} tane eleman vardır.".format(len(meyveler)))
for sayac in range( len(meyveler) ):
    print(meyveler[sayac])

# c.	while döngüsü ile listenin elemanlarını yazdırma
print("-"*30, "while döngüsü ile listenin elemanlarını yazdırma")
# Örnek : meyveler listesi içerisindeki elemanları while döngüsü ile ekrana yazdıralım
sayac = 0
while sayac < len(meyveler) :
    print( meyveler[sayac] )
    sayac += 1

# 9.	LİSTELERİ SIRALAMA
# sort() metodu ile sıralama
# Parametre almaz ise varsayılan olarak küçükten büyüğe sıralar.
# reverse=True parametresi ile büyükten küçüğe sıralar.
# Kullanımı : listeAdi.sort()   # Küçükten büyüğe sıralama yapar
# Kullanımı : listeAdi.sort(reverse=True) # Büyükten küçüğe sıralar

sayilar = [1,15,65,45,-3,0,2]

# Örnek : sayilar listesinin elemanlarını küçükten büyüğe sıralayınız
print("Sıralamadan önce sayilar listesi :", sayilar)
sayilar.sort()
print("Sıralamadan sonra sayilar listesi :", sayilar)

print("\n")
sayilar = [1,15,65,45,-3,0,2]
# Örnek : sayilar listesinin elemanlarını büyükten küçüğe  sıralayınız
print("Sıralamadan önce sayilar listesi :", sayilar)
sayilar.sort(reverse=True)
print("Sıralamadan sonra sayilar listesi :", sayilar)

# 10.	LİSTELERİ KOPYALAMA
# a.	copy() metodu ile
sayilar1 = [1,2,3,4,5]
sayilar2 = sayilar1.copy()
print("sayilar1 listesi :", sayilar1)
print("sayilar2 listesi :", sayilar2)

sayilar1[0] = 87
sayilar2[3] = 95

print("\nsayilar1 listesi :", sayilar1)
print("sayilar2 listesi :", sayilar2)


# b.	list() metodu ile
sehirler1 = ["izmir"," ankara"," istanbul"]
sehirler2 = list(sehirler1)
print("\nsehirler1 listesi :", sehirler1)
print("sehirler2 listesi :", sehirler2)


# 11.	LİSTELERİ BİRLEŞTİRME
# a.	+ operatörü ile
sayilar1 = [1,2,3,4,5]
sayilar2 = [6,7,8,9,10]

# Örnek : sayilar1 ile sayilar2 listesini birleştiriniz ve sayilar3 listesine atınız
sayilar3 = sayilar1 + sayilar2
print("sayilar3 listesi =", sayilar3)

# Örnek : sayilar1 ile sayilar2 listesini birleştiriniz ve oluşan listeyi sayilar2 listesine atınız
sayilar2 += sayilar1 # sayilar2 = sayilar2 + sayilar1
print("sayilar2 listesi =", sayilar2)

# b.	append() ile listenin elemanlarını diğer listenin sonuna ekleme
#
sayilar1 = [2,4,6,8]
sayilar2 = [1,3,5,7]

# Örnek : sayilar1 listesinin sonuna sayilar2 listesini ekleyin
print(sayilar1)
for sayi in sayilar2:
    sayilar1.append(sayi)
print(sayilar1)

# c.	extend() metodu ile
sayilar1 = [0,2,4,6]
sayilar2 = [1,3]

# Örnek : sayilar1 listesi ile sayilar2 listesini sayilar1 listesi üzerinde birleştirin
print(sayilar1)
sayilar1.extend(sayilar2)
print(sayilar1)



# 12.	LİSTEDE BİR ELEMANIN KAÇ TANE OLDUĞUNU BULMA
# count() fonksiyonu ile
# Kullanımı : listeAdi.count(arananEleman)

ulkeler = ["TÜRKİYE", "Almanya" , "Avusturya" , "Arnavutluk", "TÜRKİYE"]
# Örnek : ulkeler listesinde TÜRKİYE değerinin kaç tane olduğunu bulunuz
arananEleman = "TÜRKİYE"
miktar = ulkeler.count( arananEleman )
print("ülkeler listesinde {} değeri {} adet".format(arananEleman,miktar))

# 13.	LİSTEDE ELEMAN ARAMA
#
# # if ... in ile listede bir elemanın olup olmadığını sorgulama
# # Kullanımı :  if arananEleman in listeAdi: şeklinde
# # Eğer arananEleman değişkeni içindeki değer belirtilen listede mevcut ise True döner, yok ise False döner.

# Örnek 45 sayısının sayilar listesinde olup olmadığını bulunuz, eğer varsa kaç tane olduğunu yazdırın
sayilar = [15, 45, 65, 33, 87, 45]
arananSayi = 45
if arananSayi in sayilar:
    print(arananSayi, "sayilar listesinde mevcut.")
    print(arananSayi, "sayilar listesinde", sayilar.count(arananSayi), "tane")
else:
    print("Bu değer listede yok !!!")


# 14.	LİSTEDEKİ ELEMANIN KONUMUNU,SIRASINI,İNDİSİNİ BULMA
# index() fonksiyonu ile
# # Kullanımı : listeAdi.index(arananEleman)
# # !!! Eğer aranan eleman listede yok ise hata verir.
# # eğer aranan eleman listede ise o elemanın sıra numarasını verir.

meyveler = ["elma","kivi", "çilek","muz","ananas"]
arananMeyve = "muz"

if arananMeyve in meyveler:
    konum = meyveler.index(arananMeyve)
    print(konum)
else:
    print("Aranan eleman listede yok !!!")

"""


# 15.	LİSTEYİ TERS ÇEVİRME
# reverse() fonksiyonu ile
# Kullanımı : listeAdi.reverse()

sayilar = [13,35,5,57,-5]
print(sayilar)
sayilar.reverse()
print(sayilar)















