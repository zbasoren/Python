# Kullanıcıdan alınan 4 sayıdan en küçük olanını bulma kodları.
# Fonksiyon yazarak bulma

a = int(input("1.Sayıyı Giriniz :"))
b = int(input("2.Sayıyı Giriniz :"))
c = int(input("3.Sayıyı Giriniz :"))
d = int(input("4.Sayıyı Giriniz :"))


def min(a, b, c, d):
    if a < b and a < c and a < d:
        print("1.Sayı Küçüktür", a)
    elif b < a and b < c and b < d:
        print("2.Sayı Küçüktür", b)
    elif c < a and c < b and c < d:
        print("3.Sayı Küçüktür", c)
    else:
        print(("4.Sayı Küçüktür.", d))


print(min(a, b, c, d))
