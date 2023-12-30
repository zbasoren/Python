import os  # os bilgisayarımızdaki herşeyi müdahale etmemizi sağlar...

os.system("cls")

Kitap_Liste = list()

Menu = ("""
1)Kitap Ekle
2)Kitap Çıkar
3)Kitapları Listele
Q)Çıkış
""")


def kitapekle(liste, kitap):
    liste += [kitap]
    print("{} Adlı Kitap Başarıyla eklenmiştir.\a\1".format(kitap))
    input("Ana Menüye Dönmek için Enter'a basınız.")


def kitapcikar():
    pass


def listele(Kitap_Liste):
    for a in Kitap_Liste:
        print("Kitap Adı ======>>>> {}".format(a))
    input("Ana Menüye Dönmek için Enter'a basınız.")


def cikis():
    quit()


while True:
    print(Menu)
    secim = input("Yapmak İstediğiniz İşlemi Seçiniz :")

    if secim == "1":
        kitap_adi = input("Eklemek İstediğiniz Kitap Adını Giriniz :")
        kitapekle(Kitap_Liste, kitap_adi)

    elif secim == "2":
        kitapcikar()

    elif secim == "3":
        listele(Kitap_Liste)

    elif secim == "q" or secim == "Q":
        print("Güle Güle Yine Bekleriz .... \1")
        cikis()

    else:
        print("Hatalı seçim yapılmıştır.")
        input("Ana Menüye Dönmek için Enter'a basınız.")
