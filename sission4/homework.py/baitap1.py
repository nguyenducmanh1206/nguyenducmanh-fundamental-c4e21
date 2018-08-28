a = input("nhap: ").lower()
b = list(a)
c = {}
for i in b:
    if c != " ":
        if i not in c:
            c[i] = 1
        else:
            c[i] += 1
c = sorted(c.items())
for d in c:
    print(d[0], "", d[1])







