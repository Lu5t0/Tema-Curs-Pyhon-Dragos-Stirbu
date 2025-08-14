
def numere_2():
    try:
        numar1 = float(input("Introdu primul numar:"))

        while True:
            try:
                numar2 = float(input("Introdu al doile numar:"))
                if numar2 == 0:
                    print("Al doilea numar nu poate sa fie 0.Incercati din nou.")
                else:
                    break
            except ValueError:
                print("Introduceti un numar valid")
        rezultat = numar1 / numar2
        print(f"Rezultat: {rezultat}")
    except ZeroDivisionError:
        print("Al doilea numar nu poate sa fie 0.")
    except Exception as e:
        print(f"A aparut o eroare neasteptata:{e}")

if __name__ == "__main__":
    numere_2()