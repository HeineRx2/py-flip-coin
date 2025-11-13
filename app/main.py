import random
import matplotlib.pyplot as plt


def flip_coins():
    result = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
    }
    for i in range(10000):
        eagle = 0
        for n in range(10):
            throw = random.randint(0, 1)
            if throw == 1:
                eagle += 1
        result[eagle] += 1
    for k, v in result.items():
        result[k] = round((result[k] / 10000) * 100, 2)
    return result

def graphic_flip_coin():
    data = flip_coins()
    x = list(data.keys())
    y = list(data.values())
    plt.bar(x, y, color="skyblue", edgecolor="black")
    plt.xlabel("Количество орлов")
    plt.ylabel("Процент случаев")
    plt.title("Распределение выпадений орлов при 10 бросках")
    for i, value in enumerate(y):
        plt.text(i, value + 0.5, str(value), ha="center")
    plt.show()

graphic_flip_coin()
