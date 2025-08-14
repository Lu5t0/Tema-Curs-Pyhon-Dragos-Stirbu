def f_numar(numar):
    n_str = str(numar)
    lungine = len (n_str)
    termeni = []

    for i, cifra in enumerate(n_str):
        if cifra != "0":
            putere = lungine - i - 1 # putere = 3 - 0 - 1 = 2
            termen = cifra + "0" * putere # termen = 1 + "0" * 2
            termeni.append(termen)



    return numar, "+".join(termeni)

if __name__ == "__main__":
    print(f_numar(114))