def sortare(pers1, pers2, pers3):
    sort_nume = [pers1, pers2, pers3]
    sort_nume.sort()

    inversate = [(v[1], v[0],v[2]) for v in sort_nume]
    inversate.sort()
    sort_varsta = [(v[1], v[0], v[2]) for v in inversate]

    inaltime = [(i[2], i[1], i[0]) for i in sort_nume]
    inaltime.sort()
    sort_inaltime = [(i[2], i[1], i[0]) for i in inaltime]


    print(sort_nume)
    print(sort_varsta)
    print(sort_inaltime)

if __name__ == "__main__":
    print(sortare(("Dan", 33, 170), ("Mihai", 20, 180), ("Daniel", 40, 173)))