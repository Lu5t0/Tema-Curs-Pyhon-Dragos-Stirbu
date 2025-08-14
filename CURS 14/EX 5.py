import csv

def pret_total():
    with open('vanzari.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            id = row['id_produs']
            try:
                pret = float(row['pret_unitar'])
                cantitate = float(row['cantitate'])
                valoare = cantitate * pret
                if valoare > 100:
                    print(f"Id produs: {id} - valoare totala: {valoare} lei")
            except ValueError:
                print(f"Date invalide in randul: {row}")

if __name__ == "__main__":
    pret_total()