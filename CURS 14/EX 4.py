import csv
def medie_peste_8():
    suma_note = {}
    numar_note = {}
    with open("note.csv", "r", newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            nume = row["nume_elev"]
            try:
                nota = float(row["nota"])
            except ValueError:
                print(f"Nota invalida pentru {nume}: {row['nota']}")
                continue
            if nume in suma_note:
                suma_note[nume] += nota
                numar_note[nume] += 1
            else:
                suma_note[nume] = nota
                numar_note[nume] = 1
        print("Elevii cu media peste 8:")
        for nume in suma_note:
            media = suma_note[nume] / numar_note[nume]
            if media > 8:
                print(f"{nume} - media {media:.2f}")


if __name__ == '__main__':
    medie_peste_8()