### Return İçin 2 Örnek Fonksiyon ile.....(Atom)

def hesapla(ısı, sıcaklık, nem):
    return (ısı * sıcaklık) / nem


print(hesapla(10, 20, 30))


def deger(ısı, sıcaklık, nem):
    a = ısı * 3
    b = sıcaklık * 4
    c = nem ** 3
    d = ısı ** sıcaklık - nem
    return a, b, c, d


print(deger(10, 20, 30))
