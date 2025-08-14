def elemente_5():
    lista = ["mere", "banane", "mure", "pere", "struguri"]


    try:
        index = int(input("Introdu un index:"))
        print(f"Elementul de la indexul {index} este: {lista[index]}")
    except IndexError:
        print("Indexul introdus este in afara limitelor listei.")
    except ValueError:
        print("Eroare: Introdu un  numar intreg valid.")



if __name__ == "__main__":
    elemente_5()