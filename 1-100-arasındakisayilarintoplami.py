# 1 ile 100 arasındali sayıların toplamını bulma
#Matematik formülü ile bulmak
n = int(input("BİR SAYI GİRİNİZ :"))
x = (n * (n + 1)) / 2
print(x)

## Veya ?
### Kullanıcıdan sayı alarak verdiği sayıların toplamını bulmak
m = int(input("Bir sayı giriniz :"))
a=[]
for i in range(1,m+1):
    a.append(i)
print("Sayılar Toplamı :",sum(a))

a=[]
for i in range(1,101):
    a.append(i)
print("sayılar toplamı",sum(a))
