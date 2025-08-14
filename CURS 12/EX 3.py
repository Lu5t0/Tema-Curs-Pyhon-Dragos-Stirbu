def operatie_2_nr():
    try:
        numar1 = float(input("Scrie primul numar: "))
        numar2 = float(input("Scrie al doilea numar: "))
        operatie = input("Scrie operatie: ")
        if operatie == "+":
            print(numar1 + numar2)
        elif operatie == "-":
            print(numar1 - numar2)
        elif operatie == "*":
            print(numar1 * numar2)
        elif operatie == "/":
            print(numar1 / numar2)
        else:
            print("Operatie invalida")
    except ValueError:
        print("Numar invalid")
    except ZeroDivisionError:
        print("Al doilea numar nu poate fi 0 pentru impartire")


if __name__ == "__main__":
    operatie_2_nr()

