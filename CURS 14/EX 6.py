import csv

def cheltuieli_citite():
    "Citim suma si calulcam totalul"
    suma_totala = {}
    with open('cheltuieli.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            categorie = row['categorie']
            try:
                suma = float(row['suma'])
            except ValueError:
                print(f"Valoarea sumei pentru categoria '{categorie}' este invalida.")
            if categorie not in suma_totala:
                suma_totala[categorie] = suma
            else:
                suma_totala[categorie] += suma
        return suma_totala
def cheltuieli_totale(suma_totala, fisier_output):
    "Scriem suma totala in fisier_output"
    with open(fisier_output, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["categorie","total_suma"])
        for categorie, total  in suma_totala.items():
            writer.writerow([categorie, total])


if __name__ == "__main__":
    cheltuieli_totale(cheltuieli_citite(),'total_pe_categorie.csv')