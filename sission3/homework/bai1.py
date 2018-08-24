mathang=["T-Shirt ", "Sweat", "áo len "]
print(mathang)
    
while True:
    c =input("nhung gi ban muon (C, R, U, D) ").upper()
    if c == "R":
        print("mat hang cua chung toi ", mathang)
    elif c =="C":
        new = input(" ban muon them mat hang gi ")
        mathang.append(new)
        print("mat hang cua chung toi ", mathang)
    elif c=="U":
        n=int(input("vi tri ban muon thay doi"))
        new=input("ban muon thay doi gi ")
        mathang[n-1]=new
        print("mat hang cua chung toi", mathang)
    elif c=="D":
        n=int(input("vi tri ban muon xoa "))
        mathang.pop(n-1)
        print(mathang)








