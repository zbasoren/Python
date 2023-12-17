# 100 ile 10000 arasındaki Çift ve Tek sayıların Toplamını ayrı ayrı hesaplayıp ekrana yazdıran kod..
ab = []
ac = []


def tek(x, y):
    for i in range(x, y):
        if i % 2 != 0:
            ab.append(i)
    print(ab)


print(tek(100, 10001))
print(sum(ab))


def cift(x, y):
    for i in range(x, y):
        if i % 2 == 0:
            ac.append(i)
    print(ac)


print(cift(100, 10001))
print(sum(ac))

