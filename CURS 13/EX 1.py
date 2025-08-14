def numar_linii_fisier():
    try:
        with open("Fisier1.txt", "r") as fisier:
            numer_linii = 0
            for line in fisier:
                numer_linii += 1
        print(numer_linii)
    except FileNotFoundError:
        print("Fisier1.txt not found")
    except Exception as e:
        print(f"A aparut o eroare: {e}")

if __name__ == "__main__":
    numar_linii_fisier()