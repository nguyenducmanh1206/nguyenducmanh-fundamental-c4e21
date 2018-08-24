size=[ 5, 7, 300, 90, 24 ,50, 75]
print("bay gio con cuu lon nhat cua toi co kich thuoc", max(size), "hay thit no'")
size[size.index(max(size))] = 8 
print("kich thuoc dan cuu cua toi la ", size)
for i in range(len(size)):
    size[i]=size[i]+50
print("dan cuu cua toi sau 1 thang la ", size)    
print("bay gio con cuu lon nhat cua toi co kich thuoc ", max(size), "hay thit no ")
size[size.index(max(size))] = 8
for i in range(len(size)):
    size[i]=size[i]+50
print("dan cuu cua toi sau 2 thang la ", size)  
print("kich thuoc dan cuu cua toi la ", size)
print("bay gio con cuu lon nhat cua toi co kich thuoc ", max(size), "hay thit no ")
size[size.index(max(size))] = 8
for i in range(len(size)):
    size[i]=size[i]+50
print("dan cuu cua toi sau 3 thang la ", size)
tongcannang=sum(size)
tien =tongcannang* 2
print("tong tien thu duoc la", tien, "$")









