def sayiAtama(a):
   if(a >= 10) and (a <= 99):
       print()
   else:
       return print("iki basamaklı sayı girmediniz")
       raise SystemExit
def sayiOkusu(deger):
     birler = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
     onlar = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
     bir = deger % 10
     on = deger // 10
     print(onlar[on], birler[bir])

sayi = int(input("iki basamaklı bir sayı giriniz : "))
sayiAtama(sayi)
sayiOkusu(sayi)