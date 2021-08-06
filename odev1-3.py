vizeNotu = float(input("1. Vize notu gir : "))
if(vizeNotu >= 100 and vizeNotu <= 0):
  print()
else:
    print("Geçersiz not")
    raise SystemExit
vizeNotu2 = float(input("2. Vize notu gir : "))
if(vizeNotu2 >= 100 and vizeNotu2 <= 0):
    print()
else:
    print("Geçersiz not")
    raise SystemExit
finalNotu = float(input("Final notu gir :"))
if(finalNotu >= 100 and finalNotu <= 0):
    print()
else:
    print("Geçersiz not")
    raise SystemExit


ortalamaNot = (0.3 * vizeNotu) + (0.3 * vizeNotu) + (0.4 * finalNotu)

if finalNotu >= 50:
    if (ortalamaNot >= 90 and ortalamaNot <= 100):
        print("Harf Notunuz AA")
    elif ortalamaNot >= 85 and ortalamaNot < 90:
        print("Harf Notunuz BA")
    elif ortalamaNot >= 80 and ortalamaNot < 85:
        print("Harf Notunuz BB")
    elif ortalamaNot >= 75 and ortalamaNot < 80:
        print("Harf Notunuz CB")
    elif ortalamaNot >= 70 and ortalamaNot < 75:
        print("Harf Notunuz CC")
    elif ortalamaNot >= 65 and ortalamaNot < 70:
        print("Harf Notunuz DC")
    elif ortalamaNot >= 60 and ortalamaNot < 65:
        print("Harf Notunuz DD")
    elif ortalamaNot >= 55 and ortalamaNot < 60:
        print("Harf Notunuz FD")
    elif ortalamaNot >= 0 and ortalamaNot < 55:
        print("Harf Notunuz FF")

else:
    print("Harf Notunuz FF" )
print("Not ortalamanız : ", ortalamaNot)