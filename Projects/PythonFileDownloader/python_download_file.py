# Python İle Dosya İndirme
# Downloading File With Python
# Mustafa SOLAK
# 03-03-2023

import requests

# Dosya adreslerinin bulunduğu dosyayı açıyoruz
# Opening file which contains file names to be downloaded
ms_file = open("file_names.txt", "r")

# Dosyanın içeriği okunuyor
# reading the file content
fileData = ms_file.read()

# Dosyalar içinde bir alt satıra geçilmesi satır sonu karakterini ortaya çıkarır.
# Bir alt satıra geçmek için enter düğmesine bastığımızda imleç sonraki satıra geçer.
# Dosyayı bir metin editörü ile açtığımızda herhangi bir harici karakter görülmez.
# Ancak dosya okuma işlemlerinde dosya okunurken bir alt satıra geçilmesini sağlayan
# satır sonu karakteri \n ortaya çıkar. Biz de tüm satırları bu karakter ile parçaladığımızda
# her bir satır ayrı ayrı elimizde olur.
# fileData içeriğini \n ile parçalara ayırdığımızda(split) tüm satırlar bir liste halinde
# elimizde olur. 
# replacing end splitting the text
# when newline ('\n') is seen.
adresses = fileData.split("\n")


#print(adresses)
# ms_file isimli dosya okuyucumuzu kapatıyoruz.
# closing file reader
ms_file.close()


# Dosya sayısı yazdırılıyor
# print the number of addresses  
print("Toplam {0} adet dosya bulundu.".format(len(adresses)))
print("Dosya indirme işlemi başlıyor...")
#print("{0} files found. ".format(len(adresses)))
#print("Starting download...")
print("..............")

# İnen dosyaların isimlerini sıra numarası ile ekrana yazdırıyoruz
# Bunun için counter adında bir değişken tanımlayıp 1 değerini atıyoruz.
# print the names of the files on the screen with sequence number
# defined variable named counter and assign value 1
counter = 1

# for döngüsü ile tüm adres listesi üzerinde bir gezinme işlemi yapacağız.
# iterate addresses with for loop
for url in adresses:    

    # Dosya adresini / karakteri ile parçalıyoruz ve en son parçayı alıyoruz.
    # En son parça dosya adının olduğu parçadır. Bu dosya adını da dosyayı
    # kaydederken kullanacağız. 
    # parsing url with / character. taking last part because the last part is
    # the part with the filename. we'll use it to give a name to saved file
    pieces = url.split("/")
    lastPiece = pieces[len(pieces)-1]

    # Kaydedilecek dosya adını oluşturuyoruz. 
    # we are creating file name with counter to ensure that file has been downloaded and sequence
    savedFileName = str(counter) + "_" + lastPiece

    # Belirtilen adres için istek oluşturuldu ve isteğin sonucu az önce oluşturduğumuz
    # dosya adı ile kaydedildi.
    r = requests.get(url)
    open(savedFileName, 'wb').write(r.content)

    # Kullanıcıyı indirme işlemi hakkında bilgilendiriyoruz
    # informing user about downloading process
    print("{0}. dosya indirildi. Dosya adı : {1}".format(counter, savedFileName))
    #print("{0}. file downloaded. Filename : {1}".format(counter, savedFileName))

    # counter değişkeninin değerini 1 arttırıyoruz
    # increasing counter variable by 1
    counter+=1

# İndirme işleminin tamamlandığını belirtiyoruz.
# Indicating that the download process is complete
print("İndirme işlemi tamamlandı.")    
#print("Download operation completed.")    




