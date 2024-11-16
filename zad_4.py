def CoDrugi(liczby):
    if len(liczby) != 10:
        print("Zła ilość")
        return
    for x in range(len(liczby)):
        if type(liczby[x]) != int and type(liczby[x]) != float:
            continue
        elif x%2 == 0:
            print(x)


liczby = [0,1,2,3,4,5,6,7,8,9]

CoDrugi(liczby)