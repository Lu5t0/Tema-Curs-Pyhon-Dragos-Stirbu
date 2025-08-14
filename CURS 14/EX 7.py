import csv

def calcul_medie():
    "Calcul medie si  s-a introdus status"
    note_studenti = {}
    with open("studenti.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            nume = row["nume_elev"]
            note = float(row["nota"])
            if nume in note_studenti:
                note_studenti[nume].append(note)
            else:
                note_studenti[nume] = [note]
        studenti = []
        for nume, note in note_studenti.items():
            media = sum(note) / len(note)
            status = "Promovat" if media > 5 else "Corigent"
            studenti.append({
                "nume_elev": nume,
                "media": round(media, 2),
                "status": status,
            })
        return studenti

def scrie_studenti(studenti, fisier_de_iesire):
    "Creaza noul fisier cu status"
    with open(fisier_de_iesire, "w", newline="") as csvfile:
        fieldnames = ["nume_elev", "media", "status"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(studenti)


if __name__ == '__main__':
    scrie_studenti(calcul_medie(), fisier_de_iesire="studenti_actualizat.csv")
