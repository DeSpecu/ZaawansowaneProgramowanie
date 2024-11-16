def CzyIstnieje(x: int, lista: list) -> bool:
    return x in lista

x = CzyIstnieje(5,[6,7])

if x:
    print("Istnieje")
else:
    print("Nie istnieje")