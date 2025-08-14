import csv

def marire_salariu():
    angajati_modificati = []
    with open('angajati2.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            nume = row['nume']
            salariu = float(row['salariu'])
            salariu_nou = round(salariu * 1.10, 2)
            angajati_modificati.append({"nume": nume, "salariu": salariu_nou})
    with open('angajati2.csv', "w", newline='') as csvfile:
        fieldnames = ['nume', 'salariu']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(angajati_modificati)

if __name__ == '__main__':
    marire_salariu()