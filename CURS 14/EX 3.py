import csv

def angajati():
    numar_angajati = 0
    with open("angajati.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for _ in reader:
            numar_angajati += 1
    print(f"Numarul de angajari:{numar_angajati}")

if __name__ == '__main__':
    angajati()