R = float(input("Dairenin Çapını Giriniz :"))


def alan(r):
    alan = 3.1415923565 * (r / 2) ** 2
    return "Dairenin alanı :", alan


print(alan(R))

def cevre(x):
    cevre=2*3.1415923565 * x/2
    return  "Dairenin Çevresi :" ,cevre

print(cevre(R))
