def Parzyste(liczby):
    if len(liczby) != 10:
        print("Zła ilość")
        return
    for x in liczby:
        if type(x) != int and type(x) != float:
            continue
        elif x%2 == 0:
            print(x)


liczby = [2,4,"A","E",2,4,"A","E",5,6]

Parzyste(liczby)