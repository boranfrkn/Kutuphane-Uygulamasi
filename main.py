from kutuphane import Kitap, Kutuphane
print("""
Kütüphane programına hoş geldiniz.
1-) Kitapları göster
2-) Kitap sorgula
3-) Kitap ekle
4-) Kitap sil
5-) Baskı yükselt

Çıkmak için 0'a basın.""")
kutuphane = Kutuphane()
while True:
    islem = int(input("Yapacağınız işlem:"))
    if islem == 0:
        print("Program kapandı.")
        break
    elif islem == 1:
        kutuphane.kitaplari_goster()
    elif islem == 2:
        giris = input("Sorgulamak istediğiniz kitapın adını yazınız:")
        kutuphane.kitap_sorgula(giris)
    elif islem == 3:
        isim = input("İsim:")
        yazar = input("Yazar:")
        yayinevi = input("Yayinevi:")
        tur = input("Tür:")
        baski = int(input("Baskı:"))
        kitap = Kitap(isim, yazar, yayinevi, tur, baski)
        kutuphane.kitap_ekle(kitap)
    elif islem == 4:
        giris = input("Silmek istediğiniz kitabın adını yazınız:")
        kutuphane.kitap_sil(giris)
    elif islem == 5:
        giris = input("Baskısını yükseltmek istediğiniz kitabın adını yazınız:")
        kutuphane.baski_yukselt(giris)