class Insan:
   def __init__(self, ad, soyad, yas, ulke, sehir):

     self.ad = ad
     self.soyad = soyad
     self.yas = yas
     self.ulke = ulke
     self.sehir = sehir
     self.yetenekler = []

   def kisi_bilgileri(self):
       return f'Adı soyadı : {self.ad} {self.soyad}  yaş : {self.yas} Ülkesi {self.ulke} Yaşadığı Şehir : {self.sehir}  Yeteneği : {self.yetenekler}'

   def yetenek_ekle(self, yetenek):
       self.yetenekler = yetenek

bilgiler = Insan("Mehmet", "Salih", 21, "Turkiye", "Istanbul")
bilgiler.yetenek_ekle(["python"])

print(bilgiler.kisi_bilgileri())