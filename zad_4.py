def CzyWieksze(x: int,y: int,z: int) -> bool:
    return x+y>=z

x = CzyWieksze(5,6,20)

if x:
    print("Większe lub równe")
else:
    print("Mniejsze")