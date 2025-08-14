def adunare():
    try:
        sir_de_numere = 0
        while True:
            numar_nou = str(input("Intrudu un numar intreg sau introdu 'stop' pentru a opri aplicatia: "))
            if numar_nou.lower() == "stop":
                break
            sir_de_numere += float(numar_nou)
            print(sir_de_numere)
    except ValueError:
        print("Valoare invalida")

if __name__ == "__main__":
    adunare()
