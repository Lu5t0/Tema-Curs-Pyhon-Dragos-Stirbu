import csv
def email_unic():
    unice = []
    with open('emailuri.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            if row not in unice:
                unice.append(row)
        return unice
def email_unice_nou():
    fisier = "emailuri_unice.csv"
    with open('emailuri_unice.csv', 'w', newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(email_unic())
        print(f"Fisierul '{fisier}' a fost creat cu succes.")


if __name__ == '__main__':
    email_unice_nou()

