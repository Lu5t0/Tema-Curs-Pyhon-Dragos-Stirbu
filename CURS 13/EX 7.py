def numer_pare():
    try:
        with open("number.txt, "r"") as fisier:
            lista = fisier.readlines()
        lista_numere_pare = []
        for element in fisier:
            try:
                if int(element) % 2 == 0:
                    lista_numere_pare.append(element)
            except ValueError:
                pass
        with open("EventNumbers.txt", "w") as fisier:
            fisier.writelines(lista_numere_pare)
    except FileNotFoundError:
        print("File not found")
    except Exception:
        print("Something went wrong")

if __name__ == "__main__":
    numer_pare()