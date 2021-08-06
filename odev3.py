class Ogrenci:
    def __init__(self, ogrenciAdi, ogrenciSoyadi, ogrenciSinifi):
        self.ogrenciAdi    = ogrenciAdi
        self.ogrenciSoyadi = ogrenciSoyadi
        self.ogrenciSinifi = ogrenciSinifi
​
​
class Soru:
    def NetSayisi(dogru, yanlis):
        return dogru - yanlis * 0.25
​
    def Hesapla(net):
        return net * 2
​
​
if __name__ == "__main__":
​
    ogrenci = Ogrenci(
                 input("Öğrenci adını giriniz: "),
                 input("Öğrenci soyadını giriniz: "),
                 input("Öğrenci sınıfını giriniz: "),
              )
​
    net = Soru.NetSayisi(
                 int(input("Doğru sayısını giriniz: ")),
                 int(input("Yanlış sayısını giriniz: "))
              )
​
    puan = Soru.Hesapla(net)
​
​
    print(f"\nÖğrenci adı:    {ogrenci.ogrenciAdi}" + \
          f"\nÖğrenci soyadı: {ogrenci.ogrenciSoyadi}" + \
          f"\nÖğrenci sınıfı: {ogrenci.ogrenciSinifi}" + \
          f"\nNet sayısı:     {net}" + \
          f"\nPuan:           {puan}")