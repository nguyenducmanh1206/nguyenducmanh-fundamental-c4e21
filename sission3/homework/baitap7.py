menu =["thit bo", "thit ga", "ca"]
m =input("ban muon chon gi(U, R, D, C)")
if m =="R":
    for i, item in enumerate(menu):
        print(i+1, ". ", item) 
    
elif m =="C":
    new =input("ban muon them gi")
    menu.append(new)
    print(menu)
elif m =="U":
    n =int(input("vi tri ban muon update") )

    new=intput("thu ban muon update")
    menu[n-1]=new
    print(menu)
else :
    # n =int(input("vi tri ban muon xoa "))
    # menu.pop(n-1)
    # print(menu)
    new =input("thu ban muon xoa ")
    menu.remove(new)
    print(menu)






    






