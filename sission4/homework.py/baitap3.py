gia ={
    "chuoi":2,
    "tao":3,
    "cam":1.5,
    "le":4,
}
soluong ={
    "chuoi": 6,
    "tao": 0,
    "cam": 32,
    "le": 15,
}
name = ["chuoi", "tao", "cam", "le"]
for i in name:   
    print(i)
    print("gia:", gia[i])
    print("soluong:", soluong[i])
    print()

total = 0
for n in name:
    tien = gia[n]*soluong[n]
    print(n, "tien:", tien)
    total += tien
print("tong tien kiem duoc:", total, "$")





