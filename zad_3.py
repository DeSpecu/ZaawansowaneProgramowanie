def CzyParzysta(x: int) -> bool:
    return x%2==0

x = CzyParzysta(5)

if x:
    print("Parzysta")
else:
    print("Nieparzysta")