def Pomnoz(liczby):
    if len(liczby) != 5:
        print("Zła ilość")
        return
    for x in liczby:
        if type(x) != int and type(x) != float:
            continue
        print(x*2)
    nowaLista = [x*2 for x in liczby if type(x) == int or type(x) == float]

    return nowaLista

liczby = [2,4,"A","E"]

lista = Pomnoz(liczby)

print(lista)
