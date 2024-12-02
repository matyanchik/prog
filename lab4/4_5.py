zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
zoo.insert(1, "bear")
print(zoo)

birds = ['sparrow', 'parrot', 'eagle']

for i in birds:
    zoo.append(i)
print(zoo)

zoo.pop(zoo.index("elephant"))
print(zoo)

for i in ["lion", "lark"]:
    print(zoo.index(i) if i in zoo else f"{i} не найдено в зоопарке")
