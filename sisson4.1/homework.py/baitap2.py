iven={
    "gold" : 500,
    "pouch" : ["flint", "twine", "gemstone"],
    "backpack" : ["xylophone", "dagger", "bedroll", "bread loaf"]
}
iven["pouch"] = ["flint", "twine", "gemstone", "khoa"]
print(iven)

n="pocket"
m=["seashell", "strang berry", "lint"]
iven[n]= m
print(iven)

iven["backpack"].remove("dagger")
print(iven)

iven["gold"] = 500, 50
print(iven)





