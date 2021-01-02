import sqlite3
class Kitap:
    def __init__(self, isim, yazar, yayinevi, tur, baski):
        self.isim = isim
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.tur = tur
        self.baski = baski
    def __str__(self):
        return f"Kitap isim: {self.isim}\nYazar: {self.yazar}\n Yayınevi: {self.yayinevi}\nTür: {self.tur}\nBaskı: {self.baski}"
class Kutuphane:
    def __init__(self):
        self.baglanti_olustur()
    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("kutuphane.db")
        self.cursor = self.baglanti.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS kitaplar 
        (isim TEXT,
         yazar TEXT,
          yayinevi TEXT,
           tur TEXT,
            baski INT)""")
        self.baglanti.commit()
    def baglanti_kes(self):
        self.baglanti.close()
    def kitaplari_goster(self):
        self.cursor.execute("SELECT * FROM kitaplar")
        kitaplar = self.cursor.fetchall()
        if len(kitaplar) == 0:
            print("Kütüphanede her hangi bir kitap bulunmuyor.")
        else:
            for i in kitaplar:
                print(i)
    def kitap_sorgula(self, isim):
        self.cursor.execute("SELECT * FROM kitaplar WHERE isim = ?", (isim,))
        kitaplar = self.cursor.fetchall()
        if len(kitaplar) == 0:
            print("Kütüphanede kitap bulunamadı...")
        else:
            for i in kitaplar:
                print(i)
    def kitap_ekle(self, kitap):
        self.cursor.execute("INSERT INTO kitaplar VALUES (?, ?, ?, ?, ?)",(kitap.isim, kitap.yazar, kitap.yayinevi, kitap.tur, kitap.baski))
        self.baglanti.commit()
    def kitap_sil(self, isim):
        self.cursor.execute("DELETE FROM kitaplar WHERE isim = ?", (isim,))
        self.baglanti.commit()
    def baski_yukselt(self, isim):
        self.cursor.execute("SELECT * FROM kitaplar WHERE isim = ?", (isim,))
        kitaplar = self.cursor.fetchall()
        if len(kitaplar) == 0:
            print("Kitap bulunmuyor.")
        else:
            baski = kitaplar[0][4]
            baski += 1
            self.cursor.execute("UPDATE kitapler SET baski = ? WHERE isim ?", (baski, isim))
            self.baglanti.commit()
