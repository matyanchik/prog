zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]
zoo.insert(1, "bear")
print(zoo)
for i in birds:
    zoo.append(i)
print(zoo)
zoo.pop(zoo.index("elephant"))
print(zoo)
for i in ["lion", "lark"]:
    print(zoo.index(i))