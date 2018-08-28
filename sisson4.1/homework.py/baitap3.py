r1 ={
    "chuoi":2,
    "tao":3,
    "cam":1.5,
    "le":4,
}
r2 ={
    "chuoi": 6,
    "tao": 0,
    "cam": 32,
    "le": 15,
}
ten = ["chuoi","tao", "cam", "le" ]
gia = [ r1["chuoi"], r1["tao"], r1["cam"], r1["le"] ]
soluong = [ r2["chuoi"], r2["tao"], r2["cam"], r2["le"] ]
total = 0
for i in range(0, 4):
    print(ten[i])
    print("gia", gia[i])
    print("so luong", soluong[i])
    tien=(gia[i] * soluong[i])
    print("tien thu duoc", tien)
    # tongtien = total + tien
    # print("tong tien thu duoc la", tongtien)
tonggia=total + gia[0] * soluong[0] + gia[1] * soluong[1] + gia[2] * soluong[2] + gia[3] * soluong[3]
print("tong tien thu duoc la", tonggia)

    
   





