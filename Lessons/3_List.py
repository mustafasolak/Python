# Örneğin sınıfınızda 25 öğrenci var ve her  bir öğrencinin isimlerini tutacaksınız.

# Boş bir liste aşağıdaki 2 yolla tanımlanabilir.
isimler = []
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

# Listeyi ekrana yazdırma
print("isimler listesinin içeriği")
for eleman in isimler:
    print(eleman)

print("renkler listesinin içeriği")
for renk in renkler:
    print(renk)