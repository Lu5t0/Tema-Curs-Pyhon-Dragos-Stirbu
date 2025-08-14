def numar_variabil(*args):

    lista_numere = []
    for i in args:
        lista_numere += i

    return lista_numere

if __name__ == "__main__":
    print(numar_variabil([1,2,3,4,5],[6,7,8,9],[10, 11, 12, 13] ))

