menu =["my xao", "com rang", "pho bo"]
print(menu)
    # for i, item in menu:
    #     print(i, item)




while True:
    commad =input("what you you want (C, R, U, D)").upper()
    if commad == "C":
        new=input("ban muon them gi ")
        menu.append(new)
        print(menu)
    elif commad =="R":
        for i, item in enumerate(menu):
            print(i, item)




    elif commad =="U":
        n =int(input("vi tri ban muon thay doi " ))
        new=input("ban muon thay doi gi ")
        menu[n-1]=new
        print(menu)


    






