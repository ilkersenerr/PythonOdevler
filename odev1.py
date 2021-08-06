def bolunenSayiBulma(min_sayi, max_sayi, bolunensayi):
    sonuc = 0
    bolen = []
    sayi2 = list(range(min_sayi, max_sayi + 1))

    for sayi1 in sayi2:
        if sayi1 % bolunensayi == 0:
            bolen.append(sayi1)
            sonuc = sonuc+1

    return print(bolen, sonuc)
bolunenSayiBulma(1,16,3)