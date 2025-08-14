import csv

def produse():

    with open("produse.csv","r") as file:
        reader = csv.reader(file)
        header = next(reader)
        print(f"{header[0]:<12}{header[1]:<10}{header[2]:<5}")

        for row in reader:
            id_produs, nume, pret = row
            print(f"{id_produs:<12}{nume:<10}{pret:<5}")

if __name__ == "__main__":
    produse()