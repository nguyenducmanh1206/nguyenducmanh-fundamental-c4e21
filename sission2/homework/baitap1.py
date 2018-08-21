a =int(input("chieu cao cua ban la? "))
b = a/100
print(a, "(cm) = " , b , " (m)")
c =int(input("can nang cua ban la? "))
print(c, "(kg)")
BMI = c/(b*b)
if BMI<16:
    print("giam can nang")
elif 16 <= BMI <= 18.5:
    print("thieu can nang")
elif 18.5<=BMI<=25:
    print("binh thuong")
elif 25<BMI<=30:
    print("thua can nang")
elif BMI>30:
    print("beo phi")










