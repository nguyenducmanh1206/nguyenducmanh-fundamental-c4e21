menu={
    "ngoc le":"pho",
    "quang":"pet le",
    "age":"20",

}
while True:
    print(menu)
    name=input("ban muon thong tin gi ")
    if name in menu:

        print(menu[name])
    else:
        m=input("ban co muon bo sung khong(Co, Khong)")
        if m == "Co":
            n=input("ban muon them gi")
            a=input("giai thich")
            name[n]= a
            print("them thanh cong")
            
            
           
            
        elif m =="Khong":
            print(name)






