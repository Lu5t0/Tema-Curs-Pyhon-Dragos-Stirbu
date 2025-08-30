# Înmulțirea elementelor corespunzătoare
# Date două liste de numere, folosește map și lambda pentru a înmulți elementele corespunzătoare dintre
# cele două liste (din [2, 4, 6] si [3, 5, 7] obtinem [6, 20, 42]).

if __name__ == '__main__':
    lista1 = [2,4,6]
    lista2 = [3,5,7]

    total = list(map(lambda x,y: x * y, lista1, lista2))
    print(total)