def CzyIstnieje(x: list, y: list) -> list:
    for i in x:
        y.append(i)

    y = list(set(y))

    for j in range(len(y)):
        y[j] = y[j]**3

    return y

print(CzyIstnieje([1,2,3],[3,4,5]))