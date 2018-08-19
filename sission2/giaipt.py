
a = int(input("nhap so a? "))
b = int(input("nhap so b? "))
c = int(input("nhap so c? "))
d = b**2 - 4*a*c
if d > 0 :

    x1=(-b+d*1/2)/2*a
    x2=(-b-d*1/2)/2*a
    print("pt co 2 nghiem phan biet",x1 ,x2)
elif d == 0 :

    x=-b/2*a
    print("pt co 1 ngiem ", x)
else  :
    print("pt vo nghiem ")




