import csv

def lista_elevi():
    filename = "note.csv"
    note = [
        ["nume_elev", "materie", "nota"],
        ["Andrei Popescu", "Romana", 6],
        ["Ana Dobre","Istorie", 8],
        ["Ion Ionescu", "Biologie", 10],
        ["Ana Dobre", "Matematica", 9],
        ["Ion Ionescu", "Romana", 8],
        ["Andrei Popescu", "Matematica", 4],

    ]
    with open('note.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(note)
        print(f"Fisierul '{filename}' a fost creat cu succes.")

if __name__ == '__main__':
    lista_elevi()