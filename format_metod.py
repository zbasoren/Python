# {} bu parantez için . formattan sonraki her tırnak sırasıyla temsil etmektedir.
# .Format dan sonra her tırnağa ne yazarsak onu ekler.

# 1. Kullanım Yolu
x = """
Eskişehir : Çibörek
Kütahya :   {}
Konya :     {}

""".format("Porselen", "Mevlana")

print(x)
# 2. Kullanım Yolu

x = "123456"
for i in x:
    print("Hayata {} - 0 Önde Başla".format(i))

# 3. Kullanım Yolu

a = "Python"
b = "Yazılım'ı"
c = "Öğreniyorum"

d = "{} {} {}".format(a, b, c)
print(d)
## Parantez içerisine rakamları değiştirerek sıralamaya yöne verebiliyoruz..
m = "{2} {1} {0}".format(a, b, c)
print(m)

# 4. Kullanım Yolu--- Estetiklik açısından en güzeli bence bu.

B = "Python"
Z = "|{:>50}|".format(B)
print(Z)  ## Bunun Çıktısı Şöyle oluyor.Soldan 50 boşluk Bırakıyor.
Z = "|{:<50}|".format(B)
print(Z)  ## Bunun Çıktısı Şöyle oluyor.Sağdan 50 boşluk Bırakıyor.
Z = "|{:^50}|".format(B)
print(Z)  ## Bunun Çıktısı Şöyle oluyor.Her İki tarafdan 50 boşluk bırakır.