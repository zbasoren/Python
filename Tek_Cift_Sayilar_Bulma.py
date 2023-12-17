import numpy as np

# tek ve çift sayıları bulma yöntemleri
# append bir diziye ekleme için kullanılır..
ab = []
for i in range(1, 101):
    if i % 2 == 0:
        ab.append(i)
print(ab)
print("1 ile 100 arasındaki ÇİFT sayıların toplamı :", sum(ab))
# Numpy metodu ile adet sayısınıda bulmuş oluyoruz.
adet = np.size(ab)
print(adet)

xy = []

for i in range(1, 101):
    if i % 2 != 0:
        xy.append(i)
print(xy)
print("1 ile 100 arasındaki TEK sayıların toplamı :", sum(xy))
print("Tek ve Çift Sayıların Toplamı :", sum(ab) + sum(xy))
