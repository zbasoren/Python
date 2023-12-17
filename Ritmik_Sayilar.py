# 1'den 10'a kadar olan tüm sayıların 100'e kadar olan ritmik sayılar tablosunu iç-içe döngü yapılarını kullanarak python dilinde kodlamasıdır.
for i in range(1, 11):
    print("-"*20)
    for y in range(0, 101, i):
        print(i,y)
