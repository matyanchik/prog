def f():
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

    zoo.insert(1, "bear")
    print(zoo)

    birds = ['rooster', 'ostrich', 'lark', ]
    for i in birds:
        zoo.append(i)
    print(zoo)

    zoo.pop(zoo.index("elephant"))
    print(zoo)

    for i in ["lion", "lark"]:
        print(zoo.index(i))

f()

def test(capfd):
    f()
    out, err = capfd.readouterr()
    assert out == "['lion', 'bear', 'kangaroo', 'elephant', 'monkey']\n\
['lion', 'bear', 'kangaroo', 'elephant', 'monkey', 'rooster', 'ostrich', 'lark']\n\
['lion', 'bear', 'kangaroo', 'monkey', 'rooster', 'ostrich', 'lark']\n\
0\n\
6\n"
