menu_items = ["pho bo", "my xao", "com rang"]
# for index, item in enumerate(menu_items):
#     print(index + 1,".", item, sep=" ")
# print("*" *10 )

# print(*menu_items, sep=",")

n =int(input("vi tri ma ban muon update "))
new =input("ban muon thay doi gi :")
menu_items[n-1] =new
print(*menu_items, sep=" ")





